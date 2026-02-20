# utils/get_message.py
from box import Box
import importlib


# auto-collect static  and text blocks from utils.static
_static_module = importlib.import_module("utils.templates")
_TEMPLATE_MAP = {}
for name, val in vars(_static_module).items():
    # collect names that end with _TEMPLATE (convention)
    if name.endswith("_TEMPLATE"):
        feature_key = name[:-9]  # remove suffix _TEMPLATE -> e.g. FABRIC_GENERATOR
        _TEMPLATE_MAP[feature_key] = val

_text_module = importlib.import_module("utils.messages")
_TEXT_MAP = {}
for name, val in vars(_text_module).items():
    # collect names that end with _TEMPLATE (convention)
    if name.endswith("_TEXT"):
        feature_key = name[:-5]  # remove suffix _TEXT -> e.g. FABRIC_GENERATOR
        _TEXT_MAP[feature_key] = val


def deep_merge(a, b):
    # Treat None or non-dict as empty dict
    if not isinstance(a, dict):
        a = {}
    if not isinstance(b, dict):
        b = {}

    result = dict(a)

    for k, v in b.items():
        av = result.get(k)

        # If both sides are dicts, merge deeper
        if isinstance(av, dict) and isinstance(v, dict):
            result[k] = deep_merge(av, v)
        else:
            # Otherwise, override with b’s value
            result[k] = v

    return result


def get_msg(feature_name: str) -> Box:
    feature_key = feature_name.upper()
    text = _TEXT_MAP.get(feature_key)
    static = _TEMPLATE_MAP.get(feature_key)

    if static is None:
        return Box(text)

    merged = deep_merge(text, static)
    return Box(merged)
