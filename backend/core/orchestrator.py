from .task_queue import queue_task  # Use relative import
class Orchestrator:
    """Manages AI task delegation."""

    def assign_task(self, user_id: str, agent_name: str, user_input: str):
        """Assigns a task to an agent and queues it."""
        return queue_task(agent_name, user_id, user_input)  # ✅ Pass user_id correctly