import os
from fastapi import FastAPI
from backend.core.orchestrator import Orchestrator 
from backend.core.state_manager import StateManager
from rq import Queue
from redis import Redis
from rq.job import Job
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
ENV = os.getenv("ENV", "development")  # Default to "development"
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

# Setup Redis connection
redis_conn = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
)

task_queue = Queue(connection=redis_conn)

app = FastAPI()

# Dynamic CORS Configuration
if ENV == "development":
    allowed_origins = ["*"]  # Allow all origins for local testing
else:
    allowed_origins = os.getenv("CORS_ALLOWED_ORIGINS", "https://ecoimpact.ai").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = Orchestrator()

@app.get("/")
def home():
    return {"message": "Welcome to EcoImpact AI"}

@app.get("/assign-task/")
def assign_task(user_id: str, agent_name: str, user_input: str):
    """Assigns a sustainability-related task to an AI agent"""
    result = orchestrator.assign_task(user_id, agent_name, user_input)
    return {"status": result}

@app.get("/job-result/")
def get_job_result(job_id: str):
    """Fetch the result of a queued task"""
    try:
        job = Job.fetch(job_id, connection=redis_conn)
        if job.is_finished:
            return {"status": "completed", "result": job.result}
        elif job.is_failed:
            return {"status": "failed", "error": str(job.exc_info)}
        else:
            return {"status": "processing"}
    except Exception as e:
        return {"status": "error", "message": f"Job not found: {str(e)}"}

@app.delete("/reset-memory/")
def reset_memory(user_id: str):
    """Clears all stored AI memory for a user."""
    StateManager.clear_history(user_id)
    return {"message": "User memory reset successfully."}