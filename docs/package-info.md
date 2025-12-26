# sample package info

## Check the package size

```bash
du -sh dist/
```

This gives you the total size of the dist/ folder.

## Inspect contents (if needed) To see what’s inside the wheel

```bash
unzip -l dist/your_package.whl

```

Or for the source distribution:

```bash
tar -tzf dist/your_package.tar.gz
```

this will display version and package

```sh
pip index versions sample --index-url https://test.pypi.org/simple/
```

## How to test published package locally

create new folder

```sh
mkdir pkg-test
cd pkg-test
python -m venv venv
source venv/bin/activate
```

then install

```sh
pip cache purge
pip install --no-cache-dir --default-timeout=100 -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple

# or with exact version

pip install --no-cache-dir --default-timeout=100 -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple sample==3.4.7
```

## Run Extra packages separately

```sh
pip install sample[api]
pip install sample[ml,ocr,cv]
```

create file _test.py_

```py

import sample   # use your package’s import name

def main():
    print("Testing sample package")
    print(sample.__version__)

if __name__ == "__main__":
    main()
```

uninstall using `pip uninstall sample`
