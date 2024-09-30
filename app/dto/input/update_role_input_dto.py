from pydantic import BaseModel, Field
from typing import Optional


class UpdateRoleInputSchema(BaseModel):
    name: Optional[str] = Field(None, description="Role name")
    description: Optional[str] = Field(None, description="Role description")

    class Config:
        orm_mode = True