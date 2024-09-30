from pydantic import BaseModel, Field, field_validator
from typing import Optional

class CreateRoleInputSchema(BaseModel):
    name: str = Field(..., min_length=5, max_length=50, example="Manager")
    description: Optional[str] = Field(None, min_length=5, max_length=100, example="Role for managing employees")

    @field_validator('name')
    def normalize_name(cls, v:str):
        return v.lower()