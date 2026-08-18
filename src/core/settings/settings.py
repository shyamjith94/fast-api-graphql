from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field,AliasChoices, model_validator


class Settings(BaseSettings):

    app_name : str = "GraphQL API"
    app_version:str = "v1"
    app_description: str = "GraphQL API"

    db_user : str = Field(default="postgres", validation_alias=AliasChoices("DB_USER", "db_user"))
    db_password : str = Field(default="postgres", validation_alias=AliasChoices("DB_PASSWORD", "db_password"))
    db_host : str = Field(default="localhost", validation_alias=AliasChoices("DB_HOST", "db_host"))
    db_port : int = Field(default=5432, validation_alias=AliasChoices("DB_PORT", "db_port"))
    db_name : str = Field(default="graphql", validation_alias=AliasChoices("DB_NAME", "db_name"))
    database_url:str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/graphql",
        validation_alias=AliasChoices("DATABASE_URL", "database_url")
    )
    @model_validator(mode="after")
    def construct_db_url(self):
        if not self.database_url:
            self.database_url = (
                f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            )
        return self


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )



settings = Settings()