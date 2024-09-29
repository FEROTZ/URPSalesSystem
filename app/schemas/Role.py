# from pydantic import BaseModel, Field, field_validator
# from typing import Optional
# from datetime import datetime
# from enum import Enum


# class RoleStatusType(str, Enum):
#     active = 'active'
#     inactive = 'inactive'


# class RoleBase(BaseModel):
#     name: str = Field(..., min_length=3, max_length=50, example="Manager")
#     description: str | None = Field(None, max_length=100, example="Role for managing employees")


# class RoleCreate(RoleBase):
#     pass


# class RoleUpdate(BaseModel):
#     name: Optional[str] = Field(None, min_length=3, max_length=50)
#     description: Optional[str] = Field(None, max_length=100)

#     @field_validator('*')
#     def check_at_least_one_field(cls, values):
#         if not any(values.values()):
#             raise ValueError('At least one field must be provided')
#         return values

#     class Config:
#         orm_mode = True


# class RoleResponse(RoleBase):
#     id: int
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         orm_mode = True


# class RoleInactiveResponse(BaseModel):
#     id: int
#     status: RoleStatusType