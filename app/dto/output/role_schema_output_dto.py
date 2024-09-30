from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime

class RoleStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'

class RoleSchema(BaseModel):
    id: int = Field(..., description="Id of the role")
    name: str = Field(..., description="Name of the role")
    status:RoleStatusType = Field(..., description="Status of the role created")
    created_at: Optional[datetime] = Field(None, description="Timestamp of the creation of the role")
    updated_at: Optional[datetime] = Field(None, description="Timestamp of the last update of the role")

    model_config = ConfigDict(from_attributes = True, extra = 'ignore')