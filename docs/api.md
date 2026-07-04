# API 文档

## `POST /ask`

请求：

```json
{
  "question": "生产事故复盘报告应该包含哪些内容？",
  "role": "engineer",
  "department": "engineering",
  "top_k": 5
}
```

响应：

| 字段 | 说明 |
|---|---|
| `answer` | 回答或拒答说明 |
| `citations` | 引用来源 |
| `denied_chunks` | 因权限过滤未参与检索的 chunk 数 |
| `status` | `answered` 或 `refused` |

## `POST /feedback`

请求：

```json
{
  "question": "生产事故复盘报告应该包含哪些内容？",
  "rating": 5,
  "comment": "回答完整，引用清晰"
}
```

响应：

```json
{
  "status": "recorded",
  "feedback_id": "2026-07-04T14:30:00.000000Z",
  "rating": 5
}
```

## `GET /health`

服务健康检查。
