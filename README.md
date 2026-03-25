# RZ-Sample

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rz-sample)
![pypi](https://badgen.net/pypi/v/rz-sample)
![License](https://badgen.net/pypi/license/rz-sample)

poetry + streamlit + fast api boilerplate for python development.

## Installation Guide

## Prerequisites

- Python ≥ 3.11
- Poetry ≥ 2.2.1
- Streamlit ≥ 1.49.1

## Getting Started

- [Unix/macOS Setup Guide][unix-setup]

- [Windows Setup Guide][windows-setup]

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

- `.env.development`
- `.env.production`

## Install Dependencies

```bash
poetry lock --no-cache --regenerate
poetry install  --all-extras --with dev
```

Or manually

```bash
make install
```

## How to Run

## Configure ENVIRONMENT

setup `.env.development` and `.env.production` in project root

```bash
  # for local configuration(linux)
  export ENV=development
  # for production(linux)
  export ENV=production
```

## Run Streamlit App

```bash
make dev
# OR with custom port
poetry run sample dev --port 8051

```

then open UI on : <http://localhost:8501>

to run on different port use `--port` option

```bash
poetry run sample dev --port 1234
```

## Run FastAPI Server

```bash
make api
# OR with custom port
poetry run sample api --port 5000
```

Access: <http://127.0.0.1:5000>

## 🧹 Linting & Code Quality

Pre-commit hooks are enabled. If commits fail, run:

```bash
make lint
```

or run individual

```bash
poetry run black .
poetry run flake8 .
poetry run mypy .
poetry run ruff check .
```

## CLI Shortcuts

`make dev` → Launch Streamlit UI

`make api` → Launch FastAPI

current version will be printed on start of above commands.

## Troubleshooting

sometimes there might be chances that virtual environment get corrupted then delete the old virtual environment and start afresh.

```sh
poetry env info
# this will provide virtual environment name
poetry env remove <environment-full-name>
```

## License

[MIT](https://github.com/recursivezero/rz-sample/blob/main/LICENSE)

## References

[unix-setup]: https://github.com/recursivezero/python/wiki/setup-for-osx
[windows-setup]: https://github.com/recursivezero/python/wiki/setup-for-windows

- [Python Downloads](https://www.python.org/downloads)
- [Virtualenv Docs](https://docs.python.org/3/library/venv.html)
- [Poetry Docs](https://python-poetry.org/docs/)
- [MyPy Docs](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)
- [Useful Poetry Commands](https://github.com/recursivezero/python/wiki/POETRY_COMMANDS)
