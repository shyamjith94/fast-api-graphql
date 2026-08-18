from src.schema.base import RequestBaseModel
import strawberry
from datetime import datetime
from src.schema.base import BaseRequestSchema, BaseResponseSchema
from pydantic import field_validator, ConfigDict
from pydantic import Field, EmailStr
import re


@strawberry.input
class UserCreateRequest(BaseRequestSchema):
    name: str
    email: str


@strawberry.type
class UserResponse(BaseResponseSchema):
    name: str
    email: str


class UserCreateRequestValidation(RequestBaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name: str = Field(min_length=3)
    email: EmailStr = Field()

    # validate the name
    @field_validator("name")
    @classmethod
    def validate_name(cls, name: str) -> str:
        value = name.strip()
        if not value or not re.fullmatch(r"[^0-9]+", value):
            raise ValueError(
                "Name is required or name does not match as the requirement ")
        return value
