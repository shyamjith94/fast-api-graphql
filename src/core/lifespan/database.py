from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from src.core.database import get_db


async def db_lifespan()->None:
    try:
        db_generator = get_db()
        db = await anext(db_generator)
        try:
            await db.execute(text("SELECT 1"))
            print(f"{'*' * 10} db connection success {'*' * 10}")
        finally:
            await db.close()
        
    except SQLAlchemyError as exe:
        print(f"db connection error : {exe}")
        raise
        