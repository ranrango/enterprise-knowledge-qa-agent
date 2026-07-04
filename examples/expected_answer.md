# 企业知识库问答示例

## 核心回答

当用户角色为 `engineer`、部门为 `engineering` 时，系统应能检索到《生产事故复盘规范》，并回答复盘报告应包含事故时间线、影响范围、根因分析、临时止血措施、长期修复方案、责任人、截止时间和验证标准。

## 期望检查点

- 状态为 `answered`。
- 返回至少 2 条 citation。
- 回答中包含来源编号，例如 `[engineering_incident_review-1]`。
- 当用户切换为 `employee + product` 时，应触发权限过滤提示。

## 演示命令

```bash
python3 -m src.app.cli --question "生产事故复盘报告应该包含哪些内容？" --role engineer --department engineering
python3 scripts/smoke_test.py
```
