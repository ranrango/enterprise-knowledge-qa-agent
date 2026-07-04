# Release Candidate Manifest

Generated: 2026-07-04

## Included

- `README.md`
- `pyproject.toml`
- `Makefile`
- `Dockerfile`
- `docker-compose.yml`
- `.env.example`
- `.gitignore`
- `assets/architecture.svg`
- `assets/smoke-output.svg`
- `src/app/*.py`
- `scripts/*.py`
- `examples/*`
- `data/*.md`
- `tests/*.py`
- `docs/*.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `RELEASE_NOTES.md`
- `LICENSE`

## Intentionally Excluded

- `.env`
- 真实企业知识库
- 真实用户反馈和访问日志
- 向量库持久化文件
- 模型权重和凭据

## Release Notes

本版本用于展示企业 RAG Agent 的核心工程问题：权限、引用、拒答、反馈和交付。

## Post-Release Improvements

- 增加 `scripts/smoke_test.py` 一键自检。
- 增加 examples、评估方案和路线图文档。
- README 增加预期输出和项目展示说明。
- 增加架构图、smoke 输出图和 v0.1.0 release notes。
