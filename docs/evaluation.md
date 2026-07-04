# 评估方案

## 评估目标

企业知识库问答 Agent 不能只评估“答得像不像”，还要评估权限、引用、拒答和反馈闭环。

## 核心指标

| 指标 | 说明 | 合格标准 |
|---|---|---|
| Retrieval Hit Rate | Top-K 是否命中正确文档 | 标准问题应命中对应制度或 SOP |
| Citation Accuracy | 引用是否对应回答内容 | 每个关键结论都能追溯到 citation |
| Refusal Accuracy | 证据不足时是否拒答 | 未覆盖问题不编造答案 |
| Permission Blocking | 是否阻止越权文档进入上下文 | 非授权角色不能检索部门私有文档 |
| Feedback Coverage | 用户反馈是否可沉淀 | 低评分问题可进入后续优化队列 |

## 样例评测

```json
{
  "question": "生产事故复盘报告应该包含哪些内容？",
  "role": "engineer",
  "department": "engineering",
  "expected_status": "answered",
  "expected_citation": "engineering_incident_review"
}
```

## 失败归因

- 检索未命中：检查 chunk、关键词、向量模型和重排序。
- 权限泄漏：确认权限过滤发生在检索前，而不是生成后。
- 回答幻觉：要求回答只使用 citation 中的证据。
- 拒答过多：检查知识库覆盖率和问题改写策略。

## 上线监控

- Top-K 命中率和无答案率。
- 拒答率、越权拦截率和用户满意度。
- 热门未覆盖问题。
- 文档更新时间和索引构建成功率。
- 反馈闭环处理时长。
