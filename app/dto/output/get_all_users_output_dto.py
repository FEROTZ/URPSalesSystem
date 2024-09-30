from pydantic import Field, ConfigDict, BaseModel
from .get_user_output_dto import UserSchema
from typing import List
from typing import Optional

class GetAllUsersOutputSchema(BaseModel):
    success: bool = Field(..., description="True if action was successful")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[List[UserSchema]] = Field(None, description="Users data")

    model_config = ConfigDict(from_attributes=True)