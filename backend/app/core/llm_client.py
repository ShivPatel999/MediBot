import os
import json
import httpx
import pytz
from datetime import datetime
from groq import AsyncGroq
from app.models.schemas import ChatResponse, ChatMessage
from app.db.init_db import MOCK_DB, MEDICAL_QA
from typing import List
from bs4 import BeautifulSoup

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

async def web_search(query: str) -> str:
    """Search DuckDuckGo and scrape real results for up-to-date information."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        search_url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"

        async with httpx.AsyncClient(timeout=8.0, headers=headers, follow_redirects=True) as http:
            response = await http.get(search_url)

        soup = BeautifulSoup(response.text, "html.parser")

        results = []
        for result in soup.select(".result__snippet")[:4]:
            text = result.get_text(strip=True)
            if text and len(text) > 30:
                results.append(text)

        if results:
            combined = " | ".join(results)
            print(f"Web search found {len(results)} results for: {query}")
            return combined[:1500]

        return ""

    except Exception as e:
        print(f"Web search error: {e}")
        return ""

def needs_web_search(user_input: str) -> bool:
    """Detect questions that need real-time or statistical data."""
    web_keywords = [
        "which country", "what country", "highest rate", "lowest rate",
        "most common", "statistics", "how many people", "percentage",
        "latest", "recent", "current", "2024", "2025", "2026",
        "worldwide", "globally", "in the world", "according to",
        "who has the most", "which nation", "prevalence", "rate of",
        "news", "update", "new treatment", "new study", "research shows",
        "how common is", "how many", "what percent", "outbreak",
        "mortality rate", "survival rate", "life expectancy"
    ]
    user_lower = user_input.lower()
    return any(kw in user_lower for kw in web_keywords)

async def generate_medibot_response(user_input: str, history: List[ChatMessage] = []) -> ChatResponse:
    eastern = pytz.timezone("America/New_York")
    today = datetime.now(eastern).strftime("%B %d, %Y")

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
                    },
                    "required": ["name", "purpose", "how_to_use"]
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

    # Fetch real-time web data if needed
    web_context = ""
    if needs_web_search(user_input):
        web_data = await web_search(user_input)
        if web_data:
            web_context = f"\nREAL-TIME WEB SEARCH RESULTS (use this for accuracy):\n{web_data}\n"

    system_prompt = f"""You are Medibot, an accurate and up-to-date medical information assistant.
Today's date: {today}.
Supported conditions: {conditions_list}

KNOWLEDGE BASE:
{db_context}

GENERAL QA:
{json.dumps(MEDICAL_QA)}
{web_context}

CRITICAL ACCURACY RULES:
1. ALWAYS return valid JSON with "is_medical" (boolean) and "chat_message" (string). Never null.
2. If REAL-TIME WEB SEARCH RESULTS are provided, prioritize them over your training data for statistics, rates, and current information. Always use the most up-to-date figures available.
3. For medical responses: is_medical=true, fill all fields from KNOWLEDGE BASE. EVERY medication MUST have "name", "purpose", and "how_to_use" — never omit any field.
4. For non-medical responses: is_medical=false, medications=[], empty strings for other fields.
5. Be specific and accurate. If web data gives a specific number or country, use it. Do not generalize when specific data is available.
6. If you are unsure or data might be outdated, say so clearly in the response.

BEHAVIOR:
- Greetings ("hi", "hello"): is_medical=false, introduce yourself warmly, list supported conditions.
- Date questions: is_medical=false, answer exactly: "Today is {today}."
- Statistical questions ("which country", "highest rate", "how many people", "prevalence"): is_medical=false. Use REAL-TIME WEB SEARCH RESULTS if available. Give specific accurate numbers and sources. If no web data, answer from knowledge but note it may not be current.
- General medical questions ("what is X", "causes of X", "symptoms of X", "how to treat X"): is_medical=false, answer clearly in 2-3 sentences using KNOWLEDGE BASE and GENERAL QA. Use conversation history for context on follow-ups.
- Symptom complaints ("I have X", "my X hurts", "I feel X"): is_medical=true, pull all medications, urgency, and warning_signs from KNOWLEDGE BASE.
- Follow-ups ("what else", "more options", "alternatives", "tell me more"): use conversation history to determine the topic being discussed.
- Medication questions ("tell me about ibuprofen", "is X safe"): is_medical=false, give accurate explanation.
- FORMAT: Write chat_message as plain flowing sentences. No bullet points, dashes, or numbered lists inside chat_message. Maximum 100 words. Be warm, clear, and accurate.
- Always end every chat_message with: "Note: I am an AI, not a doctor."

OUTPUT — respond ONLY with this exact JSON structure:
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
            # Upgraded to 70B model — much more accurate and knowledgeable
            model="llama-3.3-70b-versatile",
            messages=messages,
            response_format={"type": "json_object"},
            temperature=0.1,
            max_tokens=1024
        )

        raw_json = completion.choices[0].message.content
        parsed = json.loads(raw_json)

        # Ensure how_to_use always exists in every medication
        medications = parsed.get("medications") or []
        fixed_medications = []
        for med in medications:
            fixed_medications.append({
                "name": med.get("name", ""),
                "purpose": med.get("purpose", ""),
                "how_to_use": med.get("how_to_use") or "Follow package instructions and consult a pharmacist."
            })

        safe_response = {
            "is_medical": bool(parsed.get("is_medical", False)),
            "chat_message": str(parsed.get("chat_message", "I am not sure how to answer that. Could you rephrase?")),
            "symptom": parsed.get("symptom") or "",
            "severity": parsed.get("severity") or "",
            "urgency": parsed.get("urgency") or "",
            "medications": fixed_medications,
            "warning_signs": parsed.get("warning_signs") or ""
        }

        return ChatResponse(**safe_response)

    except Exception as e:
        print(f"Groq Error: {e}")
        return ChatResponse(
            is_medical=False,
            chat_message="I had trouble with that. Try asking about a symptom like 'I have a headache' or a question like 'what is anxiety'. Note: I am an AI, not a doctor."
        )