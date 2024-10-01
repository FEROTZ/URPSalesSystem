from pydantic import BaseModel, Field
from typing import Optional
from .permission_schema_output_dto import PermissionSchema


class UpdatePermissionOutputSchema(BaseModel):
    success: bool = Field(..., description="Permission updated successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[PermissionSchema] = Field(None, description="Updated permission details if updated successfully")

    class Config:
        orm_mode = True
        extra = 'ignore'