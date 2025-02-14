import redis
import json

# Connect to Redis (ensure Redis is running)
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

class StateManager:
    """Manages user state and past AI interactions."""

    @staticmethod
    def save_interaction(user_id: str, agent: str, message: str):
        """Saves user interaction history."""
        key = f"user:{user_id}:history"
        interaction = {"agent": agent, "message": message}

        # Append to Redis list
        redis_client.rpush(key, json.dumps(interaction))

    @staticmethod
    def get_relevant_interactions(user_id: str, agent: str, limit=3):
        """Retrieves the last N relevant interactions for a given agent."""
        key = f"user:{user_id}:history"
        history = redis_client.lrange(key, -10, -1)  # Retrieve last 10 interactions

        # Filter only relevant interactions for the same agent
        relevant = [json.loads(entry) for entry in history if json.loads(entry)["agent"] == agent]

        return relevant[-limit:]  # Return only the last `limit` relevant interactions

    @staticmethod
    def summarize_interactions(user_id: str, agent: str, limit=3):
        """Summarizes past interactions to prevent confusion."""
        history = StateManager.get_relevant_interactions(user_id, agent, limit)

        if not history:
            return "No prior interactions."

        summary = "\n".join([f"- {h['message']}" for h in history])
        return f"User's past relevant queries:\n{summary}"

    @staticmethod
    def clear_history(user_id: str):
        """Clears user interaction history."""
        key = f"user:{user_id}:history"
        redis_client.delete(key)