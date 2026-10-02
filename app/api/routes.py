from fastapi import APIRouter
from app.api.agent_routes import router as agent_router
from app.api.session_routes import router as session_router
from app.api.workflow_routes import router as workflow_router
from app.api.health_routes import router as health_router

router = APIRouter()

router.include_router(agent_router, prefix="/agents")
router.include_router(session_router, prefix="/sessions")
router.include_router(workflow_router, prefix="/workflow")
router.include_router(health_router, prefix="/health")
