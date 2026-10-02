from typing import Dict, Any
from datetime import datetime

MEMORY: Dict[str, Dict[str, Any]] = {}


def get_memory(task_id: str):
    if task_id not in MEMORY:
        MEMORY[task_id] = {"version": 0, "data": {}}
    return MEMORY[task_id]


def update_memory(task_id: str, key: str, value: Any, actor: str):
    memory = get_memory(task_id)
    memory["data"][key] = value
    memory["version"] += 1
    memory["updated_by"] = actor
    memory["updated_at"] = datetime.utcnow().isoformat()
    return memory
