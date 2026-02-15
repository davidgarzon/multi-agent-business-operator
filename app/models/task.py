"""Task model and enums."""
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class TaskType(str, Enum):
    """Task type enumeration."""
    
    MARKETING = "marketing"
    SALES = "sales"
    OPERATIONS = "operations"


class Task(BaseModel):
    """Task model."""
    
    id: Optional[str] = Field(default=None, description="Task identifier")
    type: TaskType = Field(..., description="Task type")
    description: str = Field(..., description="Task description")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional task metadata")
    
    class Config:
        use_enum_values = True
