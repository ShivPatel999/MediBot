from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class Medication(BaseModel):
    name: str
    purpose: str
    how_to_use: Optional[str] = "Follow package instructions."

class ChatResponse(BaseModel):
    is_medical: bool
    chat_message: str
    symptom: Optional[str] = ""
    severity: Optional[str] = ""
    urgency: Optional[str] = ""
    medications: Optional[List[Medication]] = []
    warning_signs: Optional[str] = ""