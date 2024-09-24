from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime
from enum import Enum

class UserStatusType(str, Enum):
    active = 'active'
    inactive = 'inactive'


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    
    @field_validator('email')
    def normalize_email(cls, v: EmailStr):
        return v.lower()


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)
    
    class Config:
        orm_mode = True

        
class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8, max_length=100)

    class Config:
        orm_mode = True


class UserInactiveResponse(BaseModel):
    id: int
    status: UserStatusType


class UserResponse(UserBase):
    id: int
    role_name: str
    status: UserStatusType
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(...)


class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    username: str | None = None