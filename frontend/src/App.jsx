import { useState } from "react";
import "./App.css";

function App() {
  const [aiText, setAiText] = useState("");
  const [formData, setFormData] = useState({
    hcp_name: "",
    interaction_type: "",
    date: "",
    time: "",
    attendees: "",
    topics: "",
    sentiment: "",
    outcomes: "",
    follow_up: "",
  });

  const handleAI = async () => {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: aiText }),
    });

    const data = await res.json();
    setFormData(data);
  };

  return (
    <div className="container">
      {/* LEFT SIDE FORM */}
      <div className="card">
        <h2>Log HCP Interaction</h2>

        <input value={formData.hcp_name} placeholder="HCP Name" />
        <input value={formData.interaction_type} placeholder="Interaction Type" />

        <div className="row">
          <input value={formData.date} placeholder="Date" />
          <input value={formData.time} placeholder="Time" />
        </div>

        <input value={formData.attendees} placeholder="Attendees" />

        <textarea value={formData.topics} placeholder="Topics Discussed" />

        <div className="radio">
          <label>
            <input type="radio" checked={formData.sentiment === "Positive"} readOnly />
            Positive
          </label>
          <label>
            <input type="radio" checked={formData.sentiment === "Neutral"} readOnly />
            Neutral
          </label>
          <label>
            <input type="radio" checked={formData.sentiment === "Negative"} readOnly />
            Negative
          </label>
        </div>

        <textarea value={formData.outcomes} placeholder="Outcomes" />
        <textarea value={formData.follow_up} placeholder="Follow-up Actions" />
      </div>

      {/* RIGHT SIDE AI */}
      <div className="card ai">
        <h2>AI Assistant</h2>
        <textarea
          placeholder="Log interaction details here..."
          value={aiText}
          onChange={(e) => setAiText(e.target.value)}
        />
        <button onClick={handleAI}>Log</button>
        <p className="success">{formData.summary}</p>
      </div>
    </div>
  );
}

export default App;
