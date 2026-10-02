from typing import Dict

IDENTITY: Dict[str, dict] = {}


def register_identity(agent_id: str, public_key: str):
    IDENTITY[agent_id] = {
        "agent_id": agent_id,
        "public_key": public_key,
        "active": True,
    }
    return IDENTITY[agent_id]


def get_identity(agent_id: str):
    return IDENTITY.get(agent_id)
