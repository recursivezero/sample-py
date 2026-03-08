# Publish the package on testpy

1. Register the Repository

Poetry needs to know the specific upload URL for TestPyPI. Use the legacy upload endpoint

```bash
poetry config repositories.<project-name> https://test.pypi.org/legacy/
```

1. Disable System Keyring (Optional but Recommended)
   If you encounter 403 Forbidden errors or the terminal hangs, disable the system keyring to force Poetry to use a local auth.toml file for your tokens

```bash
poetry config keyring.enabled false
```

3. Set Your API Token
   Add your TestPyPI API token. Ensure it includes the _pypi-_ prefix.

```bash
poetry config pypi-token.<project-name> pypi-your-token-here
```

1. Rename Project (If Needed)

If you need to change the package name to avoid conflicts on TestPyPI, update the name field in your pyproject.toml. After renaming, refresh your environment:

## Update the 'name' field in pyproject.toml first, then

```bash
poetry install
```

5. Build and Publish
   You can build and publish the package in a single command. The -r flag specifies the repository we configured in step 1.

```bash
poetry publish -r <project-name> --build
```

6. Update and republish
   1. change version using `poetry version major` other value is _minor_ or _patch_, use as per requirements.
   2. sync and rebuild

   ```bash
   poetry lock
   poetry build
   ```

   3. `poetry publish -r <project-name>`

---

## Quick Checklist before Publishing

- Unique Name: Ensure the name in pyproject.toml isn't already taken on [TestPyPI](https://test.pypi.org/).
- Version Bump: If you are re-uploading, you must increment the version in pyproject.toml.
- Trailing Slash: Ensure your repository URL ends with /legacy/ to avoid 405 or 400 errors.
