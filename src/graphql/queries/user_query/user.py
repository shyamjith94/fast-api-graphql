
import strawberry
from src.schema.user import UserResponse
from src.models.user import User
from src.services.user_service.user_orm import UserService


@strawberry.type
class UserQuery:

    @strawberry.field
    async def get_users(self, info: strawberry.Info) -> list[UserResponse]:
        user_service: UserService = info.context.user_service
        return await user_service.get_all_users()
    
    @strawberry.field
    async def get_user(self,info:strawberry.Info,id:int)->UserResponse:
        user_service:UserService = info.context.user_service
        return await user_service.get_user(id)
