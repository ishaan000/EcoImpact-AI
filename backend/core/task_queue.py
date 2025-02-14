from backend.core.agent_registry import AGENT_REGISTRY
from rq import Queue
from redis import Redis
import time

# Connect to Redis
redis_conn = Redis()
task_queue = Queue(connection=redis_conn)

def execute_task(agent_name: str, user_id: str, user_input: str):
    """Standalone function that calls an agent's task handler."""
    agent = AGENT_REGISTRY.get(agent_name)
    if not agent:
        return f"❌ Agent '{agent_name}' not found!"
    
    return agent.handle_task(user_id, user_input)

def queue_task(agent_name: str, user_id: str, user_input: str):
    """Queues a task for execution by the AI agent."""
    job = task_queue.enqueue(execute_task, agent_name, user_id, user_input)
    return job.get_id()  # Returns job ID for tracking

def get_task_result(job_id: str):
    """Fetches job result from Redis."""
    job = task_queue.fetch_job(job_id)

    if job is None:
        return {"status": "error", "message": "Job not found"}

    if job.is_finished:
        return {"status": "completed", "result": job.result}
    elif job.is_failed:
        return {"status": "failed", "error": str(job.exc_info)}
    else:
        return {"status": "in_progress"}