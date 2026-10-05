# 🕷️ ScrapeCore

> **Невидимая, сверхбыстрая и интеллектуальная библиотека веб-скрейпинга для современного интернета**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Языки / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <b>🇷🇺 Русский</b> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** — это Python-библиотека веб-скрейпинга нового поколения, созданная для обхода современных систем защиты от ботов (Cloudflare Turnstile, DataDome, WAF и др.), сверхвысокопроизводительного парсинга DOM-дерева, перехвата сетевых пакетов Fetch/XHR с прямым извлечением данных и проведения масштабного асинхронного краулинга.

> **Уведомление о лицензии и форке:**
> Проект активно разрабатывается и поддерживается **Alperen AKKAYA**. Базовая архитектура опирается на библиотеку Scrapling, созданную Karim Shoair, которая была форкнута и независимо развивается на условиях лицензии **BSD-3-Clause** с полным сохранением первоначальных авторских прав.

---

## 🚀 Ключевые возможности

* 🛡️ **Продвинутый стелс-движок (Stealth Engine):** Реалистичная симуляция цифровых отпечатков TLS/JA3 и заголовков браузера с помощью `patchright`, `curl_cffi` и `browserforge`.
* 📡 **Мониторинг и перехват сетевых пакетов Fetch/XHR:** Перехватывает все фоновые вызовы AJAX, Fetch и JSON (`capture_xhr=True`) и извлекает структурированные данные напрямую без парсинга HTML.
* 🧩 **Автоматический обход Cloudflare Turnstile:** Автоматически решает капчи Turnstile и промежуточные защитные экраны с помощью единственного параметра (`solve_cloudflare=True`).
* ⚡ **Сверхбыстрый парсер DOM:** Единый движок `Selector` на базе `lxml` и `cssselect`, работающий в разы быстрее BeautifulSoup.
* 🔄 **Самовосстанавливающиеся (адаптивные) селекторы:** Умный алгоритм `relocate`, способный находить элементы по структурному сходству даже после смены верстки сайта.
* 🕷️ **Встроенный фреймворк для пауков и краулеров:** Асинхронный краулинг с авторегулировкой скорости (autothrottle), управлением сессиями, поддержкой robots.txt и возобновлением работы (checkpointing).
* 🤖 **Готовность к ИИ и MCP:** Встроенный сервер Model Context Protocol (`scrapecore-mcp`) для LLM и ИИ-агентов, а также качественный конвертер HTML в Markdown для RAG-конвейеров.
* 💻 **Интерактивная консоль и тестовая лаборатория:** Интерактивная среда REPL через `scrapecore shell` и полноценный диагностический комплекс `ScrapeCore.py`.

---

## 📦 Установка (Кроссплатформенная)

ScrapeCore полностью совместим с **Windows**, **Linux** (Ubuntu, Debian, CentOS, Arch и др.) и **macOS**.

### 1. Подготовка виртуального окружения (Рекомендуется)
Поддерживается Python 3.10 и выше (Рекомендуется: **Python 3.13**).

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

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Установка бинарных файлов браузеров и системных зависимостей
Для работы динамического и стелс-браузеров (Playwright / Patchright) скачайте Chromium и необходимые системные библиотеки.

**Windows:**
```powershell
scrapecore install
# или
playwright install chromium
```

**Linux (Ubuntu/Debian / Docker / Headless-серверы):**
На серверах Linux необходимые общие системные библиотеки устанавливаются автоматически:
```bash
scrapecore install
# или с полной установкой системных зависимостей ОС:
playwright install --with-deps chromium
```

### 4. Интерактивная лаборатория тестирования (`ScrapeCore.py`)
Запустите интерактивную лабораторию для тестирования всех модулей:

**Windows:**
```powershell
python ScrapeCore.py
```

**Linux / macOS:**
```bash
python3 ScrapeCore.py
```

---

## 📖 Полное руководство пользователя

### 1. Быстрый старт (Quickstart)

```python
from scrapecore import Fetcher

# Быстрый GET-запрос на базе curl_cffi с маскировкой под TLS браузера
page = Fetcher.get("https://quotes.toscrape.com")

print("Код ответа:", page.status)

# Извлечение текста первой цитаты через CSS-селектор
first_quote = page.css("span.text::text").get()
print("Цитата:", first_quote)

# Список всех авторов
authors = page.css("small.author::text").getall()
print(f"Всего авторов найдено: {len(authors)}: {authors[:3]}")
```

---

### 2. Сетевые движки (Обзор Fetchers)

ScrapeCore предоставляет 4 движка под любые задачи:

| Движок | Основа | Применение | Нужен JS? | Защита от ботов |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | Статический HTML, REST API, максимальная скорость | ❌ | Средняя (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | Высококонкурентные асинхронные запросы | ❌ | Средняя (TLS/JA3) |
| `DynamicFetcher` | `playwright` | SPA, сайты с обязательным рендерингом JS | ✅ | Стандартная |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome и строгие антибот-системы | ✅ | **Максимальная (Стелс)** |

#### A. Высокоскоростные статические запросы (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Синхронный запрос
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Value"})
print(res.json())

# Асинхронный запрос
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. Рендеринг JavaScript (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Ожидание спада сетевой активности
)

print(page.css("span.text::text").get())
```

#### C. Обход Cloudflare и сложных систем защиты (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Демо-сайт с защитой Cloudflare
    solve_cloudflare=True,              # Автоматическое решение Turnstile
    headless=True,                      # Фоновый запуск
    block_ads=True,                     # Блокировка более 3500 рекламных доменов
    disable_resources=True,             # Пропуск картинок и шрифтов для ускорения в 3 раза
    timeout=60000                       # Таймаут 60 секунд
)

print("Успешный вход! Заголовок:", page.css("h1::text").get())
```

#### D. Автоматизация действий на странице (`page_action`)

```python
from scrapecore import StealthyFetcher

def бесконечная_прокрутка(page):
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=бесконечная_прокрутка
)
```

---

### 3. Извлечение данных и селекторы

Любой fetcher возвращает унифицированный объект **`Response`**, наследующий методы `Selector`.

#### CSS и XPath селекторы
```python
# Извлечение одного фрагмента текста
title = page.css("h1.main-title::text").get()

# Извлечение списка атрибутов
links = page.css("div.menu a::attr(href)").getall()

# Поддержка XPath
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### Поиск в стиле BeautifulSoup (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

buttons = page.find_all("button", type="submit")
for btn in buttons:
    print(btn.attrib.get("id"))
```

#### Очистка текста (`clean_text`)
```python
elem = page.css("div.description").first
print(elem.clean_text())
```

#### Самовосстанавливающиеся (адаптивные) селекторы
```python
# Сохранение слепка структуры в локальную базу SQLite
page.css("button.buy-now", adaptive=True, auto_save=True)

# При изменении дизайна в будущем элемент будет найден повторно
button = page.css("button.buy-now", adaptive=True)
```

---

### 4. Мониторинг сетевых пакетов Fetch/XHR и сбор данных

Современные веб-приложения зачастую отдают данные не в статическом HTML, а через фоновые сетевые запросы API. Прямой перехват этих пакетов происходит **быстрее, надежнее и сразу возвращает структурированный JSON**.

#### A. Базовый перехват (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Включает перехват сетевых пакетов
)

print(f"Всего пакетов поймано: {len(page.captured_xhr)}")
print(f"Список URL: {page.xhr_urls}")
```

#### B. Выборочная фильтрация с помощью регулярных выражений или функций

```python
# 1. Регулярное выражение:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Пользовательская функция-фильтр:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. Методы работы с XHR в объекте `Response`

| Свойство / Метод | Описание |
| :--- | :--- |
| `page.captured_xhr` | Список всех перехваченных объектов `Response` |
| `page.xhr_urls` | Список URL всех перехваченных запросов (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Возвращает **первый** подходящий пакет (или `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Возвращает **все** подходящие пакеты (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | Автоматически парсит тело первого совпавшего пакета в JSON |
| `xhr.post_data` / `xhr.request_data` | Тело или POST-нагрузка, отправленная клиентом |
| `xhr.resource_type` | Тип ресурса в Playwright (`"xhr"` или `"fetch"`) |
| `xhr.method` | HTTP-метод (`"GET"`, `"POST"` и т.д.) |

#### Пример: Получение JSON прямо из перехваченного API

```python
# Декодирование ответа API без разбора HTML
products_json = page.xhr_json(r"/api/products\?category=electronics")
if products_json:
    for item in products_json.get("items", []):
        print(item["name"], item["price"])

# Анализ отправленных POST-запросов
post_requests = page.filter_xhr(method="POST", status=200)
for req in post_requests:
    print(f"POST URL: {req.url}")
    print(f"Отправленная полезная нагрузка: {req.post_data}")
    print(f"Ответ сервера (JSON): {req.json()}")
```

#### D. Использование в CLI и лаборатории

```powershell
# Запись XHR-пакетов через CLI:
scrapecore extract fetch "https://quotes.toscrape.com/js/" out.html --capture-xhr

# Тестирование перехвата в интерактивной лаборатории:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Масштабный краулинг: Фреймворк Spiders

```python
from scrapecore.spiders import Spider, Request

class BooksSpider(Spider):
    name = "books_crawler"
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
    spider = BooksSpider()
    result = spider.start()
    print(f"Собрано {len(result.items)} книг!")
```

---

### 6. Управление сессиями и ротация прокси

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

### 7. Искусственный интеллект и сервер MCP

```powershell
# Запуск MCP в режиме stdio
scrapecore-mcp

# Или запуск HTTP-потока по сети
scrapecore-mcp --http --port 8000
```

#### Конвертация в Markdown для RAG
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o news.md
```

---

### 8. Интерфейс командной строки (CLI)

#### Интерактивная консоль (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### Прямое сохранение в файл (`scrapecore extract`)
```powershell
# Извлечение CSS-селектора в файл
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o quotes.txt

# Стелс-браузер с обходом Cloudflare
scrapecore extract stealthy-fetch "https://target-site.com" --solve-cloudflare -o page.html
```

---

## 📁 Структура каталогов

```
ScrapeCore/
│
├── lang/                       # Многоязычная документация
│   ├── readme_en.md            # Английский
│   ├── readme_es.md            # Испанский
│   ├── readme_pt-br.md         # Португальский (Бразилия)
│   ├── readme_zh.md            # Упрощенный китайский
│   ├── readme_ja.md            # Японский
│   ├── readme_de.md            # Немецкий
│   ├── readme_fr.md            # Французский
│   ├── readme_ru.md            # Русский
│   ├── readme_ko.md            # Корейский
│   └── readme_ar.md            # Арабский
│
├── scrapecore/                 # Исходный код библиотеки
├── tests/                      # Набор тестов
├── .venv/                      # Виртуальное окружение Python 3.13
├── pyproject.toml              # Конфигурация сборщика пакета
├── requirements.txt            # Список зависимостей
├── LICENSE                     # Лицензия BSD-3 (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # Интерактивная тестовая лаборатория
└── README.md                   # Основная документация (Турецкий)
```

---

## 🙏 Благодарности и авторы

Этот проект опирается на фундаментальную разработку **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))**, создателя замечательной библиотеки **[Scrapling](https://github.com/D4Vinci/Scrapling)**.

* **Оригинальный репозиторий:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Автор оригинала:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Лицензия оригинала:** BSD 3-Clause License

Мы выражаем искреннюю признательность Karim Shoair и сообществу open-source за создание этой передовой архитектуры. ScrapeCore продолжает развивать эту концепцию в рамках независимой разработки.

---

## ⚖️ Лицензия

Проект распространяется под **лицензией BSD 3-Clause**:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

Подробности смотрите в файле [LICENSE](../LICENSE).
