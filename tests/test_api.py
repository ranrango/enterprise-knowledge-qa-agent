from fastapi.testclient import TestClient

from src.app.main import app


client = TestClient(app)


def test_health_endpoint_reports_service_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "enterprise-knowledge-qa-agent",
    }


def test_ask_endpoint_returns_permission_aware_answer():
    response = client.post(
        "/ask",
        json={
            "question": "生产事故复盘报告应该包含哪些内容？",
            "role": "engineer",
            "department": "engineering",
            "top_k": 5,
        },
    )

    payload = response.json()
    assert response.status_code == 200
    assert payload["status"] == "answered"
    assert payload["citations"]
    assert payload["denied_chunks"] >= 1
    assert "复盘" in payload["answer"]


def test_feedback_endpoint_records_user_rating():
    response = client.post(
        "/feedback",
        json={
            "question": "生产事故复盘报告应该包含哪些内容？",
            "rating": 5,
            "comment": "回答完整，引用清晰",
        },
    )

    payload = response.json()
    assert response.status_code == 200
    assert payload["status"] == "recorded"
    assert payload["rating"] == 5
