from src.validations.base import BaseValidation
from src.schema.user import UserCreateRequest, UserCreateRequestValidation
from pydantic import ValidationError
from dataclasses import asdict


class UserValidator(BaseValidation[UserCreateRequestValidation]):

    @classmethod
    def validate(cls, data: UserCreateRequest) -> UserCreateRequestValidation:
        validated = UserCreateRequestValidation(**asdict(data))
        return validated
