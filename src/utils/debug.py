import os
import sys
from pathlib import Path

CURRENT_PATH = os.path.dirname(__file__)

SRC_PATH = os.path.dirname(os.path.abspath(__file__))

print("SRC PATH", SRC_PATH)

# Get the root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

print(f"Project Root: {PROJECT_ROOT}")
print(f"Current script path: {CURRENT_PATH}")
print(f"Working directory: {os.getcwd()}")
print(f"Command used: {sys.argv[0]}")
