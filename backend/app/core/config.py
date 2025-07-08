"""
Application configuration settings.
"""

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Project info
    PROJECT_NAME: str = "Telegram Manager Backend"
    VERSION: str = "0.1.0"
    DEBUG: bool = Field(default=False, validation_alias=AliasChoices("DEBUG"))

    # Server settings
    HOST: str = Field(default="0.0.0.0", validation_alias=AliasChoices("HOST"))
    PORT: int = Field(default=8000, validation_alias=AliasChoices("PORT"))

    # CORS settings
    ALLOWED_HOSTS: list[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        validation_alias=AliasChoices("ALLOWED_HOSTS"),
    )

    # Database settings
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:password@localhost:5432/telegram_manager",
        validation_alias=AliasChoices("DATABASE_URL"),
    )

    # Test database settings
    TEST_DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:password@localhost:5432/telegram_manager_test",
        validation_alias=AliasChoices("TEST_DATABASE_URL"),
    )

    # AWS settings
    AWS_ACCESS_KEY_ID: str = Field(
        default="", validation_alias=AliasChoices("AWS_ACCESS_KEY_ID")
    )
    AWS_SECRET_ACCESS_KEY: str = Field(
        default="", validation_alias=AliasChoices("AWS_SECRET_ACCESS_KEY")
    )
    AWS_REGION: str = Field(
        default="us-east-1", validation_alias=AliasChoices("AWS_REGION")
    )
    AWS_S3_BUCKET: str = Field(
        default="", validation_alias=AliasChoices("AWS_S3_BUCKET")
    )

    # Redis settings (for ARQ)
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0", validation_alias=AliasChoices("REDIS_URL")
    )

    # Telegram settings
    TELEGRAM_BOT_TOKEN: str = Field(
        default="", validation_alias=AliasChoices("TELEGRAM_BOT_TOKEN")
    )

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
    }


# Global settings instance
settings = Settings()
