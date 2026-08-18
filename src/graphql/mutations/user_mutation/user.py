import strawberry
from pydantic import ValidationError
from fastapi.exceptions import HTTPException
from src.schema.user import UserCreateRequest, UserResponse, UserCreateRequestValidation
from src.models.user import User
from src.validations.user.validation import UserValidator
from src.services.user_service.user_orm import UserService


@strawberry.type
class UserMutation:

    @strawberry.mutation
    async def create_user(self,
                    info: strawberry.Info,
                    user: UserCreateRequest,
                    ) -> UserResponse | None:
        try:
            user_service: UserService = info.context.user_service
            validated_data: UserCreateRequestValidation = UserValidator.validate(
                user)
            user_response = await user_service.create_user(validated_data)

            return user_response
        except (ValueError, ValidationError) as e:
            raise HTTPException(status_code=400, detail=str(e))

    @strawberry.mutation
    async def update_user(self, info: strawberry.Info, user_id: int, user: UserCreateRequest) -> UserResponse:
        try:
            validated_data: UserCreateRequestValidation = UserValidator.validate(user)
        except (ValueError, ValidationError) as e:
            raise HTTPException(status_code=400, detail=str(e))
        user_service: UserService = info.context.user_service
        user_response = await user_service.update_user(user_id, validated_data)
        return user_response

    @strawberry.mutation
    async def delete_user(self, info: strawberry.Info, user_id: int) -> bool:
        user_service: UserService = info.context.user_service
        user_response = await user_service.delete_user(user_id)
        return user_response
