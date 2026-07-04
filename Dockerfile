FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
COPY data ./data
RUN mkdir -p storage && pip install --no-cache-dir -e .

EXPOSE 8030
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8030"]
