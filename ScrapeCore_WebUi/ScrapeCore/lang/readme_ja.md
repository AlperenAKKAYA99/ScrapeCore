# 🕷️ ScrapeCore

> **モダンWebのためのステルス・高速・高機能Webスクレイピングライブラリ**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 言語 / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <b>🇯🇵 日本語</b> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** は、現代のWebサイトにおける高度なボット対策（Cloudflare Turnstile、DataDome、WAFなど）を突破し、極めて高速なDOM解析を実行、バックグラウンドのFetch/XHR通信を監視・直接データ抽出し、大規模な非同期クローリングを容易に実現する次世代のPython Webスクレイピングライブラリです。

> **ライセンスとフォークに関する告知 (Fork Notice):**
> 本プロジェクトは **Alperen AKKAYA** によって開発・保守されています。コアアーキテクチャは Karim Shoair 氏が開発した Scrapling ライブラリをベースにしており、**BSD-3-Clause** ライセンス規約に則ってフォーク・独立開発され、オリジナルの著作権を尊重して継承されています。

---

## 🚀 主な機能

* 🛡️ **高度なステルスエンジン (Stealth Engine):** `patchright`、`curl_cffi`、`browserforge` によるリアルなTLS/JA3フィンガープリントおよびブラウザヘッダーシミュレーション。
* 📡 **Fetch/XHR 通信監視・スクレイピング機能:** ブラウザがバックグラウンドで行うすべてのAPI、JSON、AJAX通信を捕捉（`capture_xhr=True`）し、HTMLをパースすることなく直接構造化データを取得可能。
* 🧩 **Cloudflare Turnstile 自動突破:** 単一のパラメータ（`solve_cloudflare=True`）でTurnstile認証画面や待機画面を自動的に解決。
* ⚡ **超高速DOMパーサー:** `lxml` と `cssselect` をベースに高度に最適化された統一 `Selector` エンジン。BeautifulSoupを遥かに凌駕する処理速度。
* 🔄 **自己修復（適応型）セレクター (Adaptive Selectors):** サイトのデザインや構造が変更された場合でも、類似性解析によって対象要素を再検出するインテリジェントな `relocate` メカニズム。
* 🕷️ **組み込みSpider・Crawlerフレームワーク:** 自動レート制御（autothrottle）、セッション管理、robots.txt準拠、チェックポイント（中断・再開）機能を完備。
* 🤖 **AIおよびMCPネイティブ対応:** LLMやAIエージェントがWeb検索・抽出を行える Model Context Protocol（`scrapecore-mcp`）サーバーおよびRAG向けHTML-Markdownコンバーター。
* 💻 **対話型シェル・実験ラボ:** ライブREPL環境 `scrapecore shell` および総合テストスイート `ScrapeCore.py`。

---

## 📦 インストール方法 (クロスプラットフォーム)

ScrapeCoreは **Windows**、**Linux** (Ubuntu, Debian, CentOS, Arch など)、**macOS** に完全対応しています。

### 1. 仮想環境の準備 (推奨)
Python 3.10以降をサポート（推奨: **Python 3.13**）。

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

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. ブラウザバイナリと依存ライブラリのインストール
動的・ステルスブラウザ（Playwright / Patchright）を実行するために Chromium をダウンロードします。

**Windows:**
```powershell
scrapecore install
# または
playwright install chromium
```

**Linux (Ubuntu/Debian / Docker / ヘッドレスサーバー):**
Linuxサーバー環境では必要な共有ライブラリを含めてインストールします:
```bash
scrapecore install
# またはシステム依存パッケージを含めてインストール:
playwright install --with-deps chromium
```

### 4. 対話型テスト＆実験ラボ (`ScrapeCore.py`)
すべての機能を対話型メニューでテストできます:

**Windows:**
```powershell
python ScrapeCore.py
```

**Linux / macOS:**
```bash
python3 ScrapeCore.py
```

---

## 📖 包括的利用ガイド

### 1. クイックスタート (Quickstart)

```python
from scrapecore import Fetcher

# curl_cffiベースのTLS偽装による高速GETリクエスト
page = Fetcher.get("https://quotes.toscrape.com")

print("ステータスコード:", page.status)

# CSSセレクターで最初の名言を取得
first_quote = page.css("span.text::text").get()
print("名言:", first_quote)

# 全著者をリスト形式で取得
authors = page.css("small.author::text").getall()
print(f"著者数: {len(authors)} 名: {authors[:3]}")
```

---

### 2. リクエストエンジン解説 (Fetchers)

対象サイトの難易度や動的度合に応じて4種類のエンジンを選択可能です:

| エンジン | ベース | 主な用途 | JS実行? | ボット回避力 |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | 静的HTML、REST API、最高速度 | ❌ | 中程度 (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | 高並行・大規模な非同期データ取得 | ❌ | 中程度 (TLS/JA3) |
| `DynamicFetcher` | `playwright` | SPA、JavaScriptによる動的描画ページ | ✅ | 標準 |
| `StealthyFetcher` | `patchright` | Cloudflare、DataDome、強固な防御壁 | ✅ | **最高峰 (完全偽装)** |

#### A. 高速な静的リクエスト (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# 同期リクエスト
res = Fetcher.get("https://httpbin.org/headers", headers={"X-Custom": "Value"})
print(res.json())

# 非同期リクエスト
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. JavaScriptレンダリング (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # ネットワーク通信が落ち着くまで待機
)

print(page.css("span.text::text").get())
```

#### C. 高度なボット対策およびCloudflare突破 (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Cloudflare保護対象サイト
    solve_cloudflare=True,              # Turnstile認証を自動解決
    headless=True,                      # バックグラウンド実行
    block_ads=True,                     # 3500以上の広告・トラッカードメインを遮断
    disable_resources=True,             # 画像やフォント読み込みを省略して3倍高速化
    timeout=60000                       # 60秒タイムアウト
)

print("アクセス成功! タイトル:", page.css("h1::text").get())
```

#### D. ページ内自動化アクション (`page_action`)

```python
from scrapecore import StealthyFetcher

def infinite_scroll(page):
    # ページを3回下方にスクロール
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=infinite_scroll
)
```

---

### 3. データ抽出とセレクター

すべてのFetcherは `Selector` を継承した統一 **`Response`** オブジェクトを返します。

#### CSSおよびXPathセレクター
```python
# CSSによる単一テキスト取得
title = page.css("h1.main-title::text").get()

# 属性のリスト取得
links = page.css("div.menu a::attr(href)").getall()

# 完全なXPath対応
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### BeautifulSoupライクな検索 (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

buttons = page.find_all("button", type="submit")
for btn in buttons:
    print(btn.attrib.get("id"))
```

#### スマートテキストクリーニング (`clean_text`)
余分な空白や改行、エスケープ文字を自動的に整理します:
```python
node = page.css("div.description").first
print(node.clean_text())
```

#### 自己修復型セレクター (Adaptive Selectors)
```python
# 構造指紋をローカルのSQLiteに保存
page.css("button.buy-now", adaptive=True, auto_save=True)

# 将来サイトのクラス名が変更されても自動的に要素を再発見
button = page.css("button.buy-now", adaptive=True)
```

---

### 4. Fetch/XHR パケット監視と直接スクレイピング

モダンWebアプリは、HTML内部にデータを埋め込まず、バックグラウンドのAPIコールを介してJSONを読み込むことが大半です。このネットワーク通信を直接インターセプトすることで、**HTMLパース不要で、圧倒的に高速かつ確実に**構造化データを取得できます。

#### A. 基本的なキャプチャ (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # ネットワークパケットの捕捉を有効化
)

print(f"捕捉した通信数: {len(page.captured_xhr)}")
print(f"捕捉したURL一覧: {page.xhr_urls}")
```

#### B. 正規表現やコールバックによる絞り込み

```python
# 1. 正規表現で特定APIのみを捕捉:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. 独自関数による高度なフィルタリング:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. `Response` オブジェクトのXHR操作メソッド

| プロパティ / メソッド | 説明 |
| :--- | :--- |
| `page.captured_xhr` | 捕捉されたXHR/Fetch `Response` オブジェクトのリスト |
| `page.xhr_urls` | 捕捉されたすべてのURL文字列リスト (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | 条件に合致する**最初**のパケットを返却（なければ `None`） |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | 条件に合致する**すべて**のパケットをリストで返却 |
| `page.xhr_json(url_pattern=..., default=None)` | 最初の一致パケットのボディを直接JSON辞書/リストとしてデコード |
| `xhr.post_data` / `xhr.request_data` | クライアントが送信したPOSTデータ・ペイロード文字列 |
| `xhr.resource_type` | Playwrightリソース種別（`"xhr"` または `"fetch"`） |
| `xhr.method` | HTTPメソッド（`"GET"`, `"POST"` など） |

#### 例: インターセプトしたAPIから直接JSONを抽出

```python
# APIのJSONレスポンスを直接パース
products_json = page.xhr_json(r"/api/products\?category=electronics")
if products_json:
    for item in products_json.get("items", []):
        print(item["name"], item["price"])

# 送信されたPOSTリクエストの内容を検査
post_reqs = page.filter_xhr(method="POST", status=200)
for req in post_reqs:
    print(f"POST先: {req.url}")
    print(f"送信ペイロード: {req.post_data}")
    print(f"レスポンスJSON: {req.json()}")
```

#### D. CLIおよびテスト環境からの利用

```powershell
# CLIコマンドからXHRパケットを捕捉して保存:
scrapecore extract fetch "https://quotes.toscrape.com/js/" output.html --capture-xhr

# 対話型実験ラボでテスト:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. 大規模クローリング: Spiders フレームワーク

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
    print(f"合計 {len(result.items)} 件の書籍データを収集しました！")
```

---

### 6. セッション管理とプロキシローテーション

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

### 7. AIおよびMCPサーバー (Model Context Protocol)

```powershell
# stdioモードでMCPサーバーを起動
scrapecore-mcp

# HTTPストリーミングモードで起動
scrapecore-mcp --http --port 8000
```

#### RAG向けクリーンMarkdownへの自動変換
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o news.md
```

---

### 8. コマンドラインインターフェース (CLI)

#### 対話型スクレイピングシェル (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### ファイルへの直接抽出 (`scrapecore extract`)
```powershell
# CSSセレクターの結果をファイルへ出力
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o quotes.txt

# ステルスブラウザ＋Cloudflare解決
scrapecore extract stealthy-fetch "https://target-site.com" --solve-cloudflare -o page.html
```

---

## 📁 ディレクトリ構成

```
ScrapeCore/
│
├── lang/                       # 多言語ドキュメント
│   ├── readme_en.md            # 英語
│   ├── readme_es.md            # スペイン語
│   ├── readme_pt-br.md         # ポルトガル語 (ブラジル)
│   ├── readme_zh.md            # 簡体字中国語
│   ├── readme_ja.md            # 日本語
│   ├── readme_de.md            # ドイツ語
│   ├── readme_fr.md            # フランス語
│   ├── readme_ru.md            # ロシア語
│   ├── readme_ko.md            # 韓国語
│   └── readme_ar.md            # アラビア語
│
├── scrapecore/                 # ライブラリ本体のソースコード
├── tests/                      # 単体・統合テストスイート
├── .venv/                      # Python 3.13 仮想環境
├── pyproject.toml              # パッケージ定義
├── requirements.txt            # インストール依存関係
├── LICENSE                     # BSD-3 ライセンス (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # 対話型テスト・診断ラボ
└── README.md                   # メインドキュメント (トルコ語)
```

---

## 🙏 謝辞とクレジット (Acknowledgements)

本プロジェクトは、**Karim Shoair 氏 ([@D4Vinci](https://github.com/D4Vinci))** が制作した偉大なライブラリ **[Scrapling](https://github.com/D4Vinci/Scrapling)** を基盤としています。

* **元リポジトリ:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **オリジナル開発者:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **オリジナルライセンス:** BSD 3-Clause License

革新的なステルス技術と優れたアーキテクチャをオープンソースとして提供してくださった Karim Shoair 氏およびコミュニティに心より敬意と感謝を表します。ScrapeCore はこの基盤の上で独自に進化を続けています。

---

## ⚖️ ライセンス

本プロジェクトは **BSD 3-Clause License** の下で提供されています:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

詳細は [LICENSE](../LICENSE) ファイルをご参照ください。
