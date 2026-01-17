# Project Setup for Windows user

## WINDOWS

### Prerequisites

- Python v3.11.7+
- Windows 10/11

1. **Navigate to the project root:**

```sh
cd \project\folder
```

2. **Install useful packages:**

```sh
pip install vulture ruff
```

3. **Create a virtual environment:**

```sh
python -m venv .venv
```

> **Note**: Ensure `venv` is installed with your Python setup.

4. **Activate the virtual environment:**

```sh
.\.venv\Scripts\activate
```

5. \*\*Install dependencies

### Using `requirements.txt`\*\*

```sh
pip install -r requirements.txt
```

OR

### using Poetry\*\*

```sh
pip install poetry
poetry lock
poetry install
```

1. **Update dependencies if required:**

```sh
poetry update
```

Note: To add or remove any package within the virtual environment, run:

```sh
poetry add <package-name>
poetry remove <package-name>
exit
```

7. **Test all dependencies before running:**

```sh
poetry run ruff check
```

8. **Fix any issues and check the dependency list:**

```sh
poetry show --tree
```

9. **Run the application:**

Note: if you want use `poetry shell` command then install and then run as below

```sh
   pip install poetry-plugin-shell
   poetry shell
   sample dev
```

- Open [http://localhost:8085](http://localhost:8085) in a web browser
