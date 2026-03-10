.PHONY: install lint format type test run api clean

PORT ?= 8501
PORT_API ?= 5000
install:
	poetry install

lint:
	poetry run ruff check .
	poetry run black --check .
	poetry run mypy .

hooks:
	poetry run scripts/setup-hooks.sh

format:
	poetry run black .
	poetry run ruff check --fix .

type:
	poetry run mypy .


dev:
	poetry run sample dev --port $(PORT)

api:
	poetry run sample api --port $(PORT_API)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache dist build
