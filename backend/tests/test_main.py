"""
Tests for main application endpoints.
"""

import pytest
from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Telegram Manager Backend"}


def test_health_check_endpoint(client: TestClient) -> None:
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "message" in data


def test_api_health_endpoint(client: TestClient) -> None:
    """Test API health endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "API is running"


@pytest.mark.asyncio
async def test_api_database_health_endpoint(client: TestClient) -> None:
    """Test API database health endpoint."""
    response = client.get("/api/v1/health/db")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "database" in data
