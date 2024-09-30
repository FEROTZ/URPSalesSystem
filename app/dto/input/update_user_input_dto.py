from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UpdateUserInputSchema(BaseModel):
    username : Optional[str] = Field(None, min_length=3, max_length=20)
    email : Optional[EmailStr] = None
    password : Optional[str] = Field(None, min_length=8, max_length=100)

    class Config:
        orm_mode = True