import os
import shutil
import subprocess
from pathlib import Path


def _remove_artifacts():
    for path in ["dist", "build"]:
        shutil.rmtree(path, ignore_errors=True)

    for p in Path(".").glob("*.egg-info"):
        shutil.rmtree(p, ignore_errors=True)


def clean():
    print("Cleaning build artifacts...")
    _remove_artifacts()
    print("Done ✨")


def reset():
    print("Cleaning build artifacts...")
    _remove_artifacts()

    if "VIRTUAL_ENV" in os.environ:
        print("You are inside a Poetry env. Cannot delete active env.")
        print("Run this instead:")
        print("  deactivate && poetry run reset")
        return

    print("Removing virtualenv...")
    subprocess.run(["poetry", "env", "remove", "--all"], check=False)

    print("Reinstalling dependencies...")
    subprocess.run(["poetry", "install"], check=True)

    print("Environment fully reset ✨")


def main():
    clean()


if __name__ == "__main__":
    main()
