from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from .permission_schema_output_dto import PermissionSchema

class GetAllPermissionsOutputSchema(BaseModel):
    success: bool = Field(..., description="True if action was successful")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: Optional[List[PermissionSchema]] = Field(None, description="Permissions data")

    model_config = ConfigDict(from_attributes = True)