import asyncio
from alembic.config import command, Config


def run_migrations()->None:
    config = Config("alembic.ini")
    command.upgrade(
        config,
        "head"
    )


async def run_async_migrations()->None:
    await asyncio.to_thread(run_migrations)