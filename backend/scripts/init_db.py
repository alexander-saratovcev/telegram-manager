#!/usr/bin/env python3
"""
Database initialization script for Telegram Manager Backend.
"""
import asyncio

import asyncpg

from app.core.config import settings


async def create_database(database_url: str, database_name: str) -> None:
    """Create database if it doesn't exist."""
    # Extract connection parameters from URL
    # Format: postgresql+asyncpg://user:password@host:port/database
    url_parts = database_url.replace("postgresql+asyncpg://", "").split("/")
    connection_string = url_parts[0]

    try:
        # Connect to PostgreSQL server (without specifying database)
        conn = await asyncpg.connect(f"postgresql://{connection_string}/postgres")

        # Check if database exists
        exists = await conn.fetchval(
            "SELECT 1 FROM pg_database WHERE datname = $1", database_name
        )

        if not exists:
            print(f"Creating database: {database_name}")
            await conn.execute(f'CREATE DATABASE "{database_name}"')
            print(f"Database '{database_name}' created successfully!")
        else:
            print(f"Database '{database_name}' already exists.")

        await conn.close()

    except Exception as e:
        print(f"Error creating database '{database_name}': {e}")
        raise


async def init_databases() -> None:
    """Initialize both main and test databases."""
    print("Initializing databases...")

    # Create main database
    main_db_name = settings.DATABASE_URL.split("/")[-1]
    await create_database(settings.DATABASE_URL, main_db_name)

    # Create test database
    test_db_name = settings.TEST_DATABASE_URL.split("/")[-1]
    await create_database(settings.TEST_DATABASE_URL, test_db_name)

    print("Database initialization completed!")


def main() -> None:
    asyncio.run(init_databases())


if __name__ == "__main__":
    main()
