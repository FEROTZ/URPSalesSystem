from pydantic import BaseModel, Field, EmailStr, ConfigDict
from enum import Enum
from datetime import datetime

class UserStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'

class UserSchema(BaseModel):
    id: int = Field(..., description="Id of the user")
    email: EmailStr = Field(..., description="Email of the user")
    status: UserStatusType = Field(..., description="Status of the user")
    updated_at: datetime = Field(..., description="Timestamp of the last update")

    model_config = ConfigDict(from_attributes=True, extra='ignore')