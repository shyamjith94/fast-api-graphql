from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.graphql.context import get_context
from src.graphql.schema import schema
from strawberry.fastapi import GraphQLRouter
from src.core.lifespan import db_lifespan
from src.core.settings import settings
from src.core.lifespan import run_async_migrations
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await asyncio.gather(
            db_lifespan(),
            run_async_migrations(),
        )
        yield
    except Exception:
        raise
        
    
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    lifespan=lifespan
)



graphql_router = GraphQLRouter(
    schema,
    context_getter=get_context,
    graphql_ide="graphiql"
)

app.include_router(graphql_router, prefix="/graphql")


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)
