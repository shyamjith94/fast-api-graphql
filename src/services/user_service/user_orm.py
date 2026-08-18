from src.repositories.user_repo.user import UserRepository
from src.models.user import User
from src.schema.user import UserCreateRequest, UserResponse, UserCreateRequestValidation
from fastapi.exceptions import HTTPException


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    async def create_user(self, user_data: UserCreateRequestValidation) -> UserResponse:
        return await self.user_repo.create(user_data)

    async def get_user(self, user_id: int) -> UserResponse:
        return await self.user_repo.get_by_id(user_id)

    async def update_user(self, user_id: int, user_data: UserCreateRequestValidation) -> UserResponse:
        return await self.user_repo.update(user_id, user_data)

    async def delete_user(self, user_id: int) -> bool:
        return await self.user_repo.delete(user_id)

    async def get_all_users(self) -> list[UserResponse]:
        return await self.user_repo.get_list()
        # raise HTTPException(status_code=404, detail="no data found")
