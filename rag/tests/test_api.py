import pytest
from fastapi.testclient import TestClient
from rag.src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Textbook RAG Service"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ping():
    # Since there's no ping endpoint by default, we'll test the root
    response = client.get("/")
    assert response.status_code == 200