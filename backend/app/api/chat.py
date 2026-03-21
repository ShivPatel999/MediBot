from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.core.llm_client import generate_medibot_response

router = APIRouter()

EMERGENCY_KEYWORDS = ["chest pain", "cant breathe", "cannot breathe", "heart attack",
                      "stroke", "unconscious", "throat closing", "anaphylaxis"]

@router.post("/", response_model=ChatResponse)
async def chat_with_medibot(request: ChatRequest):
    if any(kw in request.message.lower() for kw in EMERGENCY_KEYWORDS):
        return ChatResponse(
            is_medical=True,
            chat_message="EMERGENCY: You may be experiencing a serious medical emergency. Please call 911 or go to your nearest emergency room immediately. Do not rely on this chatbot. Note: I am an AI, not a doctor.",
            urgency="EMERGENCY"
        )

    try:
        response = await generate_medibot_response(request.message, request.history)
        if not response:
            raise HTTPException(status_code=500, detail="Failed to generate response.")
        return response
    except Exception as e:
        print(f"Route Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))