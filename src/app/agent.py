from __future__ import annotations

from pathlib import Path

from .retriever import retrieve


def answer_question(question: str, role: str = "employee", department: str = "all", top_k: int = 5, data_dir: Path | str | None = None) -> dict[str, object]:
    chunks, denied_count = retrieve(question, role=role, department=department, top_k=top_k, data_dir=data_dir)
    if not chunks:
        return {
            "answer": "当前可访问知识库中没有足够证据回答该问题。建议补充文档、提高权限后重试，或转人工确认。",
            "citations": [],
            "denied_chunks": denied_count,
            "status": "refused",
        }

    citations = [
        {"id": chunk.id, "title": chunk.title, "department": chunk.department, "score": chunk.score}
        for chunk in chunks
    ]
    answer = build_answer(question, chunks, denied_count)
    return {"answer": answer, "citations": citations, "denied_chunks": denied_count, "status": "answered"}


def build_answer(question: str, chunks, denied_count: int) -> str:
    bullets = []
    for chunk in chunks[:4]:
        sentence = chunk.text.split("。", 1)[0].strip()
        bullets.append(f"- {sentence}。来源：[{chunk.id}] {chunk.title}")

    note = ""
    if denied_count:
        note = f"\n\n权限提示：本次检索中有 {denied_count} 个 chunk 因角色或部门限制未参与回答。"

    return "\n".join(
        [
            f"问题：{question}",
            "",
            "基于当前可访问知识库，建议回答如下：",
            *bullets,
            "",
            "结论：以上回答仅基于已检索到的企业文档，若涉及正式制度或审批口径，应以最新发布文件和负责人确认为准。",
            note,
        ]
    ).strip()
