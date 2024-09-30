from pydantic import BaseModel, Field
from typing import Optional
from .user_schema_output_dto import UserSchema

class CreateUserOutputSchema(BaseModel):
    success: bool = Field(..., description="User created successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[UserSchema] = Field(None, description="User details of user")

    class Config:
        orm_mode = True
        extra = 'ignore'
