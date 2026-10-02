from datetime import datetime, timedelta
from typing import Dict

PAIRINGS: Dict[str, dict] = {}


def create_pairing(agent_a: str, agent_b: str):
    session_id = f"{agent_a}:{agent_b}:{datetime.utcnow().isoformat()}"
    pair = {
        "session_id": session_id,
        "agent_a": agent_a,
        "agent_b": agent_b,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat(),
        "expires_at": (datetime.utcnow() + timedelta(minutes=10)).isoformat(),
    }
    PAIRINGS[session_id] = pair
    return pair


def approve_pairing(session_id: str):
    if session_id not in PAIRINGS:
        raise ValueError("Unknown pairing session")
    PAIRINGS[session_id]["status"] = "active"
    return PAIRINGS[session_id]
