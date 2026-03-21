from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str

class Medication(BaseModel):
    name: str
    used_for: str
    dosage: str
    side_effects: str
    warnings: str

class TriageGuidance(BaseModel):
    urgency_level: str
    possible_causes: List[str]
    self_care: List[str]
    when_to_see_doctor: str

class SymptomAnalysis(BaseModel):
    symptom: str
    severity: str = "Not specified"
    duration: str = "Not specified"

class ChatResponse(BaseModel):
    is_emergency: bool = False
    emergency_message: Optional[str] = None
    analysis: Optional[SymptomAnalysis] = None
    triage: Optional[TriageGuidance] = None
    medications: Optional[List[Medication]] = []