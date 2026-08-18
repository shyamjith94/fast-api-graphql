from sqlalchemy.exc import SQLAlchemyError
from fastapi import Request
from src.graphql.context.service_context import ApplicationContext
from src.repositories.user_repo.user import UserRepository
from src.services.user_service.user_orm import UserService
from src.core.database import get_db



async def get_context(request: Request):
    db_generator = get_db()
    db = await anext(db_generator)
    try:
        context =  ApplicationContext(
            db = db,
            user_service=UserService(UserRepository(db))
        )
        yield context
    except SQLAlchemyError:
        await db.rollback()
        raise
    finally:
        await db.close()