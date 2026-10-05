# 🕷️ ScrapeCore

> **Stealthy, Fast, and Intelligent Web Scraping Library for the Modern Web**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Languages / Diller:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <b>🇬🇧 English</b> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** is a next-generation Python web scraping library engineered to bypass modern bot protection systems (Cloudflare Turnstile, DataDome, WAFs, etc.), perform ultra-high-performance DOM parsing, monitor background Fetch/XHR network packets, and effortlessly execute large-scale asynchronous crawling.

> **License & Fork Notice:**
> This project is actively developed and maintained by **Alperen AKKAYA**. The core architecture is based on the Scrapling library created by Karim Shoair, forked and independently maintained under the terms of the **BSD-3-Clause** license with original copyrights fully honored.

---

## 🚀 Key Features

* 🛡️ **Advanced Stealth Engine:** Realistic TLS/JA3 fingerprint and browser header simulation via `patchright`, `curl_cffi`, and `browserforge`.
* 📡 **Fetch/XHR Network Monitoring & Scraping:** Intercept all background API, JSON, and AJAX network requests (`capture_xhr=True`) and directly extract structured data without parsing HTML.
* 🧩 **Automatic Cloudflare Turnstile Bypass:** Solve Turnstile and interstitial security verification screens automatically with a single flag (`solve_cloudflare=True`).
* ⚡ **Ultra-Fast DOM Parser:** Unified `Selector` engine optimized over `lxml` and `cssselect`, performing significantly faster than BeautifulSoup.
* 🔄 **Self-Healing (Adaptive) Selectors:** Smart `relocate` algorithm capable of re-finding elements using structural similarity even after website layout updates.
* 🕷️ **Built-in Spider & Crawler Framework:** Async crawling with autothrottle, session management, robots.txt compliance, and pause/resume checkpointing.
* 🤖 **AI & MCP Ready:** Built-in Model Context Protocol (`scrapecore-mcp`) server for LLMs/AI agents and clean HTML-to-Markdown conversion for RAG pipelines.
* 💻 **Interactive Playground & Shell:** Live REPL environment via `scrapecore shell` and test suite `ScrapeCore.py`.

---

## 📦 Installation & Platform Compatibility (Windows & Linux / macOS)

ScrapeCore is 100% cross-platform and fully compatible with **Windows**, **Linux** (Ubuntu, Debian, Fedora, Arch, CentOS, etc.), and **macOS**. Supports Python 3.10 and newer (Recommended: **Python 3.13**).

### 1. Setup Virtual Environment

**🪟 Windows (PowerShell / CMD):**
```powershell
# Create virtual environment
python -m venv .venv

# Activate on PowerShell
.\.venv\Scripts\Activate.ps1

# (If using CMD)
.\.venv\Scripts\activate.bat
```

**🐧 Linux & 🍎 macOS (Bash / Zsh):**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

---

### 2. Install Dependencies

Install all core engines, browser automation tools, and AI components:

**Windows & Linux:**
```bash
pip install -r requirements.txt
```

---

### 3. Install Browser Binaries & System Libraries

Install Chromium binaries required for dynamic rendering and stealth browser engines (`Playwright` / `Patchright`):

**🪟 Windows:**
```powershell
scrapecore install
# or
playwright install chromium
```

**🐧 Linux (Servers, Docker & Distributions):**
> 💡 *On headless Linux servers (Ubuntu/Debian, etc.), Chromium requires OS shared libraries to run in headless mode. Install them alongside the browser:*
```bash
# Install Chromium with required OS libraries
playwright install --with-deps chromium
# or via built-in command
scrapecore install
```

---

### 4. Interactive Test & Playground (`ScrapeCore.py`)

Run the comprehensive diagnostics and experimentation lab to test all features:

**🪟 Windows:**
```powershell
python ScrapeCore.py
```

**🐧 Linux & 🍎 macOS:**
```bash
python3 ScrapeCore.py
```
*(View command-line flags: `python3 ScrapeCore.py --help`)*

---

## 📖 Comprehensive User Guide

### 1. Quickstart

```python
from scrapecore import Fetcher

# Fast GET request using curl_cffi with TLS impersonation
page = Fetcher.get("https://quotes.toscrape.com")

print("Status Code:", page.status)

# Extract first quote text using CSS selector
first_quote = page.css("span.text::text").get()
print("Quote:", first_quote)

# List all authors on the page
authors = page.css("small.author::text").getall()
print(f"Found {len(authors)} authors: {authors[:3]}")
```

---

### 2. Request Engines (Fetchers Guide)

ScrapeCore provides 4 specialized fetcher engines tailored to your target website's complexity:

| Engine | Under the Hood | Best For | JavaScript? | Bot Protection |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | Static HTML, REST APIs, maximum speed | ❌ | Moderate (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | High-concurrency asynchronous scraping | ❌ | Moderate (TLS/JA3) |
| `DynamicFetcher` | `playwright` | Single Page Apps (SPA), JavaScript-heavy sites | ✅ | Standard |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome, advanced bot blockers | ✅ | **Maximum (Undetectable)** |

#### A. Fast Static Requests (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Synchronous request with custom headers
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Value"})
print(res.json())

# Asynchronous batch request
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. JavaScript Rendered Pages (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

# Render page after client-side JavaScript execution
page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Wait until network activity settles
)

print(page.css("span.text::text").get())
```

#### C. Advanced Anti-Bot & Cloudflare Bypass (`StealthyFetcher`)

`StealthyFetcher` mimics human browser footprints and solves Cloudflare Turnstile screens automatically:

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Cloudflare-protected demo site
    solve_cloudflare=True,              # Automatically solve Turnstile challenge
    headless=True,                      # Run headless (set False to view browser)
    block_ads=True,                     # Block 3500+ ad and tracker domains
    disable_resources=True,             # Skip images, fonts, media for ~300% speed boost
    timeout=60000                       # 60s timeout
)

print("Access successful! Title:", page.css("h1::text").get())
```

#### D. In-Page Automation (`page_action`)
Perform clicks, form submissions, or infinite scrolling directly through the Playwright `page` instance:

```python
from scrapecore import StealthyFetcher

def infinite_scroll(page):
    # Scroll down 3 times
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=infinite_scroll
)
```

---

### 3. Parsing Data & Selectors

Every fetcher returns a unified **`Response`** object that inherits directly from `Selector`.

#### CSS and XPath Selectors
```python
# Single text extraction with CSS
title = page.css("h1.main-title::text").get()

# Extract attribute list
links = page.css("div.menu a::attr(href)").getall()

# Full XPath support
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### BeautifulSoup-Style Finding (`find` & `find_all`)
```python
# Find first matching element
header = page.find("h1", class_="title")
print(header.text)

# Find all matching elements
all_buttons = page.find_all("button", type="submit")
for btn in all_buttons:
    print(btn.attrib.get("id"))
```

#### Clean Text Helper (`clean_text`)
Automatically strips excessive whitespace, newlines, and unescapes HTML entities:
```python
dirty_div = page.css("div.description").first
print(dirty_div.clean_text())
```

#### Self-Healing (Adaptive) Selectors
Prevents broken scrapers when websites update their CSS classes or DOM structure:
```python
# Save structural fingerprint to local SQLite database
page.css("button.buy-now", adaptive=True, auto_save=True)

# Later, even if the class changes, ScrapeCore relocates the element
target_button = page.css("button.buy-now", adaptive=True)
```

---

### 4. Fetch/XHR Network Monitoring & Scraping (Network Traffic Capture)

Modern web applications and Single Page Applications (SPAs) rarely load all data inside static HTML; they fetch structured JSON APIs via background AJAX, Fetch, and XHR requests. Capturing these network packets is **faster, more reliable, and yields clean structured data** without tedious HTML parsing.

Both `DynamicFetcher` and `StealthyFetcher` can intercept and capture network packets as first-class `Response` objects.

#### A. Basic Capture (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Enables network packet capture
)

print(f"Captured network requests: {len(page.captured_xhr)}")
print(f"Captured URLs: {page.xhr_urls}")
```

#### B. Targeted Filtering with Regex or Callables

```python
# 1. Regex string filter:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Custom callable filter:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. `Response` Methods for XHR Querying

| Property / Method | Description |
| :--- | :--- |
| `page.captured_xhr` | List of captured XHR/Fetch `Response` objects |
| `page.xhr_urls` | List of all captured request URLs (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Returns the **first** matching packet (or `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Returns **all** matching packets (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | Parses matching packet body as JSON directly |
| `xhr.post_data` / `xhr.request_data` | Request payload/POST body sent by client |
| `xhr.resource_type` | Playwright resource type (`"xhr"` or `"fetch"`) |
| `xhr.method` | HTTP method (`"GET"`, `"POST"`, etc.) |

#### Example: Extracting JSON Data Directly from Intercepted API

```python
# Intercept and decode API JSON response directly
products_data = page.xhr_json(r"/api/products\?category=electronics")
if products_data:
    for item in products_data.get("items", []):
        print(item["name"], item["price"])

# Inspect intercepted POST requests and their payloads
post_requests = page.filter_xhr(method="POST", status=200)
for req in post_requests:
    print(f"POST URL: {req.url}")
    print(f"Payload sent: {req.post_data}")
    print(f"JSON response: {req.json()}")
```

#### D. CLI & Playground Usage

```powershell
# Intercept XHR packets from terminal CLI:
scrapecore extract fetch "https://quotes.toscrape.com/js/" output.html --capture-xhr

# Test live XHR capture in interactive playground:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Large-Scale Crawling: Spiders Framework

```python
from scrapecore.spiders import Spider, Request

class BookSpider(Spider):
    name = "book_crawler"
    start_urls = ["https://books.toscrape.com/"]
    
    autothrottle_enabled = True
    concurrent_requests = 4

    async def parse(self, response):
        for book in response.css("article.product_pod"):
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield Request(url=response.urljoin(next_page), callback=self.parse)

if __name__ == "__main__":
    spider = BookSpider()
    result = spider.start()
    print(f"Scraped {len(result.items)} books!")
```

---

### 6. Session Management & Proxy Rotation

```python
from scrapecore.fetchers import FetcherSession, ProxyRotator

# Define rotating proxy pool
rotator = ProxyRotator([
    "http://user:pass@proxy1.com:8000",
    "http://user:pass@proxy2.com:8000",
])

# Initialize stateful session
session = FetcherSession(proxy=rotator)

# Authenticate
session.post("https://example.com/login", data={"user": "admin", "pass": "secret"})

# Access authenticated dashboard
dashboard = session.get("https://example.com/dashboard")
print(dashboard.css("h2::text").get())
```

---

### 7. AI & MCP (Model Context Protocol)

Run ScrapeCore as a Model Context Protocol server for Claude Desktop, Cursor, or autonomous LLM agents:

```powershell
# Start stdio MCP server
scrapecore-mcp

# Or start streaming HTTP server
scrapecore-mcp --http --port 8000
```

#### Clean HTML to Markdown for RAG Pipelines
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o hacker_news.md
```

---

### 8. Command-Line Interface (CLI Guide)

#### Interactive Scraping Shell (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```
*The shell launches with `page`, `Fetcher`, and `Selector` preloaded:*
```python
In [1]: page.css("span.text::text").get()
Out[1]: '“The world as we have created it is a process of our thinking...”'
```

#### Extract Data Directly to File (`scrapecore extract`)
```powershell
# Extract CSS selector and save to file
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o quotes.txt

# Extract with stealth browser and Cloudflare bypass
scrapecore extract stealthy-fetch "https://target-site.com" --solve-cloudflare -o page.html
```

---

## 📁 Project Directory Structure

```
ScrapeCore/
│
├── lang/                       # Multi-language documentation
│   ├── readme_en.md            # English
│   ├── readme_es.md            # Español
│   ├── readme_pt-br.md         # Português (Brasil)
│   ├── readme_zh.md            # 简体中文
│   ├── readme_ja.md            # 日本語
│   ├── readme_de.md            # Deutsch
│   ├── readme_fr.md            # Français
│   ├── readme_ru.md            # Русский
│   ├── readme_ko.md            # 한국어
│   └── readme_ar.md            # العربية
│
├── scrapecore/                 # Core library source code
│   ├── core/                   # DOM engine, storage, typing, AI/MCP utilities
│   ├── engines/                # Browser engines, stealth patches, convertors
│   ├── fetchers/               # Fetcher, AsyncFetcher, DynamicFetcher, StealthyFetcher
│   ├── parser/                 # lxml Selector engine & adaptive algorithms
│   ├── spiders/                # Asynchronous spider framework & presets
│   └── cli.py                  # CLI tools (scrapecore, scrapecore-mcp)
│
├── tests/                      # Unit and integration test suites
├── .venv/                      # Python 3.13 virtual environment
├── pyproject.toml              # Packaging and dependency specifications
├── requirements.txt            # Project installation dependencies
├── LICENSE                     # BSD-3 License (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # Interactive Playground & Diagnostics Lab
└── README.md                   # Primary Documentation (Turkish)
```

---

## 🙏 Acknowledgements & Credits

This project is built upon the foundational work of **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))**, creator of the exceptional **[Scrapling](https://github.com/D4Vinci/Scrapling)** library.

* **Upstream Repository:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Original Author:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Original License:** BSD 3-Clause License

We express our gratitude to Karim Shoair and the open-source community for developing this innovative architecture and stealth mechanics. ScrapeCore continues this lineage with independent development, new feature additions, and ongoing modernization.

---

## ⚖️ License

This project is licensed under the **BSD 3-Clause License**:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

See [LICENSE](../LICENSE) for complete details.
