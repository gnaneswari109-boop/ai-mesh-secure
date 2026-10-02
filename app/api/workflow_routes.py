from fastapi import APIRouter
import asyncio

from app.services.scheduler import add_task, ready_tasks, mark_task_done, list_tasks
from app.services.worker import execute_task
from app.services.aggregator import aggregate_results

router = APIRouter()


@router.post("/run")
async def run_workflow(name: str = "mesh-workflow"):
    from app.services.scheduler import TASK_GRAPH
    TASK_GRAPH.clear()

    add_task("research-1", "Research Market", "research")
    add_task("code-1", "Build MVP", "code")
    add_task("summary-1", "Write Final Summary", "summary", ["research-1", "code-1"])

    results = []
    while True:
        pending = ready_tasks()
        if not pending:
            break
        computed = await asyncio.gather(*(execute_task(task) for task in pending))
        for item in computed:
            mark_task_done(item["task_id"], item)
            results.append(item)

    return {
        "workflow_name": name,
        "results": results,
        "aggregated": aggregate_results(results),
    }


@router.get("/")
async def list_workflow_tasks():
    return {"tasks": list_tasks()}
