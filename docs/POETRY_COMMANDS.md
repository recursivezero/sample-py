# Useful Poetry commands

## clean the cache

- when you are in virtual environment type `exit` to stop virtual environment then run

```sh
poetry cache clear . --all
```

## delete cache files

```sh
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type d -name ".pytest_cache" -exec rm -r {} +

```

## remove lockfile and install

```sh
rm poetry.lock
poetry install
```

Note: run `poetry install` command before running `poetry shell`

## delete virtual environment if it is on custom location

1. To check the custom location run `poetry env info --path` also you can check all config using

```sh
poetry config --list
```

and see against `virtualenvs.path ` value

2. clean virtual environment

```sh
rm -rf $(poetry env info --path)
```

## Remove Virtual Environment

first check the env list

```sh
poetry env list
```

this output something like this

> tz-script-fBo1usnc-py3.12 (Activated)

now delete using version showing at the end of the environment name

```sh
poetry env remove python3.12
```

## Package mode

check with `poetry env info` to verify

## get all version details of poetry

```sh
poetry debug info
```

```swift
Poetry
Version: 2.1.4
Python:  3.12.7

Virtualenv
Python:         3.12.7
Implementation: CPython
Path:           ~/Library/Caches/pypoetry/virtualenvs/tz-script-7YHTbn9s-py3.12
Executable:     ~/Library/Caches/pypoetry/virtualenvs/tz-script-7YHTbn9s-py3.12/bin/python
Valid:          True

Base
Platform:   darwin
OS:         posix
Python:     3.12.7
Path:       ~/.pyenv/versions/3.12.7
Executable: ~/.pyenv/versions/3.12.7/bin/python3.12
```

## check poetry core version

```sh
poetry run python -c "import poetry.core; print(poetry.core.__version__)"
```

## Install a package in dev dependencies

```sh
poetry add --group dev twine
```

## publish packages

1. Register your account on <https://test.pypi.org> and generate token; which copy and save
2. Add TestPyPI repository to Poetry:

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

```sh
poetry publish -r testpypi --build
```

3. save Token in file
   create a file on your root `.pipyrc` and put below content and replace token

```yml
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
username = __token__
password = pypi-<your-real-token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-<your-test-token>
```

4. run publish command

```sh
poetry build          # optional, creates dist/*.whl and dist/*.tar.gz
poetry publish -r testpypi
```

or single command which do build also

```sh
poetry publish -r testpypi --build

```

## run Audit in development

```sh
poetry run pip-audit -r requirements.txt
```

## check version dependencies

```sh
poetry show --tree <package-name>
```

so you can check if upgrading is actually possible without breaking things?

to see package details from testPyPI portal

```sh
pip index versions sample -i https://test.pypi.org/simple
```
