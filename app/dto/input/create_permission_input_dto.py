from pydantic import BaseModel, Field
from typing import Optional


class CreatePermissionInputSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=5, max_length=100)