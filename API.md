# API Documentation

## AI Mesh Secure with LLM Integration

This API integrates ChatGPT and Gemini with the AI mesh orchestration system.

### Agent Registration

Register an agent with capabilities:

```bash
curl -X POST http://localhost:8000/agents/register \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "researcher-1",
    "capabilities": ["research"],
    "public_key": "demo-key"
  }'
```

### Session Pairing

Pair two agents for secure communication:

```bash
curl -X POST http://localhost:8000/sessions/pair \
  -H "Content-Type: application/json" \
  -d '{
    "agent_a": "researcher-1",
    "agent_b": "coder-1"
  }'
```

### Run Workflow

Execute a multi-agent workflow with LLM support:

```bash
curl -X POST http://localhost:8000/workflow/run \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI strategy workflow",
    "description": "Market research and implementation planning"
  }'
```

### Response Example

```json
{
  "workflow_name": "AI strategy workflow",
  "description": "Market research and implementation planning",
  "results": [
    {
      "task_id": "research-1",
      "summary": "[Gemini-generated research findings...]",
      "facts": ["Fact 1", "Fact 2", "Fact 3"]
    },
    {
      "task_id": "code-1",
      "summary": "[ChatGPT-generated implementation plan...]",
      "files": ["main.py", "service.py"]
    },
    {
      "task_id": "summary-1",
      "summary": "[Gemini-generated executive summary...]",
      "key_takeaways": ["Takeaway 1", "Takeaway 2", "Takeaway 3"]
    }
  ],
  "aggregated": {
    "summary": [...],
    "facts": [...],
    "artifacts": [...]
  }
}
```

## Agent-to-LLM Mapping

- **researcher**: Gemini
- **coder**: ChatGPT
- **summarizer**: Gemini
- **orchestrator**: ChatGPT

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   export OPENAI_API_KEY=sk-...
   export GEMINI_API_KEY=AIz-...
   ```

3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Docker

```bash
docker-compose up --build
```
