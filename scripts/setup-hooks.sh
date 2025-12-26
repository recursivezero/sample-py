#!/bin/bash
set -e

SOURCE_HOOKS_DIR=".githooks"
GIT_HOOKS_DIR=".git/hooks"

# Ensure we are inside a git repository
if [ ! -d "$GIT_HOOKS_DIR" ]; then
    echo "Error: Run this script from the root of a Git repository."
    exit 1
fi

# Install all valid git hooks from .githooks
for HOOK in "$SOURCE_HOOKS_DIR"/*; do
    [ -f "$HOOK" ] || continue

    HOOK_NAME=$(basename "$HOOK")

    # Allow only valid git hook names
    case "$HOOK_NAME" in
        pre-*|post-*|commit-msg|prepare-commit-msg)
            ;;
        *)
            echo "Skipping non-hook file: $HOOK_NAME"
            continue
            ;;
    esac

    cp "$HOOK" "$GIT_HOOKS_DIR/$HOOK_NAME"
    # Normalize line endings to Unix style
    sed -i 's/\r$//' "$GIT_HOOKS_DIR/$HOOK_NAME"
    chmod +x "$GIT_HOOKS_DIR/$HOOK_NAME"

    echo "Installed hook: $HOOK_NAME"
done

echo "All hooks have been set up successfully."
