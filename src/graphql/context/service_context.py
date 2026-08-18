from dataclasses import dataclass
from strawberry.fastapi import BaseContext
from src.services.user_service.user_orm import UserService
from sqlalchemy.ext.asyncio import AsyncSession

@dataclass
class ApplicationContext(BaseContext):
    db: AsyncSession
    user_service: UserService

