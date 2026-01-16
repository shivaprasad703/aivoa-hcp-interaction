
# Aivoa – Log HCP Interaction (AI-assisted)

This project is a **full-stack assignment** that demonstrates an AI-assisted interface to log HCP (Health Care Professional) interactions.

The application consists of:
- **Frontend**: React + Vite (UI)
- **Backend**: FastAPI (API)
- **AI Assistant (Mock)**: Parses free-text input and auto-fills structured fields

---

## 📂 Project Structure

```
aivoa-task1/
│
├── backend/
│   └── main.py          # FastAPI backend
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   └── package.json
│
└── README.md
```

---

## 🚀 Features

- Full-screen **two-panel layout**
  - Left: Log HCP Interaction Form
  - Right: AI Assistant
- AI Assistant accepts **natural language input**
- Backend parses text and returns structured data
- Form fields auto-populate from AI response
- Clean, enterprise-style UI

---

## 🛠 Tech Stack

- **Frontend**: React, Vite, CSS
- **Backend**: FastAPI, Python
- **API Communication**: REST (JSON)

---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup

```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

Backend will run at:
```
http://127.0.0.1:8000
```

Swagger Docs:
```
http://127.0.0.1:8000/docs
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at:
```
http://localhost:5173
```

---

## 🔗 API Endpoint

### POST `/chat`

**Request Body**
```json
{
  "message": "Met Dr. Shiva for a call on 16-01-2026 at 12:00. Positive discussion."
}
```

**Response**
```json
{
  "hcp_name": "Shiva",
  "interaction_type": "Call",
  "date": "2026-01-16",
  "time": "12:00",
  "attendees": "Shivaprasad",
  "topics": "Hero product discussion",
  "sentiment": "Positive",
  "outcomes": "Hero",
  "follow_up": "Shivae",
  "summary": "Interaction logged successfully"
}
```

---

## ✅ Assignment Outcome

This project fulfills the assignment by:
- Implementing a clean UI similar to the provided design
- Connecting frontend and backend
- Demonstrating AI-assisted data extraction
- Following best practices for code structure

---

## 👤 Author

**Polapally Shiva Prasad**  
MCA Graduate | Full Stack Python Developer  

---

## 📌 Notes

- AI logic is mocked for assignment/demo purposes
- Can be extended with real LLMs or database storage

