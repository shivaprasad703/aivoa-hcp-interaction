from langchain_groq import ChatGroq
from database import SessionLocal, Interaction

llm = ChatGroq(
    groq_api_key="PASTE_YOUR_GROQ_API_KEY_HERE",
    model_name="gemma2-9b-it"
)

def log_interaction_tool(text: str):
    response = llm.invoke(
        f"Summarize and detect sentiment: {text}"
    ).content

    db = SessionLocal()
    interaction = Interaction(
        hcp_name="Doctor",
        summary=response,
        sentiment="Positive",
        follow_up="Follow up suggested"
    )
    db.add(interaction)
    db.commit()

    return "Interaction logged successfully"

def edit_interaction_tool(id: int, new_text: str):
    db = SessionLocal()
    interaction = db.query(Interaction).filter(
        Interaction.id == id
    ).first()
    interaction.summary = new_text
    db.commit()
    return "Interaction updated"

def fetch_hcp_history_tool(hcp_name: str):
    db = SessionLocal()
    return db.query(Interaction).all()

def suggest_followup_tool(text: str):
    return llm.invoke(f"Suggest follow up: {text}").content

def summarize_interaction_tool(text: str):
    return llm.invoke(f"Summarize: {text}").content
