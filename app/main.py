"""FastAPI application entry point."""
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.api.routes import router as tasks_router
from app.config import settings
from app.orchestrator.orchestrator import Orchestrator
from app.registry.agent_registry import AgentRegistry
from app.agents.marketing_agent import MarketingAgent
from app.agents.sales_agent import SalesAgent
from app.agents.ops_agent import OperationsAgent


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan manager.
    Initializes and cleans up resources.
    """
    # Startup: Initialize agent registry and orchestrator
    registry = AgentRegistry()
    registry.register(MarketingAgent())
    registry.register(SalesAgent())
    registry.register(OperationsAgent())
    
    orchestrator = Orchestrator(registry)
    
    # Store in app state for dependency injection
    app.state.registry = registry
    app.state.orchestrator = orchestrator
    
    yield
    
    # Shutdown: Cleanup if needed
    pass


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)

# Include router
app.include_router(tasks_router)
