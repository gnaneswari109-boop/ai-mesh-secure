from fastapi import APIRouter
from pydantic import BaseModel

from app.services.registry import register_agent, list_agents, find_agents_by_capability
from app.services.pairing import create_pairing, approve_pairing
from app.services.scheduler import add_task, ready_tasks, mark_task_done, list_tasks
from app.services.worker import execute_task
from app.services.aggregator import aggregate_results

router = APIRouter()


class RegisterRequest(BaseModel):
    agent_id: str
    capabilities: list[str]
    public_key: str | None = None


class PairRequest(BaseModel):
    agent_a: str
    agent_b: str


class ApproveRequest(BaseModel):
    session_id: str


class WorkflowRequest(BaseModel):
    name: str
    description: str | None = None


@router.post("/register")
async def register(payload: RegisterRequest):
    agent = register_agent(payload.agent_id, payload.capabilities, payload.public_key)
    return {"status": "registered", "agent": agent}


@router.get("/")
async def list_all_agents():
    return {"agents": list_agents()}


@router.get("/capabilities/{capability}")
async def find_capability(capability: str):
    return {"matches": find_agents_by_capability(capability)}


@router.post("/pair")
async def pair_agents(payload: PairRequest):
    pair = create_pairing(payload.agent_a, payload.agent_b)
    return {"status": "pairing_started", "pairing": pair}


@router.post("/approve")
async def approve_agents(payload: ApproveRequest):
    pair = approve_pairing(payload.session_id)
    return {"status": "approved", "pairing": pair}
