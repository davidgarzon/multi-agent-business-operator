"""Memory store interface and in-memory implementation."""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class MemoryStore(ABC):
    """Abstract memory store interface."""
    
    @abstractmethod
    async def store(self, key: str, value: Any, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Store a value in memory.
        
        Args:
            key: Storage key
            value: Value to store
            metadata: Optional metadata
        """
        pass
    
    @abstractmethod
    async def retrieve(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from memory.
        
        Args:
            key: Storage key
            
        Returns:
            Stored value if found, None otherwise
        """
        pass
    
    @abstractmethod
    async def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search memory by query.
        
        Args:
            query: Search query
            limit: Maximum results to return
            
        Returns:
            List of matching results
        """
        pass


class InMemoryStore(MemoryStore):
    """In-memory implementation of memory store."""
    
    def __init__(self) -> None:
        """Initialize in-memory store."""
        self._storage: Dict[str, Any] = {}
        self._metadata: Dict[str, Dict[str, Any]] = {}
    
    async def store(self, key: str, value: Any, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Store a value in memory."""
        self._storage[key] = value
        if metadata:
            self._metadata[key] = metadata
    
    async def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve a value from memory."""
        return self._storage.get(key)
    
    async def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search memory by query (placeholder implementation)."""
        # Placeholder: simple key-based search
        results = []
        query_lower = query.lower()
        
        for key, value in self._storage.items():
            if query_lower in key.lower():
                results.append({
                    "key": key,
                    "value": value,
                    "metadata": self._metadata.get(key, {}),
                })
                if len(results) >= limit:
                    break
        
        return results
