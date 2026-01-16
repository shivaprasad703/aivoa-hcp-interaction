from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(data: dict):
    text = data.get("message", "")

    # Mock AI parsing (INTERVIEW LEVEL – PERFECT)
    return {
        "hcp_name": "Dr. Shiva",
        "interaction_type": "Meeting",
        "date": "2026-01-16",
        "time": "12:00",
        "attendees": "Shivaprasad",
        "topics": "Hero product discussion",
        "sentiment": "Positive",
        "outcomes": "Interested in Hero",
        "follow_up": "Schedule follow-up in 2 weeks",
        "summary": f"Interaction logged successfully: {text}"
    }
