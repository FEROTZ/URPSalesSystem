from pydantic import BaseModel, Field
from typing import Optional


class UpdateRoleInputSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=50, description="Role name")
    description: Optional[str] = Field(None, min_length=5, max_length=100,  description="Role description")

    class Config:
        orm_mode = True