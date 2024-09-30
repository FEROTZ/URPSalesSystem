from pydantic import BaseModel, Field
from typing import Optional
from .role_schema_output_dto import RoleSchema


class CreateRoleOutputSchema(BaseModel):
    success: bool = Field(..., description="Role created successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[RoleSchema] = Field(None, description="Role details of the rol")

    class Config:
        orm_mode = True
        extra = 'ignore'