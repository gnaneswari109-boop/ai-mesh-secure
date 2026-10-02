from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SessionPairRequest(BaseModel):
    agent_a: str
    agent_b: str


@router.post("/pair")
async def pair_agents(payload: SessionPairRequest):
    from app.services.pairing import create_pairing
    return {"status": "pairing_started", "pairing": create_pairing(payload.agent_a, payload.agent_b)}


@router.post("/approve")
async def approve_agents(session_id: str):
    from app.services.pairing import approve_pairing
    return {"status": "approved", "pairing": approve_pairing(session_id)}
