from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from .role_schema_output_dto import RoleSchema

class GetAllRolesOutputSchema(BaseModel):
    success: bool = Field(..., description="True if action was successful")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[List[RoleSchema]] = Field(..., description="Users data")

    model_config = ConfigDict(from_attributes = True)