from app.services.scheduler import add_task as scheduler_add_task
from typing import Optional, List


def add_task(
    task_id: str,
    name: str,
    capability: str,
    dependencies: Optional[List[str]] = None,
    input_data: Optional[dict] = None,
):
    """Add a task with input data support."""
    from app.services.scheduler import TASK_GRAPH
    
    TASK_GRAPH[task_id] = {
        "task_id": task_id,
        "name": name,
        "capability": capability,
        "dependencies": dependencies or [],
        "status": "pending",
        "result": None,
        "input_data": input_data or {},
    }
