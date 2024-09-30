from pydantic import BaseModel, Field
from typing import Optional
from .user_schema_output_dto import UserSchema

class DeleteUserOutputSchema(BaseModel):
    success: bool = Field(..., description="True if user deleted successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[UserSchema] = Field(None, description="User details if deleted successfully")

    class Config:
        orm_mode = True
        extra = 'ignore'