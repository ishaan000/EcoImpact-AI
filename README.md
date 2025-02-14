# EcoImpact AI

## Overview

EcoImpact AI is a sustainability-focused AI system that provides eco-friendly solutions through intelligent agents. It consists of a **FastAPI backend** for AI processing and a **Next.js 15 frontend**.

---

## Tech Stack

- **Backend:** FastAPI, Python, Redis Queue (RQ), OpenAI API
- **Frontend:** Next.js 15, TypeScript, Material-UI (MUI)
- **Database & Caching:** Redis for task management

---

## Features

- AI-powered agents for sustainability guidance  
- Redis Queue for background task handling  
- Next.js 15 frontend with Material-UI  
- Dark Mode UI with chat-based interaction  
- API with CORS support for smooth communication  

---

## Getting Started

### Backend Setup (FastAPI + Redis + RQ)

```sh
# Clone the repository
git clone https://github.com/yourrepo/EcoImpact-AI.git
cd EcoImpact-AI

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Start Redis
redis-server

# Start the backend server
uvicorn backend.api.main:app --reload
```

### Frontend Setup (Next.js 15 + MUI)
```sh
# Move to frontend directory
cd frontend

# Install dependencies
yarn install  # or npm install

# Start the frontend server
yarn dev  # or npm run dev
```

---

## AI Agents 

- GeneralAgent: Handles general sustainability questions  
- TransportAgent: Provides eco-friendly transport advice
- EnergyAgent: Suggests energy-efficient practices
- FoodAgent: Recommends sustainable food choices

---
## API Endpoints
- GET	`/`	Root API endpoint
- GET	`/assign-task/`	Assigns a task to an agent
- GET	`/job-result/`	Fetches task results
- DELETE	`/reset-memory/`	Clears user memory
---

## API Usage with cURL

### 1) Assign a Task to an AI Agent
```sh
curl -X GET "http://127.0.0.1:8000/assign-task/" \
     -H "Content-Type: application/json" \
     --data-urlencode "user_id=user_123" \
     --data-urlencode "agent_name=transport_agent" \
     --data-urlencode "user_input=How can I reduce my carbon footprint?"
```

### Response Example:

```json
{
  "status": "job_id_123456789"
}
```
### 2) Fetch Task Result
```sh
curl -X GET "http://127.0.0.1:8000/job-result/" \
     -H "Content-Type: application/json" \
     --data-urlencode "job_id=job_id_123456789"
```

### Response Example:

```json
{
  "status": "completed",
  "result": "Use public transport, carpool, or switch to an electric vehicle."
}

```

## 3) Reset AI Memory
```sh
curl -X DELETE "http://127.0.0.1:8000/reset-memory/" \
     -H "Content-Type: application/json" \
     --data-urlencode "user_id=user_123"
```
### Response Example:

```json
{
  "message": "User memory reset successfully."
}
```










