from pydantic import BaseModel


class AgentRequest(BaseModel):
    agent_id: str
    capabilities: list[str]


class PairRequest(BaseModel):
    agent_a: str
    agent_b: str


class PairApproveRequest(BaseModel):
    session_id: str


class WorkflowRequest(BaseModel):
    name: str
