REGISTRY: dict[str, dict] = {}


def register_agent(agent_id: str, capabilities: list[str]):
    REGISTRY[agent_id] = {
        "agent_id": agent_id,
        "capabilities": capabilities,
        "online": True,
    }
    return REGISTRY[agent_id]


def find_agents_by_capability(capability: str):
    return [agent for agent in REGISTRY.values() if capability in agent["capabilities"]]
