from typing import Dict, Optional, List

TASK_GRAPH: Dict[str, dict] = {}


def add_task(task_id: str, name: str, capability: str, dependencies: Optional[List[str]] = None):
    TASK_GRAPH[task_id] = {
        "task_id": task_id,
        "name": name,
        "capability": capability,
        "dependencies": dependencies or [],
        "status": "pending",
    }


def ready_tasks():
    return [
        task for task in TASK_GRAPH.values()
        if task["status"] == "pending"
        and all(TASK_GRAPH.get(dep, {}).get("status") == "completed" for dep in task["dependencies"])
    ]


def mark_task_done(task_id: str):
    if task_id in TASK_GRAPH:
        TASK_GRAPH[task_id]["status"] = "completed"
