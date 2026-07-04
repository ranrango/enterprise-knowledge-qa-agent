from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

DEFAULT_FEEDBACK_PATH = Path(__file__).resolve().parents[2] / "storage" / "feedback.jsonl"


def record_feedback(
    question: str, rating: int, comment: str = "", path: Path | str | None = None
) -> dict[str, object]:
    target = Path(path) if path else DEFAULT_FEEDBACK_PATH
    target.parent.mkdir(exist_ok=True)
    item = {
        "time": datetime.utcnow().isoformat() + "Z",
        "question": question,
        "rating": rating,
        "comment": comment,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    return {"status": "recorded", "path": str(target)}
