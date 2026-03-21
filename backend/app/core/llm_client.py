import os
import json
from datetime import date
from groq import AsyncGroq
from app.models.schemas import ChatResponse, ChatMessage
from app.db.init_db import MOCK_DB, MEDICAL_QA
from pydantic import ValidationError
from typing import List

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

def get_condition_data(user_input: str, history: List[ChatMessage] = []):
    user_lower = user_input.lower()
    for condition, data in MOCK_DB.items():
        if condition in user_lower:
            return condition, data
        for alias in data.get("aliases", []):
            if alias in user_lower:
                return condition, data
    for msg in reversed(history[-4:]):
        msg_lower = msg.content.lower()
        for condition, data in MOCK_DB.items():
            if condition in msg_lower:
                return condition, data
            for alias in data.get("aliases", []):
                if alias in msg_lower:
                    return condition, data
    return None, None

async def generate_medibot_response(user_input: str, history: List[ChatMessage] = []) -> ChatResponse:
    today = date.today().strftime("%B %d, %Y")

    # Simplified schema — all fields optional except the two required ones
    manual_schema = {
        "type": "object",
        "properties": {
            "is_medical": {"type": "boolean"},
            "chat_message": {"type": "string"},
            "symptom": {"type": "string"},
            "severity": {"type": "string"},
            "urgency": {"type": "string"},
            "medications": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "purpose": {"type": "string"},
                        "how_to_use": {"type": "string"}
                    }
                }
            },
            "warning_signs": {"type": "string"}
        },
        "required": ["is_medical", "chat_message"]
    }

    condition_name, condition_data = get_condition_data(user_input, history)

    if condition_data:
        db_context = json.dumps({condition_name: condition_data})
    else:
        slim = {
            k: {
                "urgency": v.get("urgency", "Low"),
                "symptoms": v.get("symptoms", []),
                "causes": v.get("causes", ""),
                "meds": [m["name"] for m in v.get("meds", [])]
            }
            for k, v in MOCK_DB.items()
        }
        db_context = json.dumps(slim)

    conditions_list = ", ".join(MOCK_DB.keys())

    system_prompt = f"""You are Medibot, a medical information assistant.
Today: {today}.
Supported conditions: {conditions_list}

KNOWLEDGE BASE:
{db_context}

GENERAL QA:
{json.dumps(MEDICAL_QA)}

CRITICAL RULES:
1. ALWAYS return valid JSON with exactly these two fields at minimum: "is_medical" (boolean) and "chat_message" (string). Never omit them. Never return null for them.
2. For non-medical responses set: is_medical=false, medications=[], and leave symptom/severity/urgency/warning_signs as empty strings "".
3. For medical responses set: is_medical=true and fill in all fields from KNOWLEDGE BASE.

BEHAVIOR:
- Greetings ("hi","hello"): is_medical=false, introduce yourself, list all supported conditions.
- Date questions: is_medical=false, answer with {today}.
- General questions ("what is X", "what are symptoms of X", "what causes X", "tell me more", "how do I treat X"): is_medical=false, answer helpfully in 2-3 short sentences using KNOWLEDGE BASE and GENERAL QA. Use conversation history for context — if the user asks "what are the symptoms" look at the previous message to know what condition they mean.
- Symptom complaints ("I have X", "my X hurts"): is_medical=true, pull meds/urgency/warnings from KNOWLEDGE BASE.
- Follow-ups ("what else", "more options", "give me alternatives"): is_medical=true, use the symptom from conversation history.
- Medication questions ("tell me about ibuprofen"): is_medical=false, explain in 2-3 sentences.
- FORMAT: Write chat_message as plain short sentences only. No bullet points, no dashes, no numbered lists. Max 80 words.
- Always end chat_message with: "Note: I am an AI, not a doctor."

OUTPUT FORMAT — respond ONLY with this JSON structure, no other text:
{{
  "is_medical": true or false,
  "chat_message": "your response here",
  "symptom": "",
  "severity": "",
  "urgency": "",
  "medications": [],
  "warning_signs": ""
}}"""

    messages = [{"role": "system", "content": system_prompt}]

    for msg in history[-4:]:
        content = msg.content[:200] if len(msg.content) > 200 else msg.content
        messages.append({"role": msg.role, "content": content})

    messages.append({"role": "user", "content": user_input})

    try:
        completion = await client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            response_format={"type": "json_object"},
            temperature=0.1
        )

        raw_json = completion.choices[0].message.content
        parsed = json.loads(raw_json)

        # Manually ensure required fields always exist
        safe_response = {
            "is_medical": bool(parsed.get("is_medical", False)),
            "chat_message": str(parsed.get("chat_message", "I'm not sure how to answer that. Could you rephrase?")),
            "symptom": parsed.get("symptom") or "",
            "severity": parsed.get("severity") or "",
            "urgency": parsed.get("urgency") or "",
            "medications": parsed.get("medications") or [],
            "warning_signs": parsed.get("warning_signs") or ""
        }

        return ChatResponse(**safe_response)

    except Exception as e:
        print(f"Groq Error: {e}")
        return ChatResponse(
            is_medical=False,
            chat_message="I had trouble with that. Try asking about a symptom like 'I have a headache' or a question like 'what is anxiety'. Note: I am an AI, not a doctor."
        )