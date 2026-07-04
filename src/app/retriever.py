from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path

TOKEN_RE = re.compile(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]")
DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "data"


@dataclass(frozen=True)
class KnowledgeChunk:
    id: str
    title: str
    department: str
    min_role: str
    text: str
    score: float = 0.0


ROLE_ORDER = {"guest": 0, "employee": 1, "engineer": 2, "manager": 3, "admin": 4}


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def _parse_document(path: Path) -> tuple[dict[str, str], str]:
    metadata = {"title": path.stem, "department": "all", "min_role": "employee"}
    lines = path.read_text(encoding="utf-8").splitlines()
    body_start = 0
    for index, line in enumerate(lines):
        if not line.strip():
            body_start = index + 1
            break
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
    return metadata, "\n".join(lines[body_start:]).strip()


def load_chunks(data_dir: Path | str | None = None) -> list[KnowledgeChunk]:
    root = Path(data_dir) if data_dir else DEFAULT_DATA_DIR
    chunks: list[KnowledgeChunk] = []
    for path in sorted(root.glob("*.md")):
        metadata, body = _parse_document(path)
        paragraphs = [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
        for number, paragraph in enumerate(paragraphs, start=1):
            chunks.append(
                KnowledgeChunk(
                    id=f"{path.stem}-{number}",
                    title=metadata.get("title", path.stem),
                    department=metadata.get("department", "all"),
                    min_role=metadata.get("min_role", "employee"),
                    text=paragraph,
                )
            )
    return chunks


def can_access(chunk: KnowledgeChunk, role: str, department: str) -> bool:
    role_ok = ROLE_ORDER.get(role, 0) >= ROLE_ORDER.get(chunk.min_role, 1)
    dept_ok = chunk.department in {"all", department}
    return role_ok and dept_ok


def retrieve(question: str, role: str = "employee", department: str = "all", top_k: int = 5, data_dir: Path | str | None = None) -> tuple[list[KnowledgeChunk], int]:
    query_tokens = tokenize(question)
    chunks = load_chunks(data_dir)
    accessible = [chunk for chunk in chunks if can_access(chunk, role, department)]
    denied_count = len(chunks) - len(accessible)

    document_frequency: dict[str, int] = {}
    chunk_tokens: dict[str, list[str]] = {}
    for chunk in accessible:
        tokens = tokenize(chunk.title + " " + chunk.text)
        chunk_tokens[chunk.id] = tokens
        for token in set(tokens):
            document_frequency[token] = document_frequency.get(token, 0) + 1

    scored: list[KnowledgeChunk] = []
    total_docs = max(len(accessible), 1)
    for chunk in accessible:
        tokens = chunk_tokens[chunk.id]
        token_count = len(tokens) or 1
        score = 0.0
        for token in query_tokens:
            tf = tokens.count(token) / token_count
            idf = math.log((total_docs + 1) / (document_frequency.get(token, 0) + 1)) + 1
            score += tf * idf
        if score > 0:
            scored.append(
                KnowledgeChunk(
                    id=chunk.id,
                    title=chunk.title,
                    department=chunk.department,
                    min_role=chunk.min_role,
                    text=chunk.text,
                    score=round(score * 100, 4),
                )
            )
    return sorted(scored, key=lambda item: item.score, reverse=True)[:top_k], denied_count
