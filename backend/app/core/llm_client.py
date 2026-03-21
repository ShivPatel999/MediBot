import os
import json
from groq import AsyncGroq
from app.models.schemas import ChatResponse
from app.db.init_db import MOCK_DB
from pydantic import ValidationError

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

async def generate_medibot_response(user_input: str) -> ChatResponse:
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

    system_prompt = f"""
    You are Medibot, a friendly medical information assistant.

    KNOWLEDGE BASE:
    {json.dumps(MOCK_DB, indent=2)}

    RULES:
    1. Greetings ("hi", "hello"): set is_medical=false, respond warmly, ask how you can help.
    2. Symptoms detected: set is_medical=true.
       - Explain the symptom in chat_message.
       - Pull urgency, warning_signs, and medications ONLY from the KNOWLEDGE BASE.
       - If symptom not in knowledge base, say so and recommend seeing a doctor.
    3. Always end with: "Note: I am an AI, not a doctor."

    Respond ONLY in valid JSON matching this schema:
    {json.dumps(manual_schema)}
    """

    try:
        completion = await client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            response_format={"type": "json_object"},
            temperature=0.2
        )

        raw_json = completion.choices[0].message.content
        return ChatResponse.model_validate_json(raw_json)

    except ValidationError as e:
        print(f"Validation Error: {e}")
        return ChatResponse(
            is_medical=False,
            chat_message="I had trouble formatting that response. Could you rephrase your symptoms?"
        )
    except Exception as e:
        print(f"Groq Error: {e}")
        return None