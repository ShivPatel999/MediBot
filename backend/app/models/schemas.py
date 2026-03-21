from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str

class Medication(BaseModel):
    name: str
    purpose: str
    how_to_use: str

class ChatResponse(BaseModel):
    is_medical: bool
    chat_message: str
    symptom: Optional[str] = None
    severity: Optional[str] = None
    urgency: Optional[str] = None
    medications: Optional[List[Medication]] = []
    warning_signs: Optional[str] = None