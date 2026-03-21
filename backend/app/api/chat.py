from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.core.llm_client import generate_medibot_response

router = APIRouter()

SEVERE_KEYWORDS = ["chest pain", "worst pain", "shortness of breath", "bleeding profusely"]

def check_emergency(text: str) -> bool:
    return any(keyword in text.lower() for keyword in SEVERE_KEYWORDS)

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if check_emergency(request.message):
        return ChatResponse(
            is_emergency=True,
            emergency_message="🚨 EMERGENCY WARNING: Severe symptom detected. Seek immediate medical attention. Do not rely on Medibot."
        )

    response_data = await generate_medibot_response(request.message)
    if not response_data:
        raise HTTPException(status_code=500, detail="Failed to generate response.")
        
    return response_data