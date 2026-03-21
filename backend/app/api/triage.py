from fastapi import APIRouter
from app.db.init_db import MOCK_DB

router = APIRouter()

@router.get("/symptoms")
async def get_supported_symptoms():
    """Endpoint to return a list of symptoms currently in our knowledge base."""
    return {"supported_symptoms": list(MOCK_DB.keys())}