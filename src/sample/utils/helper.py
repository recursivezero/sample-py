def normalize_name(name: str) -> str | None:
    """
    Normalize and validate a user's name.
    Returns None if input is not usable.
    """
    if not name:
        return None

    clean = name.strip().title()

    if len(clean) < 2:
        return None

    return clean
