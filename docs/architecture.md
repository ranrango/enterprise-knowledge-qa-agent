# 架构设计

## 目标

企业知识库问答不是简单 RAG，它必须处理权限、引用、拒答、反馈和审计。系统需要保证“能回答时带来源，不能回答时明确拒答”。

## 数据流

```text
用户问题 + 用户身份
  -> 文档加载
  -> 权限过滤
  -> RAG 检索
  -> 证据充足性判断
  -> 回答生成 / 拒答
  -> 引用返回
  -> 用户反馈记录
```

## 模块职责

| 模块 | 职责 | 当前实现 | 生产替换 |
|---|---|---|---|
| Document Loader | 读取企业文档 | Markdown 样例 | PDF/Word/飞书/Confluence/数据库 |
| Access Control | 过滤不可访问文档 | role + department | SSO + RBAC/ABAC |
| Retriever | 找相关 chunk | 关键词检索 | Hybrid Search + Reranker |
| Answer Builder | 生成可引用回答 | 模板化总结 | LLM + citation guardrail |
| Feedback | 记录评价 | JSONL | 数据库 + 标注平台 |

## 关键工程点

1. 先做权限过滤，再做检索，避免越权 chunk 进入上下文。
2. 回答必须返回 citations，前端可以展开来源。
3. 证据不足时拒答，不让模型编制度。
4. 用户反馈要落库，用于后续评测和知识库补齐。
