"""Integrations with third-party frameworks.

Each integration lives in its own module and is imported explicitly, so its
framework never becomes a required dependency of ScrapeCore. Example::

    from scrapecore.integrations.scrapy import scrapecore_response
"""
