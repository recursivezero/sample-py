# Sample BoilerPlate

A Sample template for Recursive Zero repository

## Installation Guide

## Prerequisites

- Python ≥ 3.11FAQ
- Poetry ≥ 2.2.1

## Getting Started

- [Unix/macOS Setup Guide](./docs/setup-for-osx.md)

- [Windows Setup Guide](./docs/setup-for-windows.md)

## Poetry Setup

```bash
curl -sSL https://install.python-poetry.org | python3 -
# OR
pip install poetry>=2.2.1
```

## Virtual Environment Configuration

```bash
poetry config virtualenvs.path /your/desired/path
```

Ensure below files are configured (create if not exist) properly to run the project;

- `.env.local`,
- `.env`, and

## Install Dependencies

```bash
poetry lock --no-cache --regenerate
poetry install  --all-extras --with dev
```

Or manually

```bash
poetry install
```

## How to Run

## Run Sample App

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
poetry run lint
```

or run individual

```bash
poetry run black .
poetry run flake8 .
poetry run mypy .
poetry run ruff check .
```

## Build & Packaging

## Build Package

```bash
poetry clean
poetry build
```

Artifacts in `dist/`

- sample-x.y.0-py3-none-any.whl
- sample-x.y.0.tar.gz

## Test Locally

```bash
python -m venv .venv-dist
source .venv-dist/bin/activate
# Windows
.venv-dist\Scripts\activate
```

### Install package

```bash
pip install dist/*.whl
pip install --upgrade dist/*.whl
# Install extras:
pip install sample
```

## CLI Shortcuts

`sample dev` → Launch UI

`sample api` → Launch FastAPI

current version will be printed on start of above commands.

## Install GIT hooks

these hooks will

- Check for lint and audit for security before commit
- Append branch name in commit message
- Generate requirements.txt on checkout on new branch

```bash
# Install git hooks
poetry run ./scripts/setup-hooks.sh
```

there is `.vscode/Python.code-profile` file; import this as a profile in vscode which include necessary extension for python development.

## Troubleshooting

sometimes there might be chances that virtual environment get corrupted then delete the old virtual environment and start afresh.

```sh
poetry env info
# this will provide virtual environment name
poetry env remove <environment-full-name>
```

## Reset Environment

Use the reset script to clean artifacts and recreate the project virtual environment:

```bash
./scripts/reset.sh
```

Note:

On first clone, the script is already executable (permission is tracked in git).

If you see Permission denied, run once:

```bash
chmod +x scripts/reset.sh
```

This will completely reset the environment.

## License

[MIT](./LICENSE)

## References

- [Python Downloads](https://www.python.org/downloads)
- [Virtualenv Docs](https://docs.python.org/3/library/venv.html)
- [Python Tips](https://www.airplane.dev/blog/12-useful-python-scripts-for-developers)
- [Poetry Docs](https://python-poetry.org/docs/)
- [MyPy Docs](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)
- [Useful Poetry commands](./docs//POETRY_COMMANDS.md)
