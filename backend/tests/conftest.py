"""
Pytest configuration and fixtures.
"""

from collections.abc import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings
from app.core.database import Base, get_db
from main import app

# Test database URL
TEST_DATABASE_URL = settings.TEST_DATABASE_URL

# Create test engine
test_engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=False,
)

# Create test session factory
TestingSessionLocal = async_sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession]:
    """Create a test database session."""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestingSessionLocal() as session:
        yield session

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def client(db_session: AsyncSession) -> Generator[TestClient]:
    """Create a test client."""

    def override_get_db() -> Generator[AsyncSession]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def test_app() -> FastAPI:
    """Get the test application."""
    return app
