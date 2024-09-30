from pydantic import BaseModel, Field
from typing import Optional
from .role_schema_output_dto import RoleSchema

class DeleteRoleOutputSchema(BaseModel):
    success: bool = Field(..., description="True if role deleted successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[RoleSchema] = Field(None, description="Role details if deleted successfully")

    class Config:
        orm_mode = True
        extra = 'ignore'