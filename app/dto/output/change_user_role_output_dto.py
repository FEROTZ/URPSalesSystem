from pydantic import BaseModel, Field, ConfigDict
from .user_schema_output_dto import UserSchema
from typing import Optional


class ChangeUserRoleOutputSchema(BaseModel):
    success: bool = Field(..., description="Role assignment changed successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[UserSchema] = Field(None, description="Updated role assignment if changed successfully")

    model_config = ConfigDict(from_attributes=True)