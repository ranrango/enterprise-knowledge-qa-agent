from __future__ import annotations

import argparse
import json

from .agent import answer_question


def main() -> None:
    parser = argparse.ArgumentParser(description="企业知识库问答 Agent")
    parser.add_argument("--question", default="生产事故复盘报告应该包含哪些内容？")
    parser.add_argument("--role", default="employee")
    parser.add_argument("--department", default="all")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = answer_question(
        args.question, role=args.role, department=args.department, top_k=args.top_k
    )
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["answer"])


if __name__ == "__main__":
    main()
