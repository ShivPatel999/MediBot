import os
import json
from datetime import date
from groq import AsyncGroq
from app.models.schemas import ChatResponse
from app.db.init_db import MOCK_DB
from pydantic import ValidationError

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

def get_slim_db():
    """Send only condition names + aliases to save tokens. Full data fetched separately."""
    slim = {}
    for condition, data in MOCK_DB.items():
        slim[condition] = {
            "aliases": data.get("aliases", []),
            "urgency": data.get("urgency", "Low"),
            "meds": [m["name"] for m in data.get("meds", [])],
            "warning": data.get("warning", "")
        }
    return slim

def get_condition_data(user_input: str):
    """Find the best matching condition from user input."""
    user_lower = user_input.lower()
    for condition, data in MOCK_DB.items():
        if condition in user_lower:
            return condition, data
        for alias in data.get("aliases", []):
            if alias in user_lower:
                return condition, data
    return None, None

async def generate_medibot_response(user_input: str) -> ChatResponse:
    today = date.today().strftime("%B %d, %Y")

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

    # Try to pre-match the condition so we only send relevant data
    condition_name, condition_data = get_condition_data(user_input)

    if condition_data:
        # Send only the matched condition — keeps prompt short
        db_context = json.dumps({condition_name: condition_data}, indent=2)
    else:
        # Send slim version of full DB for matching
        db_context = json.dumps(get_slim_db(), indent=2)

    conditions_list = ", ".join(MOCK_DB.keys())

    system_prompt = f"""You are Medibot, a medical information assistant.
Today's date is {today}.
Supported conditions: {conditions_list}

RELEVANT KNOWLEDGE:
{db_context}

RULES:
1. Greetings ("hi","hello"): is_medical=false, introduce yourself, list supported conditions.
2. Date questions: is_medical=false, answer with {today}.
3. General questions ("what is X", "what causes X"): is_medical=false, answer helpfully.
4. Any symptom/health complaint: is_medical=true.
   - Use the RELEVANT KNOWLEDGE above for medications, urgency, warning_signs.
   - Handle typos charitably.
   - Unknown symptom: is_medical=true, medications=[], recommend seeing a doctor.
5. Always end chat_message with: "Note: I am an AI, not a doctor."

Respond ONLY in valid JSON: {json.dumps(manual_schema)}"""

    try:
        completion = await client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )

        raw_json = completion.choices[0].message.content
        return ChatResponse.model_validate_json(raw_json)

    except ValidationError as e:
        print(f"Validation Error: {e}")
        return ChatResponse(
            is_medical=False,
            chat_message="I had trouble with that. Try asking about a symptom like 'I have a headache'."
        )
    except Exception as e:
        print(f"Groq Error: {e}")
        return None