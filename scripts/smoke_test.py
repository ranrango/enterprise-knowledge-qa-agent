from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.app.agent import answer_question


DEFAULT_QUESTION = "生产事故复盘报告应该包含哪些内容？"


def run_smoke_test() -> dict[str, object]:
    engineer_answer = answer_question(
        DEFAULT_QUESTION,
        role="engineer",
        department="engineering",
        top_k=5,
    )
    restricted_answer = answer_question(
        DEFAULT_QUESTION,
        role="employee",
        department="product",
        top_k=5,
    )
    return {
        "service": "enterprise-knowledge-qa-agent",
        "status": "ok" if engineer_answer["citations"] else "failed",
        "question": DEFAULT_QUESTION,
        "answer_status": engineer_answer["status"],
        "citation_count": len(engineer_answer["citations"]),
        "denied_chunks": engineer_answer["denied_chunks"],
        "permission_filter_checked": restricted_answer["denied_chunks"] > 0,
    }


def main() -> None:
    print(json.dumps(run_smoke_test(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
