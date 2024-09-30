from pydantic import BaseModel, Field
from typing import Optional
from .role_schema_output_dto import RoleSchema


class UpdateRoleOutputSchema(BaseModel):
    success: bool = Field(..., description="Role updated successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[RoleSchema] = Field(None, description="Updated role details if updated successfully")

    class Config:
        orm_mode = True
        extra = 'ignore'