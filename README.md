# AI Mesh Secure

The AI Mesh Secure project is a production-ready prototype for a Bluetooth-like multi-agent architecture.

It includes:
- FastAPI REST API
- Redis event bus
- agent registry and discovery
- secure pairing with session secrets
- signed message verification
- task DAG orchestration
- memory tracking
- Docker deployment
- gRPC protocol design for inter-agent communication

## Architecture

- Agent discovery
- Session pairing and trust creation
- Secure message signing
- Task DAG scheduling
- Shared memory
- Result aggregation
- Event-driven messaging

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Run with Docker

```bash
docker-compose up --build
```

## Endpoints

- POST /agents/register
- GET /agents
- GET /agents/capabilities/{capability}
- POST /sessions/pair
- POST /sessions/approve
- POST /workflow/run
- GET /health

## gRPC

The proto definition is in `proto/mesh.proto`.

Generate code with:

```bash
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/mesh.proto
```

## Security model

- each agent can register an identity
- pairing creates a shared session secret
- all inter-agent messages are signed
- signatures are validated before processing
- session expiry is enforced

## Production notes

This prototype is designed for deployment and extension, with a clear path to:
- PostgreSQL persistence
- distributed workers
- TLS and mTLS
- monitoring and tracing
- retries and dead-letter routing
