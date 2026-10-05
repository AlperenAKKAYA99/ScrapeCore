__author__ = "Alperen AKKAYA"
__version__ = "0.4.15"
__copyright__ = "Copyright (c) 2026 Alperen AKKAYA, (c) 2024 Karim Shoair"
__upstream__ = "https://github.com/D4Vinci/Scrapling"

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from scrapecore.parser import Selector, Selectors
    from scrapecore.core.custom_types import AttributesHandler, TextHandler
    from scrapecore.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher


# Lazy import mapping
_LAZY_IMPORTS = {
    "Fetcher": ("scrapecore.fetchers", "Fetcher"),
    "Selector": ("scrapecore.parser", "Selector"),
    "Selectors": ("scrapecore.parser", "Selectors"),
    "AttributesHandler": ("scrapecore.core.custom_types", "AttributesHandler"),
    "TextHandler": ("scrapecore.core.custom_types", "TextHandler"),
    "AsyncFetcher": ("scrapecore.fetchers", "AsyncFetcher"),
    "StealthyFetcher": ("scrapecore.fetchers", "StealthyFetcher"),
    "DynamicFetcher": ("scrapecore.fetchers", "DynamicFetcher"),
}
__all__ = ["Selector", "Fetcher", "AsyncFetcher", "StealthyFetcher", "DynamicFetcher"]


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module_path, class_name = _LAZY_IMPORTS[name]
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Support for dir() and autocomplete."""
    return sorted(__all__ + ["fetchers", "parser", "cli", "core", "__author__", "__version__", "__copyright__"])
