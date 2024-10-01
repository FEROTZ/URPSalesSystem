from pydantic import BaseModel, Field
from typing import Optional
from .permission_schema_output_dto import PermissionSchema


class DeletePermissionOutputSchema(BaseModel):
    success: bool = Field(..., description="True if role deleted successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[PermissionSchema] = Field(None, description="Permission details if deleted successfully")

    class Config:
        orm_mode = True
        extra = 'ignore'