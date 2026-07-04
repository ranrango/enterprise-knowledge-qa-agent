# 复现指南

## 1. 命令行问答

```bash
python3 -m src.app.cli --question "生产事故复盘报告应该包含哪些内容？" --role engineer --department engineering --json
```

## 2. 权限测试

```bash
python3 -m src.app.cli --question "生产事故复盘报告应该包含哪些内容？" --role employee --department product --json
```

预期：工程部门文档不可访问，系统应拒答或只基于公共文档回答。

## 3. 运行测试

```bash
python3 -m pytest tests/ -q
```
