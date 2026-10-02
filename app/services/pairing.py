import hashlib
from datetime import datetime, timedelta

PAIRINGS: dict[str, dict] = {}


def generate_session_secret(agent_a: str, agent_b: str):
    seed = f"{agent_a}:{agent_b}:{datetime.utcnow().isoformat()}".encode()
    return hashlib.sha256(seed).hexdigest()


def create_pairing(agent_a: str, agent_b: str):
    session_id = generate_session_secret(agent_a, agent_b)
    PAIRINGS[session_id] = {
        "session_id": session_id,
        "agent_a": agent_a,
        "agent_b": agent_b,
        "status": "pending",
        "secret": generate_session_secret(agent_a, agent_b),
        "created_at": datetime.utcnow().isoformat(),
        "expires_at": (datetime.utcnow() + timedelta(minutes=10)).isoformat(),
    }
    return PAIRINGS[session_id]


def approve_pairing(session_id: str):
    if session_id not in PAIRINGS:
        raise ValueError("Unknown pairing session")
    PAIRINGS[session_id]["status"] = "active"
    return PAIRINGS[session_id]


def get_pairing(session_id: str):
    return PAIRINGS.get(session_id)
