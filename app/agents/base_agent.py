"""Abstract base agent class."""
from abc import ABC, abstractmethod
from typing import Any, Dict

from app.models.result import ExecutionResult
from app.models.task import Task


class BaseAgent(ABC):
    """Abstract base class for all agents."""
    
    def __init__(self, name: str) -> None:
        """Initialize agent with a name."""
        self.name = name
    
    @abstractmethod
    async def execute(self, task: Task) -> ExecutionResult:
        """
        Execute a task.
        
        Args:
            task: Task to execute
            
        Returns:
            ExecutionResult with execution details
        """
        pass
    
    @abstractmethod
    def can_handle(self, task: Task) -> bool:
        """
        Check if this agent can handle the given task.
        
        Args:
            task: Task to check
            
        Returns:
            True if agent can handle the task
        """
        pass
    
    def get_capabilities(self) -> Dict[str, Any]:
        """
        Get agent capabilities.
        
        Returns:
            Dictionary with agent capabilities
        """
        return {
            "name": self.name,
            "type": self.__class__.__name__,
        }
