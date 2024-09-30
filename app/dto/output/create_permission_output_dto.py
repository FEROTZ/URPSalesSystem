from pydantic import BaseModel, Field
from typing import Optional
from .permission_schema_output_dto import PermissionSchema

class CreatePermissionOutputSchema(BaseModel):
    success: bool = Field(..., description="Permission created successfully")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[PermissionSchema] = Field(None, description="Permission details of the permission")

    class Config:
        orm_mode = True
        extra = 'ignore'