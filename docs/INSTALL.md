# Installation Guide

## Prerequisites

- Python ≥ 3.11
- Poetry ≥ 2.2.1

## Getting Started

[macOS Setup Guide](./setup-for-osx.md)

[Windows Setup Guide](./setup-for-windows.md)

## Poetry Setup

```bash
curl -sSL https://install.python-poetry.org | python3 -
# OR
pip install poetry>=1.5.0
```

## Virtual Environment Configuration

```bash
poetry config virtualenvs.path /your/desired/path
```

Ensure `.env.local`, `.env` are configured with appropriate keys.

## Install Dependencies

```bash
poetry lock --no-cache
poetry install --all-extras --with dev

```

Or manually

```bash
poetry install
poetry install --extras "each block name with spaces"
```
