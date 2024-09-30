from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from datetime import datetime
from typing import Optional

class PermissionStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'

class PermissionSchema(BaseModel):
    id: int = Field(..., description="Id of the permission")
    name: str = Field(..., description="Name of the permission")
    description: Optional[str] = Field(None, description="Description of the permission")
    status: PermissionStatusType = Field(..., description="Status of the permission")
    updated_at: datetime = Field(..., description="Timestamp of the last update of the permission")

    model_config = ConfigDict(from_attributes = True, extra = 'ignore')