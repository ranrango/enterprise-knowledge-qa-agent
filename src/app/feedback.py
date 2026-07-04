from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Union

DEFAULT_FEEDBACK_PATH = Path(__file__).resolve().parents[2] / "storage" / "feedback.jsonl"


def record_feedback(
    question: str,
    rating: int,
    comment: str = "",
    path: Optional[Union[Path, str]] = None,
) -> Dict[str, object]:
    target = Path(path) if path else DEFAULT_FEEDBACK_PATH
    target.parent.mkdir(exist_ok=True)
    feedback_id = datetime.utcnow().isoformat() + "Z"
    item = {
        "time": feedback_id,
        "question": question,
        "rating": rating,
        "comment": comment,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    return {"status": "recorded", "feedback_id": feedback_id, "rating": rating}
