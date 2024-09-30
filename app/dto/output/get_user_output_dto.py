from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from .user_schema_output_dto import UserSchema


class GetUserOutputSchema(BaseModel):
    success: bool = Field(..., description="True if action was successful")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[UserSchema] = Field(None, description="User data")

    model_config = ConfigDict(from_attributes=True)
