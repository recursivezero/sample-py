# use this to update version in setup.py automatically
# when building the package, so that we don't have to maintain version in two places

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # Python <3.8
    from importlib.metadata import PackageNotFoundError, version


def get_version() -> str:
    try:
        return version("sample")  # must match pyproject.toml [project].name
    except PackageNotFoundError:
        return "0.0.0"
