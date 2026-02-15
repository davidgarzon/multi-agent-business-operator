"""Agent registry implementation."""
from typing import Dict, List, Optional

from app.agents.base_agent import BaseAgent
from app.models.task import Task


class AgentRegistry:
    """Registry for managing available agents."""
    
    def __init__(self) -> None:
        """Initialize empty registry."""
        self._agents: Dict[str, BaseAgent] = {}
    
    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent.
        
        Args:
            agent: Agent to register
        """
        self._agents[agent.name] = agent
    
    def get_agent(self, name: str) -> Optional[BaseAgent]:
        """
        Get agent by name.
        
        Args:
            name: Agent name
            
        Returns:
            Agent if found, None otherwise
        """
        return self._agents.get(name)
    
    def find_agent_for_task(self, task: Task) -> Optional[BaseAgent]:
        """
        Find agent that can handle the given task.
        
        Args:
            task: Task to find agent for
            
        Returns:
            Agent if found, None otherwise
        """
        for agent in self._agents.values():
            if agent.can_handle(task):
                return agent
        return None
    
    def list_agents(self) -> List[BaseAgent]:
        """
        List all registered agents.
        
        Returns:
            List of all registered agents
        """
        return list(self._agents.values())
    
    def get_agent_names(self) -> List[str]:
        """
        Get list of registered agent names.
        
        Returns:
            List of agent names
        """
        return list(self._agents.keys())
