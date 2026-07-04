PYTHON ?= python3
PORT ?= 8030

.PHONY: help install install-dev run api smoke test lint format docker-build docker-run

help:
	@echo "可用命令："
	@echo "  install      安装运行依赖"
	@echo "  install-dev  安装开发依赖"
	@echo "  run          运行 CLI 问答"
	@echo "  api          启动 FastAPI 服务"
	@echo "  smoke        运行一键自检"
	@echo "  test         运行测试"
	@echo "  lint         运行 ruff 检查"
	@echo "  format       运行 black 格式检查"

install:
	$(PYTHON) -m pip install -e .

install-dev:
	$(PYTHON) -m pip install -e ".[dev]"

run:
	$(PYTHON) -m src.app.cli --question "生产事故复盘报告应该包含哪些内容？" --role engineer --department engineering

api:
	uvicorn src.app.main:app --reload --port $(PORT)

smoke:
	$(PYTHON) scripts/smoke_test.py

test:
	$(PYTHON) -m pytest tests/ --tb=short -q

lint:
	ruff check src/ scripts/ tests/

format:
	black --check src/ scripts/ tests/

docker-build:
	docker build -t enterprise-knowledge-qa-agent:latest .

docker-run:
	docker run --rm -p $(PORT):8030 enterprise-knowledge-qa-agent:latest
