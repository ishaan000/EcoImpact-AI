from backend.agents.base_agent import BaseAgent 
from backend.core.state_manager import StateManager

class EnergyAgent(BaseAgent):
    """Agent specialized in energy efficiency and sustainability solutions."""

    def __init__(self, name="Energy AI", category="energy"):
        super().__init__(name, category)

    def handle_task(self, user_id: str, user_input: str):
        """Process energy-related queries with summarized memory."""

        past_summary = StateManager.summarize_interactions(user_id, "energy_agent")

        prompt = f"""
        You are an expert in energy conservation.
        Provide advice based on past relevant user queries.

        {past_summary}

        User's new question: {user_input}
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )

        StateManager.save_interaction(user_id, "energy_agent", user_input)

        return response.choices[0].message.content.strip()