from app.api.routes import router
from app.api.websocket_routes import router as ws_router
from fastapi import FastAPI

app = FastAPI(title="AI Mesh Secure", version="1.0.0")
app.include_router(router, prefix="/api")
app.include_router(ws_router, prefix="/ws")

@app.get("/health")
async def health():
    return {"status": "ok"}
