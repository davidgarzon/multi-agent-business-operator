"""Base tool interface."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """Abstract base class for all tools."""
    
    def __init__(self, name: str, description: str) -> None:
        """
        Initialize tool with name and description.
        
        Args:
            name: Tool name
            description: Tool description
        """
        self.name = name
        self.description = description
    
    @abstractmethod
    async def execute(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Execute the tool.
        
        Args:
            **kwargs: Tool-specific parameters
            
        Returns:
            Dictionary with execution results
        """
        pass
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get tool schema for validation.
        
        Returns:
            Dictionary with tool schema
        """
        return {
            "name": self.name,
            "description": self.description,
        }
