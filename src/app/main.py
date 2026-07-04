from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .agent import answer_question
from .feedback import record_feedback

app = FastAPI(title="企业知识库问答 Agent", version="0.1.0")


class AskRequest(BaseModel):
    question: str = Field(..., description="用户问题")
    role: str = Field("employee", description="用户角色")
    department: str = Field("all", description="用户部门")
    top_k: int = Field(5, ge=1, le=10, description="召回数量")


class FeedbackRequest(BaseModel):
    question: str
    rating: int = Field(..., ge=1, le=5)
    comment: str = ""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "enterprise-knowledge-qa-agent"}


@app.post("/ask")
def ask(request: AskRequest) -> dict[str, object]:
    return answer_question(
        request.question,
        role=request.role,
        department=request.department,
        top_k=request.top_k,
    )


@app.post("/feedback")
def feedback(request: FeedbackRequest) -> dict[str, object]:
    return record_feedback(request.question, request.rating, request.comment)
