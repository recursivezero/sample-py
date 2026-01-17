#!/usr/bin/env bash
set -e

echo "Cleaning build artifacts..."
rm -rf dist build *.egg-info

echo "Removing project virtualenv..."
poetry env remove --all || true

echo "Reinstalling dependencies..."
poetry install

echo "Environment fully reset ✨"
