from pydantic import BaseModel


class PairRequest(BaseModel):
    agent_a: str
    agent_b: str


class PairApprovalRequest(BaseModel):
    session_id: str
