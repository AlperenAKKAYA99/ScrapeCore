# 🕷️ ScrapeCore

> **面向现代 Web 的隐形、极速且智能的 Web 数据爬取与抓取库**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 语言 / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <b>🇨🇳 简体中文</b> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** 是专为应对现代 Web 复杂反爬防护机制（Cloudflare Turnstile、DataDome、WAF 等）打造的下一代 Python 网页数据抓取库。它具备超高性能的 DOM 解析能力、实时 Fetch/XHR 网络流量监听及直接数据提取功能，并能轻松运行大规模异步爬虫。

> **开源许可与分支声明 (Fork Notice)：**
> 本项目由 **Alperen AKKAYA** 开发与维护。核心底层架构派生自 Karim Shoair 开发的 Scrapling 库，在 **BSD-3-Clause** 开源许可规范下独立分支并持续演进，完整保留原有署名及版权声明。

---

## 🚀 核心特性

* 🛡️ **高级隐形引擎 (Stealth Engine):** 借助 `patchright`、`curl_cffi` 与 `browserforge` 完美模拟真实浏览器 TLS/JA3 指纹和请求头。
* 📡 **Fetch/XHR 网络数据包监听与抓取:** 实时捕获页面底层的全部 AJAX/Fetch/JSON 流量 (`capture_xhr=True`)，无需解析 HTML 即可直接获取结构化数据。
* 🧩 **自动突破 Cloudflare Turnstile:** 仅需单个参数 (`solve_cloudflare=True`) 即可全自动解决 Turnstile 质询及过场等待页。
* ⚡ **极速 DOM 解析器:** 基于 `lxml` 与 `cssselect` 高度优化的统一 `Selector` 引擎，解析速度大幅超越 BeautifulSoup。
* 🔄 **自愈式自适应选择器 (Adaptive Selectors):** 具备基于结构相似度的智能 `relocate` 算法，在网站界面改版更新后依然能精准重定位元素。
* 🕷️ **内置异步 Spider 爬虫框架:** 具备自动限速 (autothrottle)、会话保持、robots.txt 规范遵循及爬取断点续传能力。
* 🤖 **AI 与 MCP 深度集成:** 内置 Model Context Protocol (`scrapecore-mcp`) 服务供 LLM / AI 智能体直接调用，提供高质量 HTML 转 Markdown 转换。
* 💻 **交互式控制台与实验室:** 提供实时 REPL 调试环境 `scrapecore shell` 与全面测试套件 `ScrapeCore.py`。

---

## 📦 安装与跨平台支持 (Windows & Linux / macOS)

ScrapeCore 完美兼容 **Windows**、**Linux** (Ubuntu、Debian、Fedora、Arch、CentOS 等) 与 **macOS**。支持 Python 3.10 及以上版本（推荐：**Python 3.13**）。

### 1. 创建虚拟环境 (Virtual Environment)

**🪟 Windows (PowerShell / CMD):**
```powershell
# 创建虚拟环境
python -m venv .venv

# 在 PowerShell 中激活
.\.venv\Scripts\Activate.ps1

# (使用 CMD 时)
.\.venv\Scripts\activate.bat
```

**🐧 Linux & 🍎 macOS (Bash / Zsh):**
```bash
# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境
source .venv/bin/activate
```

---

### 2. 安装核心依赖

安装全部核心请求引擎、浏览器自动化工具与 AI 组件：

**Windows 与 Linux 通用:**
```bash
pip install -r requirements.txt
```

---

### 3. 安装浏览器内核与系统运行库

运行动态渲染与隐形浏览器引擎 (`Playwright` / `Patchright`) 需要安装 Chromium：

**🪟 Windows:**
```powershell
scrapecore install
# 或
playwright install chromium
```

**🐧 Linux (服务器、Docker 与发行版):**
> 💡 *在无图形界面的 Linux 服务器 (Ubuntu/Debian 等) 上，Chromium 需要配套的系统底层动态链接库支持。请使用完整依赖命令进行安装：*
```bash
# 安装 Chromium 及所需系统共享库
playwright install --with-deps chromium
# 或使用内置命令
scrapecore install
```

---

### 4. 交互式测试与体验实验室 (`ScrapeCore.py`)

运行内置的交互式诊断实验室，即可全面验证各项功能：

**🪟 Windows:**
```powershell
python ScrapeCore.py
```

**🐧 Linux & 🍎 macOS:**
```bash
python3 ScrapeCore.py
```
*(查看可用命令行参数: `python3 ScrapeCore.py --help`)*

---

## 📖 详尽使用指南

### 1. 快速上手 (Quickstart)

```python
from scrapecore import Fetcher

# 使用 curl_cffi 模拟真实 TLS 指纹进行快速 GET 请求
page = Fetcher.get("https://quotes.toscrape.com")

print("状态码:", page.status)

# 使用 CSS 选择器获取第一条名言内容
first_quote = page.css("span.text::text").get()
print("名言:", first_quote)

# 提取所有作者名称
authors = page.css("small.author::text").getall()
print(f"共发现 {len(authors)} 位作者: {authors[:3]}")
```

---

### 2. 请求引擎详解 (Fetchers)

根据目标网站的动态程度与防御等级，ScrapeCore 提供了 4 种专业请求引擎：

| 引擎 | 底层依赖 | 适用场景 | 执行 JS? | 防反爬能力 |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | 静态 HTML、REST API、追求极速 | ❌ | 中等 (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | 高并发、大规模异步数据请求 | ❌ | 中等 (TLS/JA3) |
| `DynamicFetcher` | `playwright` | 单页应用 (SPA)、依赖 JS 渲染的页面 | ✅ | 标准 |
| `StealthyFetcher` | `patchright` | 针对 Cloudflare、DataDome 及强防护站点 | ✅ | **极强 (完全隐形)** |

#### A. 高效静态请求 (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# 同步请求
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Value"})
print(res.json())

# 异步批量请求
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. JavaScript 动态渲染 (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # 等待网络空闲
)

print(page.css("span.text::text").get())
```

#### C. 高级反反爬与 Cloudflare 绕过 (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Cloudflare 保护示范页
    solve_cloudflare=True,              # 自动通过 Turnstile 质询
    headless=True,                      # 后台静默执行
    block_ads=True,                     # 屏蔽 3500+ 常见广告与追踪域名
    disable_resources=True,             # 拦截图片和字体以获得 300% 提速
    timeout=60000                       # 超时时间 60 秒
)

print("访问成功! 页面标题:", page.css("h1::text").get())
```

#### D. 页面自动化操作 (`page_action`)

```python
from scrapecore import StealthyFetcher

def infinite_scroll(page):
    # 向下滚动 3 次以触发懒加载
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=infinite_scroll
)
```

---

### 3. 数据解析与选择器 (Selectors)

所有 Fetcher 均返回继承自 `Selector` 的统一 **`Response`** 对象。

#### CSS 与 XPath 选择器
```python
# CSS 提取单条文本
title = page.css("h1.main-title::text").get()

# CSS 提取属性列表
links = page.css("div.menu a::attr(href)").getall()

# 完整 XPath 支持
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### 类似 BeautifulSoup 的便捷查找 (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

all_buttons = page.find_all("button", type="submit")
for btn in all_buttons:
    print(btn.attrib.get("id"))
```

#### 智能文本清洗 (`clean_text`)
```python
node = page.css("div.description").first
print(node.clean_text())
```

#### 自愈式选择器 (Adaptive Selectors)
```python
# 保存元素指纹至本地数据库
page.css("button.buy-now", adaptive=True, auto_save=True)

# 网站改版后即使 class 变动，也能重新精确定位该按钮
buy_btn = page.css("button.buy-now", adaptive=True)
```

---

### 4. Fetch/XHR 网络流量监听与抓取

现代 Web 应用通常不把核心数据渲染在静态 HTML 中，而是通过后台 API 进行异步加载。监听并直接提取这些底层网络包不仅**速度更快、更稳定，还能直接拿到结构化的 JSON 数据**。

#### A. 基础监听 (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # 启用网络包拦截捕获
)

print(f"总计捕获网络包: {len(page.captured_xhr)}")
print(f"所有拦截到的 URL: {page.xhr_urls}")
```

#### B. 使用正则或过滤函数定向拦截

```python
# 1. 使用正则表达式匹配：
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. 使用自定义判定函数：
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. `Response` 中的 XHR 检索与处理方法

| 属性 / 方法 | 说明 |
| :--- | :--- |
| `page.captured_xhr` | 拦截到的所有 XHR/Fetch `Response` 对象列表 |
| `page.xhr_urls` | 所有拦截到的请求 URL 列表 (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | 返回满足条件的**首个**数据包 (或 `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | 返回满足条件的**全部**数据包 (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | 直接将首个匹配包体解析为 JSON 并返回 |
| `xhr.post_data` / `xhr.request_data` | 客户端发送的 POST / 表单请求体文本 |
| `xhr.resource_type` | Playwright 资源类型 (`"xhr"` 或 `"fetch"`) |
| `xhr.method` | HTTP 请求方法 (`"GET"`, `"POST"` 等) |

#### 示例：直接提取 API 的 JSON 数据

```python
# 无需解析 HTML，直接读取拦截到的 API 数据
products_json = page.xhr_json(r"/api/products\?category=electronics")
if products_json:
    for item in products_json.get("items", []):
        print(item["name"], item["price"])

# 检索特定 POST 请求与其提交的参数
post_requests = page.filter_xhr(method="POST", status=200)
for req in post_requests:
    print(f"POST 地址: {req.url}")
    print(f"提交载荷 (Payload): {req.post_data}")
    print(f"返回结果 (JSON): {req.json()}")
```

#### D. 命令行与测试实验室调用

```powershell
# 命令行捕获 XHR 并保存页面：
scrapecore extract fetch "https://quotes.toscrape.com/js/" output.html --capture-xhr

# 在交互式实验室中测试网络拦截：
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. 大规模分布式爬虫：Spiders 框架

```python
from scrapecore.spiders import Spider, Request

class BookSpider(Spider):
    name = "book_spider"
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
    print(f"成功采集 {len(result.items)} 本图书数据!")
```

---

### 6. 会话管理与代理轮换

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

### 7. AI 与 MCP 服务 (Model Context Protocol)

```powershell
# 启动标准输入输出 MCP 服务
scrapecore-mcp

# 或者以 HTTP 模式提供服务
scrapecore-mcp --http --port 8000
```

#### 为 RAG 知识库提取干净 Markdown
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o news.md
```

---

### 8. 命令行工具 (CLI 指南)

#### 实时交互式抓取控制台 (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### 快速提取数据至文件 (`scrapecore extract`)
```powershell
# 提取 CSS 结果保存到文件
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o quotes.txt

# 隐身浏览器 + Cloudflare 绕过抓取
scrapecore extract stealthy-fetch "https://target-site.com" --solve-cloudflare -o page.html
```

---

## 📁 目录组织结构

```
ScrapeCore/
│
├── lang/                       # 多语言文档目录
│   ├── readme_en.md            # 英文
│   ├── readme_es.md            # 西班牙语
│   ├── readme_pt-br.md         # 葡萄牙语 (巴西)
│   ├── readme_zh.md            # 简体中文
│   ├── readme_ja.md            # 日语
│   ├── readme_de.md            # 德语
│   ├── readme_fr.md            # 法语
│   ├── readme_ru.md            # 俄语
│   ├── readme_ko.md            # 韩语
│   └── readme_ar.md            # 阿拉伯语
│
├── scrapecore/                 # 库核心源代码
├── tests/                      # 单元与集成测试套件
├── .venv/                      # Python 3.13 虚拟环境
├── pyproject.toml              # 包配置与依赖定义
├── requirements.txt            # 项目安装依赖列表
├── LICENSE                     # BSD-3 许可证 (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # 交互式综合体验与诊断实验室
└── README.md                   # 主文档 (土耳其语)
```

---

## 🙏 致谢与署名 (Acknowledgements & Credits)

本项目基于 **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))** 创立的 **[Scrapling](https://github.com/D4Vinci/Scrapling)** 开源项目。

* **原始代码仓库:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **原始作者:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **开源许可证:** BSD 3-Clause License

对 Karim Shoair 及开源社区在反反爬机制与现代化数据采集架构上的杰出探索表示诚挚谢意。ScrapeCore 将继续保持独立研发与功能扩展。

---

## ⚖️ 开源许可证

本项目遵循 **BSD 3-Clause License**:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

详情见 [LICENSE](../LICENSE) 文件。
