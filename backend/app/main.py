from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat, triage
from app.db.init_db import initialize_database

app = FastAPI(title="Medibot API", version="1.0.0")

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run DB init on startup
@app.on_event("startup")
async def startup_event():
    initialize_database()

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(triage.router, prefix="/api/triage", tags=["triage"])

@app.get("/")
async def root():
    return {"message": "Medibot API is running. Systems nominal."}