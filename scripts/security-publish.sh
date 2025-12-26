#!/bin/bash
set -e

echo "🔎 Running security audit before publish..."
poetry export -f requirements.txt --without-hashes -o requirements.txt
poetry run pip-audit -r requirements.txt

echo "✅ No critical issues, publishing..."
poetry publish --build
