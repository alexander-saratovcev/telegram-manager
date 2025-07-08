"""
Tests for configuration module.
"""

from app.core.config import Settings


def test_settings_default_values() -> None:
    """Test that settings have proper default values."""
    settings = Settings()

    # Test that required settings exist
    assert hasattr(settings, "PROJECT_NAME")
    assert hasattr(settings, "DEBUG")
    assert hasattr(settings, "DATABASE_URL")
    assert hasattr(settings, "REDIS_URL")

    # Test default values
    assert settings.PROJECT_NAME == "Telegram Manager Backend"
    assert settings.DEBUG is False


def test_settings_environment_override() -> None:
    """Test that settings can be overridden by environment variables."""
    import os

    # Set environment variable
    os.environ["PROJECT_NAME"] = "Test App"
    os.environ["DEBUG"] = "true"

    try:
        settings = Settings()
        assert settings.PROJECT_NAME == "Test App"
        assert settings.DEBUG is True
    finally:
        # Clean up environment variables
        os.environ.pop("PROJECT_NAME", None)
        os.environ.pop("DEBUG", None)


def test_settings_database_url_format() -> None:
    """Test that database URL is properly formatted."""
    settings = Settings()

    # Test that DATABASE_URL is a string
    assert isinstance(settings.DATABASE_URL, str)

    # Test that it contains expected components
    assert "postgresql" in settings.DATABASE_URL.lower()


def test_settings_redis_url_format() -> None:
    """Test that Redis URL is properly formatted."""
    settings = Settings()

    # Test that REDIS_URL is a string
    assert isinstance(settings.REDIS_URL, str)

    # Test that it contains expected components
    assert "redis" in settings.REDIS_URL.lower()


def test_settings_model_config() -> None:
    """Test that Settings model has proper configuration."""
    # Test that the model can be instantiated
    settings = Settings()

    # Test that it has proper Pydantic configuration
    assert hasattr(settings, "model_config")

    # Test that env_file is configured
    assert settings.model_config["env_file"] == ".env"
