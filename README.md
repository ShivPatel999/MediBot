# Medibot

An AI-powered triage and OTC medication assistant. 

## Structure
- `backend/`: FastAPI Python application with OpenAI integration.
- `frontend/`: React/Vite web interface.

## Quick Start
1. Add your OpenAI Key to `.env` based on `.env.example`.
2. Run backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
3. Run frontend: `cd frontend && npm install && npm run dev`


docker compose up --build


http://localhost:5173