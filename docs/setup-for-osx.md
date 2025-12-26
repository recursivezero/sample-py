# Project Setup for Linux/MacOs users

## Prerequisites

- Python v3.12.7+
- Ubuntu 24.04
- MacOS sequoia 15.1.1
- Git

### How to Start

1. Navigate to the project root:

```sh
  cd /project/tz-script
```

2. install required packages

```sh
pip3 install vulture ruff
```

### Using Poetry ( recommended )

in Ubuntu install **poetry** using below command

```sh
sudo apt install python3-poetry python3-poetry-core python3-poetry-plugin-export
pip3 install poetry-plugin-shell
```

for osx, run below commands one by one to install poetry

```sh
brew install pipx
pipx ensurepath
pipx install poetry==2.0.0
pipx ensurepath
pip3 install poetry-plugin-shell
poetry --version
```

then run

```sh
poetry lock
poetry install
```

Note: `poetry install` automatically activate the virtual environment

---

To add or remove any package within the virtual environment, run:

```sh
poetry add <package-name>
poetry add --group dev <package-name> # for development environment only
poetry remove <package-name>
poetry update  # to update dependencies
```

---

1. **Test all dependencies before running:**

```sh
poetry run ruff check
```

2. **Fix any issues and check the dependency list:**

```sh
poetry show --tree
```

3. **Run the Streamlit application:**

```sh
poetry run sample dev
```

or

```sh
 poetry shell
 sample dev
```

Open [http://localhost:8085](http://localhost:8085) in a web browser.

### using **environment.txt** file

2. Install necessary packages:

3. Create a virtual environment:

```sh
python3 -m venv ~/dev/project/.venv
```

> **Note**: Replace `~/dev/project/.venv` with any desired path. Delete the existing `.venv` folder if needed.

4. Activate the virtual environment:

```sh
source ~/dev/project/.venv/bin/activate
```

5. Install dependencies:

   **Using `requirements.txt`**

```sh
pip3 install -r requirements.txt
```
