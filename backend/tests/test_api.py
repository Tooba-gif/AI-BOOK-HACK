import pytest
from fastapi.testclient import TestClient
from backend.src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Textbook Backend API"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ping():
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

# Additional tests would go here for each endpoint
# For brevity, I'm including just a few basic tests
# In a real implementation, we would have comprehensive tests for:
# - Authentication endpoints
# - Chapter endpoints
# - Progress endpoints
# - Chat endpoints
# - Personalization endpoints
# - Translation endpoints
# - User profile endpoints