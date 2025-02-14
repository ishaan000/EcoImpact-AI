from backend.agents.base_agent import BaseAgent
from backend.core.state_manager import StateManager

class FoodAgent(BaseAgent):
    """Agent specialized in food sustainability and eco-friendly eating habits."""

    def __init__(self, name="Food AI", category="food"):
        super().__init__(name, category)

    def handle_task(self, user_id: str, user_input: str):
        """Process food sustainability queries with summarized memory."""

        past_summary = StateManager.summarize_interactions(user_id, "food_agent")

        prompt = f"""
        You are an expert in food sustainability and reducing food waste.
        Provide advice based on past relevant user queries.

        {past_summary}

        User's new question: {user_input}
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )

        StateManager.save_interaction(user_id, "food_agent", user_input)

        return response.choices[0].message.content.strip()