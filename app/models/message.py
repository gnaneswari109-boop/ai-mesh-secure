from pydantic import BaseModel
from typing import Optional, Dict, Any


class MessageEnvelope(BaseModel):
    message_id: str
    sender: str
    receiver: Optional[str] = None
    session_id: Optional[str] = None
    action: str
    payload: Dict[str, Any]
    timestamp: str
    signature: Optional[str] = None
