from typing import TYPE_CHECKING, Any
from scrapecore.engines.toolbelt import ProxyRotator

if TYPE_CHECKING:
    from scrapecore.fetchers.requests import Fetcher, AsyncFetcher, FetcherSession
    from scrapecore.fetchers.chrome import DynamicFetcher, DynamicSession, AsyncDynamicSession
    from scrapecore.fetchers.stealth_chrome import StealthyFetcher, StealthySession, AsyncStealthySession


# Lazy import mapping
_LAZY_IMPORTS = {
    "Fetcher": ("scrapecore.fetchers.requests", "Fetcher"),
    "AsyncFetcher": ("scrapecore.fetchers.requests", "AsyncFetcher"),
    "FetcherSession": ("scrapecore.fetchers.requests", "FetcherSession"),
    "DynamicFetcher": ("scrapecore.fetchers.chrome", "DynamicFetcher"),
    "DynamicSession": ("scrapecore.fetchers.chrome", "DynamicSession"),
    "AsyncDynamicSession": ("scrapecore.fetchers.chrome", "AsyncDynamicSession"),
    "StealthyFetcher": ("scrapecore.fetchers.stealth_chrome", "StealthyFetcher"),
    "StealthySession": ("scrapecore.fetchers.stealth_chrome", "StealthySession"),
    "AsyncStealthySession": ("scrapecore.fetchers.stealth_chrome", "AsyncStealthySession"),
}

__all__ = [
    "Fetcher",
    "AsyncFetcher",
    "ProxyRotator",
    "FetcherSession",
    "DynamicFetcher",
    "DynamicSession",
    "AsyncDynamicSession",
    "StealthyFetcher",
    "StealthySession",
    "AsyncStealthySession",
]


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module_path, class_name = _LAZY_IMPORTS[name]
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    """Support for dir() and autocomplete."""
    return sorted(list(_LAZY_IMPORTS.keys()))
