"""
Compatibility layer for legacy imports: 'import scrapling' -> 'import scrapecore'
"""
import sys
import scrapecore

# Forward all attributes and module references
sys.modules["scrapling"] = scrapecore
from scrapecore import *
from scrapecore import __version__, __author__, __copyright__
