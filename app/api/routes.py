from fastapi import APIRouter
from pydantic import BaseModel

from app.services.registry import register_agent, find_agents_by_capability
from app.services.pairing import create_pairing, approve_pairing
from app.services.scheduler import add_task, ready_tasks, mark_task_done, TASK_GRAPH
from app.services.worker import execute_task

router = APIRouter()


class AgentRequest(BaseModel):
    agent_id: str
    capabilities: list[str]


class PairRequest(BaseModel):
    agent_a: str
    agent_b: str


class PairApproveRequest(BaseModel):
    session_id: str


class WorkflowRequest(BaseModel):
    name: str


@router.post("/register")
async def register_agent_api(payload: AgentRequest):
    return {"status": "registered", "agent": register_agent(payload.agent_id, payload.capabilities)}


@router.get("/agents")
async def list_agents():
    return {"agents": list(find_agents_by_capability("research") + find_agents_by_capability("code") + find_agents_by_capability("summary"))}


@router.get("/agents/capabilities/{capability}")
async def agents_by_capability(capability: str):
    return {"matches": find_agents_by_capability(capability)}


@router.post("/sessions/pair")
async def pair_agents(payload: PairRequest):
    return {"status": "pairing_started", "pairing": create_pairing(payload.agent_a, payload.agent_b)}


@router.post("/sessions/approve")
async def approve_agents(payload: PairApproveRequest):
    return {"status": "approved", "pairing": approve_pairing(payload.session_id)}


@router.post("/workflow/run")
async def run_workflow(payload: WorkflowRequest):
    TASK_GRAPH.clear()
    add_task("research-1", "Research Market", "research")
    add_task("code-1", "Build MVP", "code")
    add_task("summary-1", "Final Summary", "summary", ["research-1", "code-1"])

    results = []
    while True:
        pending = ready_tasks()
        if not pending:
            break

        computed = await asyncio.gather(*(execute_task(task) for task in pending))
        for item in computed:
            mark_task_done(item["task_id"])
            results.append(item)

    return {"workflow": payload.name, "results": results}
