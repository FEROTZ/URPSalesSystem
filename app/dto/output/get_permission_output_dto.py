from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from .permission_schema_output_dto import PermissionSchema


class GetPermissionOutputSchema(BaseModel):
    success: bool = Field(..., description="True if the operation was successful")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[PermissionSchema] = Field(None, description="Permission details")

    model_config = ConfigDict(from_attributes=True)