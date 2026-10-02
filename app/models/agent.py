from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class AgentSchema(BaseModel):
    agent_id: str
    capabilities: List[str]
    metadata: Dict[str, Any] = {}


class AgentRegisterRequest(BaseModel):
    agent_id: str
    capabilities: List[str]
    public_key: Optional[str] = None


class PairRequest(BaseModel):
    agent_a: str
    agent_b: str


class PairApprovalRequest(BaseModel):
    session_id: str


class WorkflowRequest(BaseModel):
    name: str
    description: Optional[str] = None


class MessageEnvelope(BaseModel):
    message_id: str
    sender: str
    receiver: Optional[str] = None
    session_id: Optional[str] = None
    action: str
    payload: Dict[str, Any]
    timestamp: str
    signature: Optional[str] = None
