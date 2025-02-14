import openai
from backend.config import OPENAI_API_KEY 
class BaseAgent:
    """Base class for AI Agents."""

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)

    def handle_task(self, user_input: str):
        """Override this method in child classes to process tasks."""
        raise NotImplementedError("Each agent must implement handle_task().")