from pydantic import BaseModel, Field
from typing import Optional
from.user_schema_output_dto import UserSchema

class UpdateUserOutputSchema(BaseModel):
    success: bool = Field(..., description="User updated successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[UserSchema] = Field(None, description="Updated user details if updated successfully")

    class Config:
        orm_mode = True
        extra = 'ignore'