# AI Mesh Secure with LLM Integration

A production-ready Bluetooth-like multi-agent AI mesh with integrated ChatGPT and Gemini.

## Features

- **Agent Discovery**: Dynamic agent registry with capability mapping
- **Secure Pairing**: Session-based trust with signed messages
- **LLM Integration**: ChatGPT and Gemini unified interface
  - Researcher agents use Gemini
  - Coder agents use ChatGPT
  - Summarizer agents use Gemini
- **Task DAG Orchestration**: Parallel execution with dependency management
- **Shared Memory**: Versioned context for inter-agent communication
- **Event Bus**: Redis-backed event propagation
- **Production Ready**: Docker deployment, error handling, retry logic

## Architecture

```
FastAPI REST API
    ↓
Agent Registry & Discovery
    ↓
Session Pairing (Secure)
    ↓
Workflow Scheduler (DAG)
    ↓
LLM Workers
    ├─ Researcher (Gemini)
    ├─ Coder (ChatGPT)
    └─ Summarizer (Gemini)
    ↓
Shared Memory
    ↓
Result Aggregation
    ↓
Redis Event Bus
```

## Quick Start

### Local Installation

```bash
# Clone repository
git clone https://github.com/gnaneswari109-boop/ai-mesh-secure.git
cd ai-mesh-secure

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys
```

### Set API Keys

```bash
# Add to .env
OPENAI_API_KEY=sk-your-openai-key
GEMINI_API_KEY=AIz-your-gemini-key
```

### Run Locally

```bash
uvicorn app.main:app --reload
```

Server runs at: http://localhost:8000

### Docker Deployment

```bash
# Start with Docker Compose
docker-compose up --build

# Or build and run separately
docker build -t ai-mesh-secure .
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=sk-... \
  -e GEMINI_API_KEY=AIz-... \
  ai-mesh-secure
```

## API Examples

### 1. Register Agent

```bash
curl -X POST http://localhost:8000/agents/register \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "researcher-1",
    "capabilities": ["research"],
    "public_key": "demo-key"
  }'
```

### 2. Pair Agents

```bash
curl -X POST http://localhost:8000/sessions/pair \
  -H "Content-Type: application/json" \
  -d '{
    "agent_a": "researcher-1",
    "agent_b": "coder-1"
  }'
```

### 3. Run Workflow

```bash
curl -X POST http://localhost:8000/workflow/run \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI strategy workflow",
    "description": "Market research and implementation planning"
  }'
```

### 4. Health Check

```bash
curl http://localhost:8000/health
```

## Project Structure

```
ai-mesh-secure/
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── settings.py             # Configuration
│   ├── services/
│   │   ├── llm/
│   │   │   ├── base.py         # LLM provider interface
│   │   │   ├── openai_provider.py
│   │   │   ├── gemini_provider.py
│   │   │   ├── agent_llm.py    # Agent-to-LLM mapping
│   │   │   └── task_context.py # Prompt building
│   │   ├── worker_llm.py       # LLM-based execution
│   │   ├── registry.py         # Agent registry
│   │   ├── pairing.py          # Session pairing
│   │   ├── scheduler.py        # Task DAG
│   │   ├── memory.py           # Shared memory
│   │   ├── bus.py              # Redis event bus
│   │   └── auth.py             # Message signing
│   └── api/
│       ├── routes.py           # Route aggregation
│       ├── agent_routes.py
│       ├── session_routes.py
│       └── workflow_routes.py
├── proto/
│   └── mesh.proto              # gRPC definitions
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .env.example
```

## LLM Integration Details

### ChatGPT Provider

- Model: `gpt-4`
- Used for: Coding, orchestration
- Temperature: 0.7
- Max tokens: 2048

### Gemini Provider

- Model: `gemini-pro`
- Used for: Research, summarization
- Supports async generation

### Custom Prompt Building

Each task builds a contextualized prompt:

```python
Task: Research AI market trends
Task ID: research-1
Capability: research

Description: Market research and analysis

Context from previous tasks:
- market_size: $50B
- growth_rate: 25%

Input data:
- topic: AI adoption in 2024
- focus: market size and growth

Please provide a detailed and structured response.
```

## Security Model

- **Agent Identity**: Each agent has unique ID and public key
- **Session Secrets**: Shared secret generated during pairing
- **Message Signing**: All inter-agent messages are signed with SHA256
- **Signature Verification**: Receivers validate signatures before processing
- **Session Expiry**: Sessions expire after 10 minutes

## Error Handling

- Automatic retries with exponential backoff
- Fallback responses for missing LLM providers
- Comprehensive error logging
- Graceful degradation

## Production Considerations

- Add PostgreSQL for persistent state
- Implement Redis Streams for durable event log
- Use mTLS for inter-agent gRPC communication
- Add OpenTelemetry instrumentation
- Set up monitoring and alerts
- Implement rate limiting
- Add request/response caching
- Deploy with Kubernetes

## Development

### Testing

```bash
pytest tests/ -v
```

### Generate gRPC Code

```bash
bash scripts/generate_proto.sh
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT

## Support

For issues, questions, or suggestions, please open a GitHub issue.
