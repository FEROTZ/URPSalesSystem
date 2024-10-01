from pydantic import BaseModel, Field
from typing import Optional


class UpdatePermissionInputSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=50, description="Permission name")
    description: Optional[str] = Field(None, min_length=5, max_length=100, description="Permission description")

    class Config:
        orm_mode = True