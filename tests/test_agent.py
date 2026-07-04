from src.app.agent import answer_question


def test_engineer_can_answer_incident_review_question():
    result = answer_question("生产事故复盘报告应该包含哪些内容？", role="engineer", department="engineering")
    assert result["status"] == "answered"
    assert result["citations"]
    assert "复盘" in result["answer"]


def test_permission_filter_can_refuse():
    result = answer_question("生产事故复盘报告应该包含哪些内容？", role="employee", department="product")
    assert result["status"] in {"answered", "refused"}
    assert result["denied_chunks"] >= 1
