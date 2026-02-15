"""API routes."""
from fastapi import APIRouter, Depends, HTTPException, Request

from app.models.result import ExecutionResult
from app.models.task import Task
from app.orchestrator.orchestrator import Orchestrator

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_orchestrator(request: Request) -> Orchestrator:
    """Dependency to get orchestrator from app state."""
    return request.app.state.orchestrator


@router.post("/execute", response_model=ExecutionResult)
async def execute_task(
    task: Task,
    orchestrator: Orchestrator = Depends(get_orchestrator),
) -> ExecutionResult:
    """
    Execute a task.
    
    Args:
        task: Task to execute
        orchestrator: Orchestrator instance (dependency injection)
        
    Returns:
        ExecutionResult with execution details
        
    Raises:
        HTTPException: If execution fails
    """
    try:
        result = await orchestrator.execute_task(task)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Task execution failed: {str(e)}")
