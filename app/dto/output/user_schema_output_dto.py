from pydantic import BaseModel, Field, EmailStr, ConfigDict
from enum import Enum
from typing import Optional
from datetime import datetime

class UserStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'

class UserSchema(BaseModel):
    id: int = Field(..., description="Id of the user")
    email: EmailStr = Field(..., description="Email of the user")
    role_name: Optional[str] = Field(None, description="Name of the user's role")
    status: UserStatusType = Field(..., description="Status of the user")
    updated_at: datetime = Field(..., description="Timestamp of the last update")

    model_config = ConfigDict(from_attributes=True, extra='ignore')