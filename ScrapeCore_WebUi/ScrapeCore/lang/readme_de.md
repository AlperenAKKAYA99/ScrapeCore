# 🕷️ ScrapeCore

> **Unsichtbare, extrem schnelle und intelligente Web-Scraping-Bibliothek für das moderne Web**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Sprachen / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <b>🇩🇪 Deutsch</b> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** ist eine Python-Web-Scraping-Bibliothek der nächsten Generation, entwickelt zur Umgehung modernster Bot-Schutzsysteme (Cloudflare Turnstile, DataDome, WAFs usw.), für ultrahochperformantes DOM-Parsing, die Live-Überwachung von Fetch/XHR-Netzwerkpaketen mit direkter Datenextraktion sowie die mühelose Durchführung asynchroner Crawling-Aufgaben in großem Maßstab.

> **Lizenz- und Fork-Hinweis:**
> Dieses Projekt wird aktiv von **Alperen AKKAYA** entwickelt und gepflegt. Die Kernarchitektur basiert auf der von Karim Shoair entwickelten Bibliothek Scrapling, die unter den Bedingungen der **BSD-3-Clause**-Lizenz unabhängig weiterentwickelt wird. Die ursprünglichen Urheberrechte bleiben uneingeschränkt gewahrt.

---

## 🚀 Hauptfunktionen

* 🛡️ **Hochentwickelte Stealth-Engine:** Naturgetreue Simulation von TLS/JA3-Fingerabdrücken und Browser-Headern über `patchright`, `curl_cffi` und `browserforge`.
* 📡 **Fetch/XHR-Netzwerküberwachung & Scraping:** Fängt alle im Hintergrund laufenden AJAX-, Fetch- und JSON-Aufrufe ab (`capture_xhr=True`) und extrahiert strukturierte Daten direkt, ohne HTML parsen zu müssen.
* 🧩 **Automatischer Cloudflare Turnstile Bypass:** Löst Turnstile-Sicherheitsprüfungen und Interstitial-Seiten vollautomatisch mit einem einzigen Flag (`solve_cloudflare=True`).
* ⚡ **Ultraschneller DOM-Parser:** Optimierte, vereinheitlichte `Selector`-Engine basierend auf `lxml` und `cssselect`, die um ein Vielfaches schneller arbeitet als BeautifulSoup.
* 🔄 **Selbstheilende (adaptive) Selektoren:** Intelligenter `relocate`-Algorithmus, der Zielelemente anhand struktureller Ähnlichkeit auch nach Website-Relaunches zuverlässig wiederfindet.
* 🕷️ **Integriertes Spider- & Crawler-Framework:** Asynchrones Crawling mit automatischer Drosselung (autothrottle), Sitzungsverwaltung, robots.txt-Konformität und Checkpoints (Pausieren/Fortsetzen).
* 🤖 **KI- und MCP-Integration:** Nativer Model Context Protocol (`scrapecore-mcp`)-Server für LLMs und KI-Agenten sowie sauberer HTML-zu-Markdown-Konverter für RAG-Pipelines.
* 💻 **Interaktive Konsole & Testlabor:** Live-REPL-Umgebung mit `scrapecore shell` und umfassendes Diagnoselabor `ScrapeCore.py`.

---

## 📦 Installation (Plattformübergreifend)

ScrapeCore ist vollständig kompatibel mit **Windows**, **Linux** (Ubuntu, Debian, CentOS, Arch usw.) und **macOS**.

### 1. Virtuelle Umgebung einrichten (Empfohlen)
Unterstützt Python 3.10 oder neuer (Empfohlen: **Python 3.13**).

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS (Bash / Zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. Browser-Binärdateien und Systembibliotheken installieren
Für dynamische und getarnte Browser (Playwright / Patchright) laden Sie die Chromium-Binärdateien herunter.

**Windows:**
```powershell
scrapecore install
# oder
playwright install chromium
```

**Linux (Ubuntu/Debian / Docker / Headless-Server):**
Auf Linux-Servern werden erforderliche GUI-/Systembibliotheken direkt mitinstalliert:
```bash
scrapecore install
# oder inklusive Systemabhängigkeiten installieren:
playwright install --with-deps chromium
```

### 4. Interaktives Test- & Diagnoselabor (`ScrapeCore.py`)
Starten Sie das integrierte Diagnoselabor, um alle Funktionen interaktiv zu testen:

**Windows:**
```powershell
python ScrapeCore.py
```

**Linux / macOS:**
```bash
python3 ScrapeCore.py
```

---

## 📖 Ausführliches Benutzerhandbuch

### 1. Schnelleinstieg (Quickstart)

```python
from scrapecore import Fetcher

# Schnelle GET-Anfrage via curl_cffi mit TLS-Impersonierung
page = Fetcher.get("https://quotes.toscrape.com")

print("Statuscode:", page.status)

# Erstes Zitat per CSS-Selektor extrahieren
first_quote = page.css("span.text::text").get()
print("Zitat:", first_quote)

# Alle Autoren auflisten
authors = page.css("small.author::text").getall()
print(f"Gefundene Autoren: {len(authors)}: {authors[:3]}")
```

---

### 2. Die Request-Engines (Fetchers-Übersicht)

ScrapeCore bietet 4 spezialisierte Fetcher für jeden Schwierigkeitsgrad:

| Engine | Grundlage | Verwendungszweck | JavaScript? | Bot-Schutz |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | Statisches HTML, REST-APIs, Höchstgeschwindigkeit | ❌ | Mittel (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | Hochparallele asynchrone Anfragen | ❌ | Mittel (TLS/JA3) |
| `DynamicFetcher` | `playwright` | Single Page Apps (SPA), dynamische JS-Seiten | ✅ | Standard |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome und strenge WAFs | ✅ | **Maximal (Unsichtbar)** |

#### A. Schnelle statische Anfragen (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Synchrone Anfrage
res = Fetcher.get("https://httpbin.org/headers", headers={"X-Header": "Wert"})
print(res.json())

# Asynchrone Anfrage
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. JavaScript-Rendering (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Warten, bis die Netzwerkaktivität abklingt
)

print(page.css("span.text::text").get())
```

#### C. Umgehung von Bot-Schutz und Cloudflare (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Cloudflare-geschützte Demoseite
    solve_cloudflare=True,              # Turnstile automatisch lösen
    headless=True,                      # Im Hintergrund ausführen
    block_ads=True,                     # Über 3500 Werbe- und Tracker-Domains blockieren
    disable_resources=True,             # Bilder und Schriftarten überspringen (3x schneller)
    timeout=60000                       # 60 Sekunden Timeout
)

print("Zugriff erfolgreich! Titel:", page.css("h1::text").get())
```

#### D. In-Page-Automatisierung (`page_action`)

```python
from scrapecore import StealthyFetcher

def unendliches_scrollen(page):
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=unendliches_scrollen
)
```

---

### 3. Datenextraktion & Selektoren

Jeder Fetcher liefert ein einheitliches **`Response`**-Objekt zurück, das von `Selector` erbt.

#### CSS- und XPath-Selektoren
```python
# Einzelnen Text extrahieren
title = page.css("h1.main-title::text").get()

# Liste von Attributen extrahieren
links = page.css("div.menu a::attr(href)").getall()

# Vollständiger XPath-Support
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### Element-Suche im BeautifulSoup-Stil (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

buttons = page.find_all("button", type="submit")
for btn in buttons:
    print(btn.attrib.get("id"))
```

#### Intelligente Textbereinigung (`clean_text`)
```python
node = page.css("div.description").first
print(node.clean_text())
```

#### Selbstheilende (adaptive) Selektoren
```python
# Strukturellen Fingerabdruck in lokaler SQLite-Datenbank speichern
page.css("button.kaufen", adaptive=True, auto_save=True)

# Selbst wenn sich der Klassenname ändert, findet ScrapeCore das Element wieder
button = page.css("button.kaufen", adaptive=True)
```

---

### 4. Fetch/XHR-Netzwerküberwachung & Paket-Scraping

Moderne Webanwendungen stellen Daten selten in statischem HTML bereit, sondern laden strukturierte JSON-APIs asynchron über AJAX-, Fetch- und XHR-Aufrufe im Hintergrund. Das direkte Abfangen dieser Pakete ist **viel schneller, ausfallsicherer und liefert saubere JSON-Daten**.

#### A. Einfache Überwachung (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Aktiviert das Abfangen von Netzwerkpaketen
)

print(f"Abgefangene Pakete: {len(page.captured_xhr)}")
print(f"Erfasste URLs: {page.xhr_urls}")
```

#### B. Gezielte Filterung mit Regex oder Callables

```python
# 1. Regex-Filter für bestimmte Endpunkte:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Eigene Filterfunktion:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. XHR-Abfragemethoden auf `Response`

| Eigenschaft / Methode | Beschreibung |
| :--- | :--- |
| `page.captured_xhr` | Liste aller abgefangenen `Response`-Objekte von XHR/Fetch |
| `page.xhr_urls` | Liste aller abgefangenen URL-Strings (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Liefert das **erste** passende Paket (oder `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Liefert **alle** passenden Pakete (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | Parst den Inhalt des ersten Treffers direkt als JSON |
| `xhr.post_data` / `xhr.request_data` | Vom Client übermittelte POST-Payload / Formulardaten |
| `xhr.resource_type` | Playwright-Ressourcentyp (`"xhr"` oder `"fetch"`) |
| `xhr.method` | HTTP-Methode (`"GET"`, `"POST"` etc.) |

#### Beispiel: JSON-Daten direkt aus abgefangener API extrahieren

```python
# JSON-Antwort direkt ohne HTML-Parsing verarbeiten
products_json = page.xhr_json(r"/api/products\?category=electronics")
if products_json:
    for item in products_json.get("items", []):
        print(item["name"], item["price"])

# Abgefangene POST-Anfragen inspizieren
post_requests = page.filter_xhr(method="POST", status=200)
for req in post_requests:
    print(f"POST URL: {req.url}")
    print(f"Gesendete Payload: {req.post_data}")
    print(f"Server-Antwort (JSON): {req.json()}")
```

#### D. Nutzung über CLI und Testlabor

```powershell
# XHR-Pakete über die CLI mitschneiden:
scrapecore extract fetch "https://quotes.toscrape.com/js/" output.html --capture-xhr

# Live-Test im interaktiven Labor:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Großflächiges Crawling: Spiders-Framework

```python
from scrapecore.spiders import Spider, Request

class BookSpider(Spider):
    name = "buch_spider"
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
    print(f"{len(result.items)} Bücher gesammelt!")
```

---

### 6. Sitzungsverwaltung & Proxy-Rotation

```python
from scrapecore.fetchers import FetcherSession, ProxyRotator

rotator = ProxyRotator([
    "http://user:pass@proxy1.com:8000",
    "http://user:pass@proxy2.com:8000",
])

session = FetcherSession(proxy=rotator)
session.post("https://example.com/login", data={"user": "admin", "pass": "geheim"})

dashboard = session.get("https://example.com/dashboard")
print(dashboard.css("h2::text").get())
```

---

### 7. Künstliche Intelligenz & MCP-Server

```powershell
# MCP-Server im Stdio-Modus starten
scrapecore-mcp

# Oder als HTTP-Stream bereitstellen
scrapecore-mcp --http --port 8000
```

#### Sauberes Markdown für RAG-Pipelines erstellen
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o nachrichten.md
```

---

### 8. Befehlszeilenschnittstelle (CLI-Handbuch)

#### Interaktive Shell (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### Direkter Datei-Export (`scrapecore extract`)
```powershell
# CSS-Selektor in Datei speichern
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o zitate.txt

# Stealth-Browser mit Cloudflare-Bypass
scrapecore extract stealthy-fetch "https://zielseite.com" --solve-cloudflare -o seite.html
```

---

## 📁 Projektstruktur

```
ScrapeCore/
│
├── lang/                       # Mehrsprachige Dokumentation
│   ├── readme_en.md            # Englisch
│   ├── readme_es.md            # Spanisch
│   ├── readme_pt-br.md         # Portugiesisch (Brasilien)
│   ├── readme_zh.md            # Vereinfachtes Chinesisch
│   ├── readme_ja.md            # Japanisch
│   ├── readme_de.md            # Deutsch
│   ├── readme_fr.md            # Französisch
│   ├── readme_ru.md            # Russisch
│   ├── readme_ko.md            # Koreanisch
│   └── readme_ar.md            # Arabisch
│
├── scrapecore/                 # Quellcode der Bibliothek
├── tests/                      # Testsuite
├── .venv/                      # Virtuelle Python 3.13-Umgebung
├── pyproject.toml              # Paket- und Build-Konfiguration
├── requirements.txt            # Projektabhängigkeiten
├── LICENSE                     # BSD-3-Lizenz (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # Interaktives Diagnoselabor
└── README.md                   # Hauptdokumentation (Türkisch)
```

---

## 🙏 Danksagung & Anerkennung

Dieses Projekt baut auf der herausragenden Arbeit von **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))** auf, dem Schöpfer der **[Scrapling](https://github.com/D4Vinci/Scrapling)**-Bibliothek.

* **Ursprüngliches Repository:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Ursprünglicher Autor:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Ursprüngliche Lizenz:** BSD 3-Clause License

Wir danken Karim Shoair und der Open-Source-Community herzlich für die Bereitstellung dieser wegweisenden Architektur. ScrapeCore führt diese Basis mit unabhängiger Weiterentwicklung fort.

---

## ⚖️ Lizenz

Dieses Projekt ist unter der **BSD 3-Clause License** lizenziert:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

Weitere Informationen finden Sie in der Datei [LICENSE](../LICENSE).
