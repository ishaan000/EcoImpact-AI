from backend.agents.base_agent import BaseAgent
from backend.core.state_manager import StateManager

class TransportAgent(BaseAgent):
    """Agent specialized in sustainable transportation solutions."""
    
    def __init__(self, name="Transport AI", category="transport"):
        super().__init__(name, category)

    def handle_task(self, user_id: str, user_input: str):
        """Process transport-related queries with context memory."""

        # Get summarized past interactions
        past_summary = StateManager.summarize_interactions(user_id, "transport_agent")

        prompt = f"""
        You are an expert in sustainable transport. 
        Provide advice based on past relevant user queries.

        {past_summary}

        User's new question: {user_input}
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )

        # Save new interaction to memory
        StateManager.save_interaction(user_id, "transport_agent", user_input)

        return response.choices[0].message.content.strip()