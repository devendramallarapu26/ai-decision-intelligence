from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_research_api_valid_question():
    response = client.post(
        "/research",
        json={
            "question": "Should we launch a food business?"
        }
    )

    assert response.status_code == 200
    assert response.json()["question"] == "Should we launch a food business?"
    assert response.json()["status"] == "processing"
    
def test_research_api_empty_question():
    response = client.post(
        "/research",
        json={
            "question": ""
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Question Cannot be Empty"


def test_research_api_short_question():
    response = client.post(
        "/research",
        json={
            "question": "Hello"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Question Must be More than 10 Characters"
    
def test_research_api_missing_question():
    response = client.post(
        "/research",
        json={}
    )

    assert response.status_code == 422
    
def test_research_api_invalid_question_type():
    response = client.post(
        "/research",
        json={
            "question": ["hello"]
        }
    )

    assert response.status_code == 422