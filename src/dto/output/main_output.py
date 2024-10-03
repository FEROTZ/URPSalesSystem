from pydantic import BaseModel, Field
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class MainSchema(BaseModel):
    status: str = Field(description="Status project")
    message: str = Field(description="Message to project", default=1)
    version: int = Field(description="Version to project", default=getenv("VERSION"))


class MainOutput:
    def create(response: MainSchema):
        return MainSchema(status=response["status"], message=response["message"])