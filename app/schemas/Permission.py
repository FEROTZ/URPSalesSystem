from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class PermissionStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'
    
    
class PermissionBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, example="restore_user")
    description: str | None = Field(None, max_length=100, example="This permission allows restore an user")
    
    @field_validator('name')
    def normalize_name(cls, v: str):
        return v.lower()
    
    @field_validator('description')
    def normalize_description(cls, v: str):
        return v.lower() if v else None


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(PermissionBase):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=100)

    class Config:
        orm_mode = True


class PermissionResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PermissionInactiveResponse(BaseModel):
    id: int
    status: PermissionStatusType