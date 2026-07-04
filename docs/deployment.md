# 部署交付说明

## 本地部署

```bash
pip install -e .
uvicorn src.app.main:app --host 0.0.0.0 --port 8030
```

## Docker 部署

```bash
docker compose up --build
```

## 生产交付架构

```text
前端/企业 IM
  -> API Gateway / Auth
  -> Knowledge QA Agent
  -> 文档解析服务
  -> 向量库 + 关键词索引
  -> 权限系统
  -> 日志与反馈数据库
```

## 交付验收指标

- 问答引用准确率。
- 拒答准确率。
- 越权访问拦截率。
- Top-K 检索命中率。
- 平均响应延迟和错误率。
- 用户反馈满意度。
