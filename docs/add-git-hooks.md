# Add github hooks

there are files in _.githooks_ folder

make them executable ( for osx )

```sh
chmod +x .githooks/pre-commit
chmod +x .githooks/prepare-commit-msg
chmod +x setup-hooks.sh
```

then run below if using poetry

```bash
poetry run ./scripts/setup-hooks.sh
```

or

```sh
#pre-commit hooks won’t run if the script has CRLF
bash ./scripts/setup-hooks.sh
```

this will add these files inside your `.git/hooks` folder

```sh
# pre-commit
DRY_RUN=1 git commit --allow-empty -m "test pre-commit"
# post-checkout
DRY_RUN=1 git switch -
# post-merge: but did not show any op if everything up to date
DRY_RUN=1 git merge HEAD
```
