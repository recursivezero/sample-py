#!/bin/sh
set -e  # stop on first error

# Step 1: Check poetry setup
echo "Running poetry check..."
poetry check

# Step 2: Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist build *.egg-info

# Step 3: Build the package
echo "Building the package..."
poetry build

# Step 4: Create or activate local venv for testing
VENV_DIR=".venv-dist"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment for testing..."
    python -m venv "$VENV_DIR"
fi

echo "Activating virtual environment..."
. "$VENV_DIR/bin/activate"

# Step 5: Install or upgrade the newly built wheel
echo "Installing/upgrading wheel..."
pip install --upgrade dist/*.whl
pip install sample[ml,cv,api,ocr]

"$VENV_DIR/bin/python" -c "import sample; print(sample.__version__)"

# Step 6: Test completed, deactivate venv automatically
# deactivate || true

echo "Build and test complete. Virtual environment deactivated."
echo "You can reactivate anytime with: . \"$VENV_DIR/bin/activate\""
