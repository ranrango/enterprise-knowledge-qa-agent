# v0.1.0 Release Notes

## Highlights

- 企业知识库 RAG 问答闭环：权限过滤、检索、引用回答、拒答和反馈记录。
- 提供 CLI、FastAPI、Docker、docker-compose、Makefile 和 smoke test。
- README 增加架构图和 smoke 输出图，便于 GitHub 展示和面试讲解。
- 文档包含 API、部署、复现、评估方案、路线图和面试讲述稿。

## Verification

```bash
python3 -m pytest tests/ -q
python3 scripts/smoke_test.py
```

期望 smoke 输出包含：

- `status: ok`
- `answer_status: answered`
- `citation_count: 5`
- `permission_filter_checked: true`

## Next

- 接入 Chroma/FAISS、embedding 和 hybrid search。
- 引入 SSO、RBAC/ABAC 和企业组织架构。
- 支持 PDF、Word、飞书、Confluence 等文档源。
- 增加引用一致性评估、拒答评估和反馈闭环看板。
