# Build & Packaging

## Build Package

```bash
poetry clean
poetry build
```

Artifacts in `dist/`

- tz_script-3.x.0-py3-none-any.whl
- tz_script-3.x.0.tar.gz

## Test Locally

```bash
python -m venv .venv-dist
source .venv-dist/bin/activate
# Windows
.venv-dist\Scripts\activate
```

### Install

```bash
pip install dist/*.whl
pip install --upgrade dist/*.whl
# Install extras:
pip install sample[full]
```

### Verify

```bash
python -c "import sample; print(sample.**version**)"
# or
pip show sample
```

## CLI Shortcuts

`sample dev` → Launch frontend

`sample api` → Launch FastAPI

current version will be printed on start of above commands.
