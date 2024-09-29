from pydantic import BaseModel, Field, ValidationError, EmailStr, field_validator


class createUserInputSchema(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=8, max_length=100)


class createUserInput:
    def create(body: createUserInputSchema):
        try:
            return createUserInputSchema.load(body)
        except ValidationError as error:
            raise Exception(error)