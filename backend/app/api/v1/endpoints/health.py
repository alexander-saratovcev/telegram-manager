"""
Health check endpoints.
"""

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def health_check() -> dict:
    """Basic health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


@router.get("/db")
async def database_health_check(db: AsyncSession = Depends(get_db)) -> dict:
    """Database health check endpoint."""
    try:
        # Simple database connection test
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
