# AI Mesh Secure

Secure Bluetooth-like multi-agent AI mesh with:
- FastAPI API
- Redis event bus
- gRPC inter-agent protocol
- signed message verification
- session pairing
- task DAG orchestration
- shared memory
- deployment-ready Docker config

## Features

- Agent discovery and capability registration
- Secure pairing between agents
- Signed live message exchange
- gRPC service for agent communication
- Redis event-driven state propagation
- Multi-agent task orchestration
- Context memory and result aggregation

## Quick start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

For gRPC service:

```bash
python -m app.grpc_server
```

## API examples

Register agent:

```bash
curl -X POST http://localhost:8000/agents/register \
  -H "Content-Type: application/json" \
  -d '{"agent_id":"researcher-1","capabilities":["research"]}'
```

Pair agents:

```bash
curl -X POST http://localhost:8000/sessions/pair \
  -H "Content-Type: application/json" \
  -d '{"agent_a":"researcher-1","agent_b":"coder-1"}'
```

Run workflow:

```bash
curl -X POST http://localhost:8000/workflow/run \
  -H "Content-Type: application/json" \
  -d '{"name":"AI strategy workflow"}'
```
