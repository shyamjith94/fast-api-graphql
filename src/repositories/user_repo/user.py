from src.models.user import User
from src.schema.user import UserCreateRequest, UserResponse, UserCreateRequestValidation
from random import randint
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import exists, select, delete, update
from fastapi.exceptions import HTTPException

class UserRepository:
    def __init__(self, db:AsyncSession):
        self.db = db
    async def user_exists_by_email(self,email:str) -> bool:
        result=await self.db.execute(
            select(exists().where(User.email == email))
            )
        return result.scalar_one()
    
    async def user_exists_by_id(self,id:int) -> bool:
        result=await self.db.execute(
            select(exists().where(User.id == id))
            )
        return result.scalar_one()
        
    async def create(self, user: UserCreateRequestValidation) -> UserResponse:
        if await self.user_exists_by_email(user.email):
            raise HTTPException(status_code=400, detail="User already exists")
        user_model = User(**user.model_dump())
        self.db.add(user_model)
        await self.db.commit()
        await self.db.refresh(user_model)
        data = UserCreateRequestValidation.model_validate(user_model).model_dump()
        return UserResponse(**data)
    async def get_by_id(self, id: int) -> UserResponse:
        user = await self.db.execute(
            select(User).where(User.id == id)
        )
        user = user.scalar_one_or_none()
        if  user is None:
            raise HTTPException(status_code=404, detail="User not found")
        user_data =  UserCreateRequestValidation.model_validate(
            user
            ).model_dump()
        return UserResponse(**user_data)

    async def update(self, id: int, user: UserCreateRequestValidation) -> UserResponse:
        if not await self.user_exists_by_id(id):
            raise HTTPException(status_code=404, detail="User not found")
        await self.db.execute(update(User).where(User.id == id).values(**user.model_dump()))
        await self.db.commit()
        return await self.get_by_id(id)
    async def delete(self, id: int) -> bool:
        if not await self.user_exists_by_id(id):
            raise HTTPException(status_code=404, detail="User not found")
        await self.db.execute(delete(User).where(User.id == id))
        await self.db.commit()
        return True
    async def get_list(self) -> list[UserResponse]:
        users = await self.db.execute(select(User))
        return [UserResponse(**UserCreateRequestValidation.model_validate(user).model_dump()) for user in users.scalars().all()]