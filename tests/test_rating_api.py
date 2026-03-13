from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_rating():

    payload = {
        "dm_id": 1,
        "reporter_id": 10,
        "dm_teaching_rating": 8,
        "reporter_learning_rating": 7
    }

    response = client.post("/ratings/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "ai_efficiency_score" in data
    assert "feedback" in data