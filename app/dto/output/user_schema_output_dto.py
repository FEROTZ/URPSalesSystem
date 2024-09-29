from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class UserStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'

class UserSchema(BaseModel):
    id: int = Field(..., description="Id of the user")
    username: str = Field(..., description="Username of the user")
    email: EmailStr = Field(..., description="Email of the user")
    status: UserStatusType = Field(..., description="Status of the user")