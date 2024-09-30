from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from .role_schema_output_dto import RoleSchema


class GetRoleOutputSchema(BaseModel):
    success: bool = Field(..., description = "True if action was successful")
    message: str = Field(..., description = "Message describing the outcome of the action")
    payload: Optional[RoleSchema] = Field(None, description = "Role data")

    model_config = ConfigDict(from_attributes = True)