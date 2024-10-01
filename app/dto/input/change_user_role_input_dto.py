from pydantic import BaseModel, Field


class ChangeUserRoleInputSchema(BaseModel):
    role_id: int = Field(..., description = "Role ID to assign to the user")

    class Config:
        orm_mode = True
        extra = 'ignore'