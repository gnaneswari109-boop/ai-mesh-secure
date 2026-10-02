from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class TaskSchema(BaseModel):
    task_id: str
    name: str
    capability: str
    dependencies: List[str] = []
    status: str = "pending"
    assigned_to: Optional[str] = None
    result: Optional[Dict[str, Any]] = None


class WorkflowRequest(BaseModel):
    name: str
    description: Optional[str] = None
