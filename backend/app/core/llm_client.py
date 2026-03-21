import os
import json
from openai import AsyncOpenAI
from app.models.schemas import ChatResponse
from app.db.init_db import MOCK_DB

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_medibot_response(user_input: str) -> ChatResponse:
    system_prompt = f"""
    You are Medibot, a medical extraction and triage assistant.
    
    CRITICAL RULES:
    1. DO NOT give medical advice.
    2. Only suggest data found in this JSON database: {json.dumps(MOCK_DB)}
    3. Extract the symptom, severity, and duration.
    4. Provide general triage guidance strictly based on the database.
    
    You MUST respond in valid JSON matching the provided schema.
    """

    try:
        completion = await client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            response_format=ChatResponse,
            temperature=0.1
        )
        return completion.choices[0].message.parsed
    except Exception as e:
        print(f"LLM Error: {e}")
        return None