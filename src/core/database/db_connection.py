from collections.abc import AsyncGenerator
from src.core.settings import settings
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (AsyncSession, create_async_engine, async_sessionmaker)

engine = create_async_engine(
    settings.database_url,
    pool_size=20,
    max_overflow=100,
    pool_pre_ping=True,
    echo=True
    )
session_local = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
    )

async def get_db()->AsyncGenerator[AsyncSession,None]:
    """
    Generate an async database session.
    This function is used as a FastAPI dependency.
    """
    
    async with session_local() as db_session:
        try:
            yield db_session
        except SQLAlchemyError:
            await db_session.rollback()
            raise
        finally:
            await db_session.close()
