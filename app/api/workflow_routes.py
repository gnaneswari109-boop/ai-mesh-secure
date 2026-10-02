from app.services.scheduler import add_task, ready_tasks, mark_task_done, list_tasks, TASK_GRAPH
from app.services.worker_llm import execute_task_with_llm
from app.services.aggregator import aggregate_results
from app.services.memory import update_memory
from fastapi import APIRouter
from pydantic import BaseModel
import asyncio

router = APIRouter()


class WorkflowRequest(BaseModel):
    name: str
    description: str | None = None


@router.post("/run")
async def run_workflow(payload: WorkflowRequest):
    """Execute a multi-agent workflow with LLM integration."""
    TASK_GRAPH.clear()

    add_task(
        "research-1",
        "Research AI market trends",
        "research",
        input_data={"topic": "AI adoption in 2024", "focus": "market size and growth"},
    )
    add_task(
        "code-1",
        "Implement REST API",
        "code",
        input_data={"features": ["authentication", "REST endpoints", "database"], "language": "Python"},
    )
    add_task(
        "summary-1",
        "Write executive summary",
        "summary",
        ["research-1", "code-1"],
        input_data={"audience": "stakeholders", "format": "executive brief"},
    )

    results = []
    iteration = 0
    
    while True:
        iteration += 1
        pending = ready_tasks()
        if not pending:
            break
        
        print(f"[Iteration {iteration}] Executing {len(pending)} task(s)")
        computed = await asyncio.gather(*(execute_task_with_llm(task) for task in pending))
        
        for item in computed:
            mark_task_done(item["task_id"], item)
            results.append(item)
            update_memory(item["task_id"], "result", item, "orchestrator")

    return {
        "workflow_name": payload.name,
        "description": payload.description,
        "results": results,
        "aggregated": aggregate_results(results),
    }


@router.get("/")
async def list_workflow_tasks():
    """List all tasks in the current workflow."""
    return {"tasks": list_tasks()}
