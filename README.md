# 🩺 Medibot — AI-Powered Medical Information Assistant

Medibot is a full-stack AI chatbot that helps users identify OTC medication options, understand symptoms, and get general health guidance. Built with React, FastAPI, and Llama 3.1 via Groq, containerized with Docker.

> ⚕️ **Disclaimer:** Medibot provides general information only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional.

---

## 🏗️ Architecture
```
User (Browser)
     ↓
Frontend — React + Vite (port 5173)
     ↓
Backend — FastAPI + Python (port 8000)
     ↓
AI Layer — Llama 3.1 via Groq API
     ↓
Knowledge Base — Local medical database (init_db.py)
```

---

## 📁 File Structure
```
medibot/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app, CORS, routing
│   │   ├── api/
│   │   │   ├── chat.py          # Chat endpoint + emergency safety layer
│   │   │   └── triage.py        # Supported symptoms endpoint
│   │   ├── core/
│   │   │   └── llm_client.py    # Groq AI integration + conversation memory
│   │   ├── models/
│   │   │   └── schemas.py       # Pydantic data models
│   │   └── db/
│   │       └── init_db.py       # Medical knowledge base (25+ conditions)
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   └── ChatWindow.jsx   # Chat UI + conversation memory
│   │   └── services/
│   │       └── api.js
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- A free [Groq API key](https://console.groq.com)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/medibot.git
cd medibot
```

### 2. Set up your API key
```bash
cp .env.example .env
```
Open `.env` and add your key:
```
GROQ_API_KEY=gsk_your_key_here
```

### 3. Launch
```bash
docker compose up --build
```

### 4. Open in browser
- **Chat UI:** http://localhost:5173
- **API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

### 5. Stop
```bash
docker compose down
```

---

## 💬 Example Conversations

**Symptom:**
```
User: I have a really bad headache
Bot:  [Analysis] Symptom: headache | Severity: severe
      [Triage]   Urgency: Low
      [Meds]     Acetaminophen, Ibuprofen, Excedrin Migraine...
      [Warning]  Seek emergency care if worst headache of your life...
```

**Follow-up with memory:**
```
User: what causes it
Bot:  Headaches are commonly caused by tension, dehydration...

User: what else can I take
Bot:  [Returns alternative medications using previous context]
```

**General questions:**
```
User: what is OCD
Bot:  OCD is a mental health condition...

User: what are the symptoms
Bot:  [Remembers OCD from previous message and answers]
```

**Emergency:**
```
User: I have chest pain and cant breathe
Bot:  🚨 EMERGENCY: Call 911 immediately...
```

---

## 🧠 How It Works

### Safety Layer
Every message passes through an emergency keyword check in `chat.py` before reaching the AI. Keywords like "chest pain" or "heart attack" trigger an immediate hardcoded 911 response — the AI is never involved.

### Knowledge Base
All medical information lives in `init_db.py` as a controlled Python dictionary. The AI can only recommend medications that already exist in this database. This prevents hallucination of incorrect dosages or prescription medications. The database was enriched using the [HuggingFace medical QA dataset](https://huggingface.co/datasets/s200862/medical_qa_meds) containing 5,942 real medical Q&A pairs.

### Conversation Memory
Memory works in three parts:
1. **Frontend** stores the conversation history array and sends it with every request
2. **`get_condition_data()`** searches both the current message and history to find the relevant condition for follow-up questions
3. **Groq receives** the last 4 messages alongside the current one giving the AI full context

### Token Optimization
Instead of sending the entire 25-condition database with every message, `llm_client.py` detects the matched condition and sends only that condition's data keeping every prompt well within Groq's token limits.

---

## 🩺 Supported Conditions

**Physical Health:**
Allergy, Anaphylaxis, Asthma, Hives, Food Allergy, Headache, Sore Throat, Cold, Flu, Fever, Stomach Ache, Muscle Pain, Cough, Skin Rash, Heartburn, Diarrhea, Insomnia, Eye Irritation, Toothache, Back Pain, Dehydration

**Mental Health:**
Depression, Anxiety, Stress, PTSD, Bipolar Disorder, OCD, ADHD, Grief, Eating Disorder, Loneliness

---

## 🛡️ Safety Features

| Feature | Implementation |
|---|---|
| Emergency detection | Hardcoded bypass — AI never involved for 911 situations |
| No hallucinations | All meds pulled exclusively from verified local database |
| OTC only | Database contains no prescription medications |
| Medical disclaimer | Appended to every single AI response |
| No diagnosis | AI uses "common options include" language, never "you have X" |
| Schema validation | Pydantic validates every response before it reaches the user |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React 18 + Vite | Fast component-based chat UI |
| Backend | FastAPI Python 3.11 | Async API automatic docs data validation |
| AI Model | Llama 3.1 8B via Groq | Fast inference free tier JSON mode |
| Data Validation | Pydantic v2 | Structured type-safe request/response models |
| Containerization | Docker + Docker Compose | One-command deployment anywhere |
| Medical Data | HuggingFace dataset + custom DB | Real medical Q&A knowledge base |

---

## 🔧 Development

### Rebuild after code changes
```bash
docker compose down && docker compose up --build
```

### View live logs
```bash
docker logs medibot-backend-1
docker logs medibot-frontend-1
```

### Add a new condition
Open `backend/app/db/init_db.py` and add to `MOCK_DB`:
```python
"condition name": {
    "urgency": "Low",
    "aliases": ["alternate name", "common typo"],
    "symptoms": ["symptom 1", "symptom 2"],
    "causes": "Brief explanation.",
    "meds": [
        {
            "name": "Medication Name",
            "purpose": "What it treats",
            "how_to_use": "Dosage and instructions."
        }
    ],
    "warning": "When to seek medical attention."
}
```
Then rebuild: `docker compose up --build`

---

## 📋 API Reference

### POST `/api/chat/`

**Request:**
```json
{
  "message": "I have a headache",
  "history": [
    { "role": "user", "content": "hi" },
    { "role": "assistant", "content": "Hello! I'm Medibot..." }
  ]
}
```

**Response:**
```json
{
  "is_medical": true,
  "chat_message": "Headaches are very common...",
  "symptom": "headache",
  "severity": "Not specified",
  "urgency": "Low",
  "medications": [
    {
      "name": "Acetaminophen (Tylenol)",
      "purpose": "Pain relief and fever reduction",
      "how_to_use": "325-650mg every 4-6 hours. Do not exceed 3000mg/day."
    }
  ],
  "warning_signs": "Seek emergency care if worst headache of your life..."
}
```

### GET `/api/triage/symptoms`
Returns list of all supported conditions.

---

## 🌐 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com | Yes |

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) for ultra-fast LLM inference
- [Meta](https://ai.meta.com) for the Llama 3.1 model
- [HuggingFace](https://huggingface.co/datasets/s200862/medical_qa_meds) for the medical QA dataset
- [FastAPI](https://fastapi.tiangolo.com) for the backend framework