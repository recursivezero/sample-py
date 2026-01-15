# How to Run

## Run Sample app

```bash
poetry run sample dev

```

Access: <http://localhost:8501>

## Run FastAPI Server

```bash
poetry run sample api
# OR
python src/api/fast_api.py
```

Access: <http://127.0.0.1:5000>

## 🧹 Linting & Code Quality

Pre-commit hooks are enabled. If commits fail, run:

```bash
poetry run black .
poetry run flake8 .
poetry run mypy .
poetry run ruff check .
```
