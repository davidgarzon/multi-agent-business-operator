"""Task model and enums.

Backward-compatible schema that accepts:
- Old: {type: marketing|sales|operations, description, metadata}
- New: {type: MARKETING_PLAN|CREATE_CONTENT|QUALIFY_LEAD|OPS_AUTOMATION, goal, context, constraints}

This model keeps internal canonical TaskType values (marketing/sales/operations)
while accepting richer task types and field aliases.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


class TaskType(str, Enum):
    MARKETING = "marketing"
    SALES = "sales"
    OPERATIONS = "operations"


class Task(BaseModel):
    """A unit of work executed by the orchestrator."""

    id: str | None = Field(default=None, description="Task identifier")

    # Canonical internal types
    type: TaskType = Field(..., description="Task type")

    # Canonical field names (backward compatible)
    description: str = Field(..., description="Task description / goal")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Task metadata / context"
    )

    # New optional field
    constraints: dict[str, Any] = Field(
        default_factory=dict, description="Constraints / guardrails"
    )

    priority: int = Field(default=3, ge=1, le=5, description="Priority 1..5")

    @model_validator(mode="before")
    @classmethod
    def normalize_input(cls, data: Any) -> Any:
        """Accept new field names while keeping backward-compatible schema."""
        if not isinstance(data, dict):
            return data

        # goal -> description
        if "description" not in data and "goal" in data:
            data["description"] = data["goal"]

        # context -> metadata
        if "metadata" not in data and "context" in data:
            data["metadata"] = data["context"]

        return data

    @field_validator("type", mode="before")
    @classmethod
    def coerce_rich_task_types(cls, v: Any) -> Any:
        """Map rich task types to canonical categories for v1."""
        if isinstance(v, str):
            mapping = {
                "MARKETING_PLAN": "marketing",
                "CREATE_CONTENT": "marketing",
                "QUALIFY_LEAD": "sales",
                "OPS_AUTOMATION": "operations",
            }
            return mapping.get(v, v)
        return v

    model_config = {"use_enum_values": True}