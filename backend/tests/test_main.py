from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_ask_agent():
    response = client.post("/ask", json={"question": "What is 2+2?"})
    assert response.status_code == 200
    assert "answer" in response.json()
