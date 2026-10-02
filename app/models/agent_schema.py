from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class AgentSchema(BaseModel):
    agent_id: str
    capabilities: List[str]
    metadata: Dict[str, Any] = {}


class RegisterAgentRequest(BaseModel):
    agent_id: str
    capabilities: List[str]
    public_key: Optional[str] = None
