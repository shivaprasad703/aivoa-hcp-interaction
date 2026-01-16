class AgentApp:
    def invoke(self, data):
        return {
            "output": f"Interaction logged successfully: {data['input']}"
        }

app = AgentApp()
