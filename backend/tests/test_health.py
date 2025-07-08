"""
Tests for health check endpoints.
"""

from fastapi.testclient import TestClient


def test_health_check_endpoint(client: TestClient) -> None:
    """Test basic health check endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "API is running"


def test_database_health_check_response_structure(client: TestClient) -> None:
    """Test database health check endpoint response structure."""
    response = client.get("/api/v1/health/db")
    assert response.status_code == 200
    data = response.json()

    # Check that response has required fields
    assert "status" in data
    assert "database" in data
    assert isinstance(data["status"], str)
    assert isinstance(data["database"], str)

    # Status should be either "healthy" or "unhealthy"
    assert data["status"] in ["healthy", "unhealthy"]

    # Database should be either "connected" or "disconnected"
    assert data["database"] in ["connected", "disconnected"]

    # If unhealthy, should have error field
    if data["status"] == "unhealthy":
        assert "error" in data
        assert isinstance(data["error"], str)


def test_health_endpoints_structure(client: TestClient) -> None:
    """Test that health endpoints return proper JSON structure."""
    # Test basic health endpoint
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "status" in data
    assert "message" in data
    assert isinstance(data["status"], str)
    assert isinstance(data["message"], str)

    # Test database health endpoint
    response = client.get("/api/v1/health/db")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "status" in data
    assert "database" in data
    assert isinstance(data["status"], str)
    assert isinstance(data["database"], str)


def test_health_endpoints_content_type(client: TestClient) -> None:
    """Test that health endpoints return proper content type."""
    response = client.get("/api/v1/health/")
    assert response.headers["content-type"] == "application/json"

    response = client.get("/api/v1/health/db")
    assert response.headers["content-type"] == "application/json"
