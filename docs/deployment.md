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

## 交付验收命令

本地常规验收：

```bash
make check
```

交付前完整验收：

```bash
make release-check
```

`release-check` 会额外执行 Docker 镜像构建；CI 会执行同样的交付验收命令，确保 API、权限过滤 smoke、代码格式和 Docker 镜像构建都能通过。

只验证容器能启动并通过健康检查：

```bash
make container-check
```

容器内置 Docker `HEALTHCHECK`，`docker compose ps` 可以看到服务健康状态。健康检查访问：

```text
http://127.0.0.1:8030/health
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
