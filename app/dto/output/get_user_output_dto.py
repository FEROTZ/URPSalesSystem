from pydantic import BaseModel, Field, ValidationError


class getUserOutputSchema(BaseModel):
    success: bool = Field(..., description="True if action was successful")
    message: str = Field(..., description="Message describing the outcome of the action")
    payload: dict = Field(...)


class getUserOutput:
    def create(body: getUserOutputSchema):
        try:
            return getUserOutputSchema().load(body)
        except ValidationError as error:
            raise Exception(error)