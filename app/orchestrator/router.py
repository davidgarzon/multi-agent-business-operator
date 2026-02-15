"""Task router implementation."""
from typing import Optional

from app.agents.base_agent import BaseAgent
from app.models.task import Task
from app.registry.agent_registry import AgentRegistry


class TaskRouter:
    """Routes tasks to appropriate agents."""
    
    def __init__(self, registry: AgentRegistry) -> None:
        """
        Initialize router with agent registry.
        
        Args:
            registry: Agent registry instance
        """
        self.registry = registry
    
    def route(self, task: Task) -> Optional[BaseAgent]:
        """
        Route task to appropriate agent.
        
        Args:
            task: Task to route
            
        Returns:
            Agent if found, None otherwise
        """
        return self.registry.find_agent_for_task(task)
