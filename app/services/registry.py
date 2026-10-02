REGISTRY: dict[str, dict] = {}


def register_agent(agent_id: str, capabilities: list[str], public_key: str | None = None):
    REGISTRY[agent_id] = {
        "agent_id": agent_id,
        "capabilities": capabilities,
        "public_key": public_key,
        "online": True,
    }
    return REGISTRY[agent_id]


def find_agents_by_capability(capability: str):
    return [agent for agent in REGISTRY.values() if capability in agent["capabilities"]]


def list_agents():
    return list(REGISTRY.values())
