"""Execution result model and enums."""
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ExecutionStatus(str, Enum):
    """Execution status enumeration."""
    
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"


class Step(BaseModel):
    """Execution step model."""
    
    name: str = Field(..., description="Step name")
    status: ExecutionStatus = Field(..., description="Step status")
    output: Optional[Dict[str, Any]] = Field(default=None, description="Step output")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    
    class Config:
        use_enum_values = True


class ExecutionResult(BaseModel):
    """Execution result model."""
    
    task_id: str = Field(..., description="Task identifier")
    status: ExecutionStatus = Field(..., description="Overall execution status")
    selected_agent: str = Field(..., description="Selected agent name")
    steps: List[Step] = Field(default_factory=list, description="Execution steps")
    output: Optional[Dict[str, Any]] = Field(default=None, description="Final output")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    
    class Config:
        use_enum_values = True
