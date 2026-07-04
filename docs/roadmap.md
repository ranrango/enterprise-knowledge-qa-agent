# Roadmap

## v0.1 当前版本

- Markdown 样例知识库。
- 角色和部门权限过滤。
- 关键词检索、引用回答、拒答和反馈记录。
- CLI、FastAPI、Docker、smoke test 和项目文档。

## v0.2 RAG 能力增强

- 接入 Chroma 或 FAISS。
- 引入 embedding 和 hybrid search。
- 增加查询改写和 Reranker。
- 增加证据充足性评分和引用一致性检查。

## v0.3 企业系统集成

- 接入 SSO、RBAC/ABAC 和组织架构。
- 支持 PDF、Word、飞书、Confluence、网页等文档源。
- 增加增量索引、文档版本和过期策略。
- 将反馈写入数据库和标注平台。

## v0.4 生产交付

- API Gateway + Auth + Rate Limit。
- trace、审计日志和管理员后台。
- 自动评测集和灰度发布。
- 监控拒答率、越权拦截率、引用准确率和用户满意度。
