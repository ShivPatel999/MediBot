from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.core.llm_client import generate_medibot_response

router = APIRouter()

EMERGENCY_KEYWORDS = ["chest pain", "can't breathe", "cannot breathe", "worst pain of my life", "fainting", "unconscious", "heart attack", "stroke"]

@router.post("/", response_model=ChatResponse)
async def chat_with_medibot(request: ChatRequest):
    # Emergency safety layer
    if any(kw in request.message.lower() for kw in EMERGENCY_KEYWORDS):
        return ChatResponse(
            is_medical=True,
            chat_message="🚨 EMERGENCY: You may be experiencing a serious medical emergency. Please call 911 or go to your nearest emergency room immediately. Do not rely on this chatbot.",
            urgency="EMERGENCY"
        )

    try:
        response = await generate_medibot_response(request.message)
        if not response:
            raise HTTPException(status_code=500, detail="Failed to generate response.")
        return response
    except Exception as e:
        print(f"Route Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))