# 🕷️ ScrapeCore

> **현대적인 웹 환경을 위한 스텔스, 초고속, 지능형 웹 스크래핑 라이브러리**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 언어 / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <b>🇰🇷 한국어</b> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore**는 현대 웹사이트의 고도화된 봇 차단 시스템(Cloudflare Turnstile, DataDome, WAF 등)을 완벽하게 우회하고, 초고속 DOM 파싱, 실시간 Fetch/XHR 네트워크 패킷 감시 및 직접 데이터 추출, 그리고 대규모 비동기 크롤링을 간편하게 수행할 수 있도록 설계된 차세대 파이썬(Python) 웹 스크래핑 라이브러리입니다.

> **라이선스 및 포크(Fork) 안내:**
> 본 프로젝트는 **Alperen AKKAYA**에 의해 적극적으로 개발 및 유지 관리되고 있습니다. 핵심 아키텍처는 Karim Shoair가 개발한 Scrapling 라이브러리를 기반으로 하며, **BSD-3-Clause** 라이선스 조건에 따라 원작자의 저작권을 온전히 보존하며 독립적으로 포크되어 발전하고 있습니다.

---

## 🚀 주요 핵심 기능

* 🛡️ **첨단 스텔스 엔진 (Stealth Engine):** `patchright`, `curl_cffi`, `browserforge`를 결합하여 실제 브라우저의 TLS/JA3 핑거프린트와 헤더를 사실적으로 시뮬레이션합니다.
* 📡 **Fetch/XHR 네트워크 패킷 감시 및 스크래핑:** 브라우저 백그라운드에서 발생하는 모든 AJAX, Fetch, JSON 호출을 가로채(`capture_xhr=True`) HTML 파싱 없이 구조화된 데이터를 즉시 추출합니다.
* 🧩 **Cloudflare Turnstile 자동 우회:** 단 하나의 파라미터(`solve_cloudflare=True`)로 턴스타일(Turnstile) 및 챌린지 대기 화면을 전자동으로 통과합니다.
* ⚡ **초고속 DOM 파서:** `lxml` 및 `cssselect`를 기반으로 최적화된 통합 `Selector` 엔진을 제공하여 BeautifulSoup 대비 월등한 처리 속도를 자랑합니다.
* 🔄 **자가 치유형 적응형 선택자 (Adaptive Selectors):** 사이트 레이아웃이나 클래스명이 변경되더라도 구조적 유사성 알고리즘을 통해 대상을 재탐색하는 스마트 `relocate` 메커니즘을 지원합니다.
* 🕷️ **내장 Spider 및 크롤러 프레임워크:** 자동 속도 조절(autothrottle), 세션 관리, robots.txt 준수 및 일시정지/재개(체크포인트)를 갖춘 완전 비동기 크롤러를 제공합니다.
* 🤖 **AI 및 MCP (Model Context Protocol) 지원:** LLM 및 AI 에이전트를 위한 내장 `scrapecore-mcp` 서버와 RAG 파이프라인 구축을 위한 고품질 HTML-to-Markdown 변환 기능을 탑재했습니다.
* 💻 **대화형 콘솔 및 테스트 랩:** 실시간 REPL 환경인 `scrapecore shell` 및 종합 진단 도구인 `ScrapeCore.py`를 제공합니다.

---

## 📦 설치 안내 (크로스 플랫폼)

ScrapeCore는 **Windows**, **Linux** (Ubuntu, Debian, CentOS, Arch 등), **macOS** 환경을 완벽하게 지원합니다.

### 1. 가상환경 구성 (권장)
Python 3.10 이상을 지원합니다 (권장 버전: **Python 3.13**).

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

### 2. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 브라우저 바이너리 및 시스템 의존성 설치
동적 및 스텔스 브라우저(Playwright / Patchright) 구동을 위한 Chromium 바이너리와 필수 라이브러리를 설치합니다.

**Windows:**
```powershell
scrapecore install
# 또는
playwright install chromium
```

**Linux (Ubuntu/Debian / Docker / 헤드리스 서버):**
Linux 서버 환경에서는 필수 공유 라이브러리를 함께 설치할 수 있습니다:
```bash
scrapecore install
# 또는 시스템 패키지를 포함하여 설치:
playwright install --with-deps chromium
```

### 4. 대화형 테스트 랩 (`ScrapeCore.py`)
모든 핵심 기능을 콘솔에서 직접 체험하고 테스트할 수 있습니다:

**Windows:**
```powershell
python ScrapeCore.py
```

**Linux / macOS:**
```bash
python3 ScrapeCore.py
```

---

## 📖 종합 사용 가이드

### 1. 빠른 시작 (Quickstart)

```python
from scrapecore import Fetcher

# curl_cffi 기반 브라우저 TLS 위장을 통한 빠른 GET 요청
page = Fetcher.get("https://quotes.toscrape.com")

print("상태 코드:", page.status)

# CSS 선택자로 첫 번째 인용구 텍스트 추출
first_quote = page.css("span.text::text").get()
print("인용구:", first_quote)

# 전체 작가 목록 추출
authors = page.css("small.author::text").getall()
print(f"발견된 작가 수: {len(authors)}명: {authors[:3]}")
```

---

### 2. 요청 엔진 가이드 (Fetchers)

ScrapeCore는 대상 사이트의 동적 수준과 보안 강도에 맞춰 4가지 요청 엔진을 제공합니다:

| 엔진 | 기반 | 용도 | JavaScript 지원 | 봇 차단 대응력 |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | 정적 HTML, REST API, 최고 속도 | ❌ | 보통 (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | 대량의 비동기 동시 요청 | ❌ | 보통 (TLS/JA3) |
| `DynamicFetcher` | `playwright` | 단일 페이지 앱(SPA), JS 렌더링 사이트 | ✅ | 표준 |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome 및 엄격한 방화벽 | ✅ | **최상 (완전 은폐)** |

#### A. 고속 정적 요청 (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# 동기 요청
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Value"})
print(res.json())

# 비동기 요청
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. JavaScript 렌더링 동적 요청 (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # 네트워크 통신이 안정화될 때까지 대기
)

print(page.css("span.text::text").get())
```

#### C. Cloudflare 우회 및 고급 스텔스 (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Cloudflare 보안 적용 데모 사이트
    solve_cloudflare=True,              # 턴스타일 챌린지 자동 해결
    headless=True,                      # 백그라운드 무두 실행
    block_ads=True,                     # 3500개 이상의 광고 및 트래커 도메인 차단
    disable_resources=True,             # 이미지, 폰트 등을 생략하여 300% 속도 향상
    timeout=60000                       # 60초 타임아웃
)

print("접속 성공! 제목:", page.css("h1::text").get())
```

#### D. 페이지 내 자동화 동작 (`page_action`)

```python
from scrapecore import StealthyFetcher

def 무한_스크롤(page):
    # 페이지를 아래로 3회 스크롤
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=무한_스크롤
)
```

---

### 3. 데이터 파싱 및 선택자 (Selectors)

모든 요청 결과는 `Selector`의 모든 기능을 즉시 사용할 수 있는 **`Response`** 객체로 반환됩니다.

#### CSS 및 XPath 선택자
```python
# 단일 텍스트 추출
title = page.css("h1.main-title::text").get()

# 속성 목록 추출
links = page.css("div.menu a::attr(href)").getall()

# 완전한 XPath 지원
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### BeautifulSoup 스타일 탐색 (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

buttons = page.find_all("button", type="submit")
for btn in buttons:
    print(btn.attrib.get("id"))
```

#### 스마트 텍스트 정제 (`clean_text`)
```python
node = page.css("div.description").first
print(node.clean_text())
```

#### 자가 치유형 선택자 (Adaptive Selectors)
```python
# 로컬 SQLite DB에 요소의 구조적 지문 저장
page.css("button.buy-now", adaptive=True, auto_save=True)

# 향후 사이트 개편으로 클래스명이 바뀌어도 요소를 자동 재탐색
button = page.css("button.buy-now", adaptive=True)
```

---

### 4. Fetch/XHR 네트워크 패킷 감시 및 직접 스크래핑

최신 웹사이트들은 정적 HTML 대신 백그라운드 API 호출을 통해 JSON 데이터를 동적으로 수신합니다. 이 네트워크 패킷을 가로채면 **HTML 파싱 과정 없이 훨씬 빠르고 안정적으로 순수 JSON 데이터를 확보**할 수 있습니다.

#### A. 기본 캡처 (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # 네트워크 패킷 가로채기 활성화
)

print(f"가로챈 패킷 수: {len(page.captured_xhr)}")
print(f"가로챈 URL 목록: {page.xhr_urls}")
```

#### B. 정규식 또는 사용자 정의 함수 기반 필터링

```python
# 1. 정규표현식 문자열로 대상 API 필터링:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. 사용자 지정 함수를 통한 정밀 필터링:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. `Response` 객체의 XHR 조회 및 조작 메서드

| 프로퍼티 / 메서드 | 설명 |
| :--- | :--- |
| `page.captured_xhr` | 가로챈 모든 XHR/Fetch `Response` 객체 리스트 |
| `page.xhr_urls` | 가로챈 모든 요청의 URL 문자열 리스트 (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | 조건에 부합하는 **첫 번째** 패킷 반환 (없으면 `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | 조건에 부합하는 **모든** 패킷 리스트 반환 (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | 첫 번째 일치 패킷의 바디를 즉시 JSON으로 파싱하여 반환 |
| `xhr.post_data` / `xhr.request_data` | 클라이언트가 전송한 POST 페이로드/요청 본문 |
| `xhr.resource_type` | Playwright 리소스 유형 (`"xhr"` 또는 `"fetch"`) |
| `xhr.method` | HTTP 메서드 (`"GET"`, `"POST"` 등) |

#### 예제: 가로챈 API로부터 순수 JSON 데이터 즉시 추출

```python
# HTML 파싱 없이 API JSON 응답 직접 획득
products_json = page.xhr_json(r"/api/products\?category=electronics")
if products_json:
    for item in products_json.get("items", []):
        print(item["name"], item["price"])

# 가로챈 POST 요청 및 전송된 파라미터 확인
post_requests = page.filter_xhr(method="POST", status=200)
for req in post_requests:
    print(f"POST 주소: {req.url}")
    print(f"전송 데이터: {req.post_data}")
    print(f"서버 응답 JSON: {req.json()}")
```

#### D. CLI 명령어 및 테스트 랩 활용

```powershell
# CLI 명령어를 통해 XHR 패킷을 가로채며 페이지 저장:
scrapecore extract fetch "https://quotes.toscrape.com/js/" output.html --capture-xhr

# 대화형 테스트 랩에서 즉시 실시간 검증:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. 대규모 크롤링: Spiders 프레임워크

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
    print(f"총 {len(result.items)}권의 도서 데이터를 수집했습니다!")
```

---

### 6. 세션 관리 및 프록시 순환

```python
from scrapecore.fetchers import FetcherSession, ProxyRotator

rotator = ProxyRotator([
    "http://user:pass@proxy1.com:8000",
    "http://user:pass@proxy2.com:8000",
])

session = FetcherSession(proxy=rotator)
session.post("https://example.com/login", data={"user": "admin", "pass": "secret"})

dashboard = session.get("https://example.com/dashboard")
print(dashboard.css("h2::text").get())
```

---

### 7. 인공지능 및 MCP 서버 (Model Context Protocol)

```powershell
# stdio 모드로 MCP 서버 구동
scrapecore-mcp

# HTTP 스트리밍 네트워크 모드로 구동
scrapecore-mcp --http --port 8000
```

#### RAG 파이프라인 구축을 위한 마크다운(Markdown) 자동 변환
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o news.md
```

---

### 8. 명령줄 인터페이스 (CLI 안내)

#### 대화형 스크래핑 쉘 (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### 파일로 직접 데이터 추출 (`scrapecore extract`)
```powershell
# CSS 선택자 결과를 텍스트 파일로 저장
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o quotes.txt

# 스텔스 브라우저 및 Cloudflare 우회 추출
scrapecore extract stealthy-fetch "https://target-site.com" --solve-cloudflare -o page.html
```

---

## 📁 디렉터리 구성

```
ScrapeCore/
│
├── lang/                       # 다국어 설명서 디렉터리
│   ├── readme_en.md            # 영어
│   ├── readme_es.md            # 스페인어
│   ├── readme_pt-br.md         # 포르투갈어 (브라질)
│   ├── readme_zh.md            # 중국어 (간체)
│   ├── readme_ja.md            # 일본어
│   ├── readme_de.md            # 독일어
│   ├── readme_fr.md            # 프랑스어
│   ├── readme_ru.md            # 러시아어
│   ├── readme_ko.md            # 한국어
│   └── readme_ar.md            # 아랍어
│
├── scrapecore/                 # 핵심 라이브러리 소스코드
├── tests/                      # 단위 및 통합 테스트 슈트
├── .venv/                      # Python 3.13 가상환경
├── pyproject.toml              # 패키징 설정
├── requirements.txt            # 설치 종속 항목
├── LICENSE                     # BSD-3 라이선스 (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # 대화형 테스트 랩 및 진단기
└── README.md                   # 기본 설명서 (한국어/다국어 허브)
```

---

## 🙏 감사의 글 및 원작자 표기 (Credits)

본 프로젝트는 **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))** 님이 제작한 뛰어난 오픈소스 라이브러리인 **[Scrapling](https://github.com/D4Vinci/Scrapling)**에 뿌리를 두고 있습니다.

* **원작 저장소:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **원작자:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **원작 라이선스:** BSD 3-Clause License

혁신적인 스텔스 구조와 우수한 아키텍처를 공개해 주신 Karim Shoair 님과 오픈소스 커뮤니티에 진심으로 감사드립니다. ScrapeCore는 이 토대 위에서 독립적인 기능 확장과 현대화를 이어가고 있습니다.

---

## ⚖️ 라이선스

본 프로젝트는 **BSD 3-Clause License** 하에 제공됩니다:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

자세한 내용은 [LICENSE](../LICENSE) 파일을 참고하십시오.
