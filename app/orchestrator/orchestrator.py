"""Orchestrator implementation."""
from typing import Optional

from app.agents.base_agent import BaseAgent
from app.models.result import ExecutionResult, ExecutionStatus
from app.models.task import Task
from app.orchestrator.router import TaskRouter
from app.registry.agent_registry import AgentRegistry


class Orchestrator:
    """Orchestrates task execution by routing to appropriate agents."""
    
    def __init__(self, registry: AgentRegistry) -> None:
        """
        Initialize orchestrator with agent registry.
        
        Args:
            registry: Agent registry instance
        """
        self.registry = registry
        self.router = TaskRouter(registry)
    
    async def execute_task(self, task: Task) -> ExecutionResult:
        """
        Execute a task by routing to appropriate agent.
        
        Args:
            task: Task to execute
            
        Returns:
            ExecutionResult with execution details
        """
        agent = self.router.route(task)
        
        if agent is None:
            return ExecutionResult(
                task_id=task.id or "unknown",
                status=ExecutionStatus.FAILED,
                selected_agent="none",
                steps=[],
                error=f"No agent found for task type: {task.type}",
            )
        
        return await agent.execute(task)
