# 🕷️ ScrapeCore

> **مكتبة كشط ويب (Web Scraping) خفية، فائقة السرعة وذكية للويب الحديث**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 اللغات / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <b>🇸🇦 العربية</b>
</p>

**ScrapeCore** هي مكتبة بايثون (Python) متطورة من الجيل الجديد لكشط البيانات واستخراجها من الويب، تم تصميمها خصيصاً لتجاوز أنظمة الحماية ومكافحة البوتات الحديثة (مثل Cloudflare Turnstile وDataDome وWAFs)، وتنفيذ تحليل فائق السرعة لشجرة DOM، واعتراض حزم شبكة Fetch/XHR في الوقت الفعلي لاستخراج البيانات مباشرة، وتشغيل زواحف الويب غير المتزامنة على نطاق واسع بكل سهولة.

> **إشعار الترخيص والتفرع (Fork Notice):**
> يتم تطوير هذا المشروع وصيانته بواسطة **Alperen AKKAYA**. البنية الأساسية مبنية على مكتبة Scrapling التي طورها Karim Shoair، حيث تم تفريعها وتطويرها بشكل مستقل وفقاً لبنود رخصة **BSD-3-Clause**، مع الحفاظ الكامل على حقوق النشر الأصلية.

---

## 🚀 المميزات الرئيسية

* 🛡️ **محرك التخفي المتقدم (Stealth Engine):** محاكاة واقعية للغاية لبصمات TLS/JA3 وترويسات المتصفحات الحقيقية عبر `patchright` و`curl_cffi` و`browserforge`.
* 📡 **مراقبة واعتراض حزم شبكة Fetch/XHR:** التقاط جميع طلبات AJAX وFetch وJSON التي تتم في الخلفية تلقائياً (`capture_xhr=True`) واستخراج البيانات المهيكلة مباشرة دون الحاجة لتحليل كود HTML.
* 🧩 **تجاوز تلقائي لحماية Cloudflare Turnstile:** حل اختبارات التحقق وصفحات الانتظار تلقائياً بالكامل باستخدام معلمة واحدة (`solve_cloudflare=True`).
* ⚡ **محلل DOM فائق السرعة:** محرك موحد `Selector` مبني على `lxml` و`cssselect`، يتفوق بمراحل على BeautifulSoup في سرعة المعالجة.
* 🔄 **محددات ذاتية الإصلاح (Adaptive Selectors):** خوارزمية ذكية `relocate` قادرة على إعادة اكتشاف العناصر المستهدفة بالاعتماد على التشابه الهيكلي حتى بعد تغيير تصميم الموقع.
* 🕷️ **إطار عمل مدمج للزواحف (Spiders & Crawlers):** زحف غير متزامن مع تحكم تلقائي في السرعة (autothrottle)، وإدارة الجلسات، والتوافق مع robots.txt، وإمكانية الإيقاف المؤقت والاستئناف.
* 🤖 **جاهز للذكاء الاصطناعي وMCP:** خادم أصيل لبروتوكول سياق النموذج (`scrapecore-mcp`) لنماذج اللغة الكبيرة ووكلاء الذكاء الاصطناعي، مع محول HTML إلى Markdown نظيف مخصص لخطوط معالجة RAG.
* 💻 **وحدة تحكم تفاعلية ومختبر تجارب:** بيئة REPL حية عبر `scrapecore shell` ومختبر فحص شامل `ScrapeCore.py`.

---

## 📦 التثبيت (متوافق مع مختلف الأنظمة)

مشروع ScrapeCore متوافق تماماً وبشكل قياسي مع أنظمة **Windows** و**Linux** (مثل Ubuntu وDebian وCentOS وArch) و**macOS**.

### 1. إعداد البيئة الافتراضية (موصى به)
يدعم ScrapeCore إصدارات Python 3.10 وما فوق (الموصى به: **Python 3.13**).

**نظام Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**أنظمة Linux / macOS (Bash / Zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. تثبيت الحزم المطلوبة

```bash
pip install -r requirements.txt
```

### 3. تحميل ملفات المتصفحات ومكتبات النظام
لتشغيل محركات التصفح الديناميكية والتخفي (Playwright / Patchright)، قم بتنزيل ملفات Chromium ومكتبات النظام اللازمة.

**نظام Windows:**
```powershell
scrapecore install
# أو
playwright install chromium
```

**أنظمة Linux (Ubuntu/Debian / بيئات Docker / الخوادم بدون واجهة رسومية Headless):**
على خوادم Linux، يمكن تثبيت المتصفح مع كافة مكتبات النظام التابعة له تلقائياً:
```bash
scrapecore install
# أو مع كافة حزم النظام المشتركة:
playwright install --with-deps chromium
```

### 4. مختبر الاختبارات التفاعلي (`ScrapeCore.py`)
يمكنك تشغيل مختبر التشخيص والتجارب لاختبار كافة الإمكانيات:

**نظام Windows:**
```powershell
python ScrapeCore.py
```

**أنظمة Linux / macOS:**
```bash
python3 ScrapeCore.py
```

---

## 📖 دليل الاستخدام الشامل

### 1. البداية السريعة (Quickstart)

```python
from scrapecore import Fetcher

# إرسال طلب GET سريع بالاعتماد على curl_cffi ومحاكاة بصمة المتصفح
page = Fetcher.get("https://quotes.toscrape.com")

print("رمز الحالة:", page.status)

# استخراج نص أول اقتباس عبر محدد CSS
first_quote = page.css("span.text::text").get()
print("الاقتباس:", first_quote)

# استخراج قائمة جميع المؤلفين
authors = page.css("small.author::text").getall()
print(f"عدد المؤلفين: {len(authors)}: {authors[:3]}")
```

---

### 2. محركات إرسال الطلبات (Fetchers)

يوفر ScrapeCore أربعة محركات متخصصة تتناسب مع درجة تعقيد الموقع المستهدف:

| المحرك | التقنية المستخدمة | أفضل استخدام | هل يدعم JS؟ | الحماية من البوتات |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | صفحات HTML الثابتة، واجهات REST API، السرعة القصوى | ❌ | متوسطة (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | الطلبات غير المتزامنة عالية التزامن | ❌ | متوسطة (TLS/JA3) |
| `DynamicFetcher` | `playwright` | تطبيقات الصفحة الواحدة (SPA)، المواقع التي تعتمد على JS | ✅ | قياسية |
| `StealthyFetcher` | `patchright` | مواقع Cloudflare وDataDome والحمايات الصارمة | ✅ | **قصوى (خفية تماماً)** |

#### أ. الطلبات الثابتة السريعة (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# طلب متزامن
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Value"})
print(res.json())

# طلب غير متزامن
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### ب. تصيير صفحات جافاسكريبت (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # الانتظار حتى تهدأ حركة الشبكة تماماً
)

print(page.css("span.text::text").get())
```

#### ج. التخفي المتقدم وتجاوز Cloudflare (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # موقع توضيحي محمي بواسطة Cloudflare
    solve_cloudflare=True,              # حل اختبار Turnstile تلقائياً
    headless=True,                      # تشغيل بدون واجهة في الخلفية
    block_ads=True,                     # حظر أكثر من 3500 نطاق إعلانات وتتبع
    disable_resources=True,             # تجاهل الصور والخطوط لتسريع التحميل بثلاثة أضعاف
    timeout=60000                       # مهلة 60 ثانية
)

print("تم الوصول بنجاح! العنوان:", page.css("h1::text").get())
```

#### د. الأتمتة التفاعلية داخل الصفحة (`page_action`)

```python
from scrapecore import StealthyFetcher

def التمرير_اللانهائي(page):
    # التمرير لأسفل الصفحة 3 مرات
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=التمرير_اللانهائي
)
```

---

### 3. استخراج البيانات والمحددات (Selectors)

تُرجع جميع المحركات كائناً موحداً من نوع **`Response`** يرث مباشرة من `Selector`.

#### محددات CSS و XPath
```python
# استخراج نص مفرد
title = page.css("h1.main-title::text").get()

# استخراج قائمة سمات (روابط)
links = page.css("div.menu a::attr(href)").getall()

# دعم كامل لـ XPath
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### البحث بأسلوب BeautifulSoup (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

buttons = page.find_all("button", type="submit")
for btn in buttons:
    print(btn.attrib.get("id"))
```

#### تنظيف النصوص الذكي (`clean_text`)
```python
node = page.css("div.description").first
print(node.clean_text())
```

#### المحددات ذاتية الإصلاح (Adaptive)
```python
# حفظ البصمة الهيكلية للعنصر في قاعدة بيانات SQLite المحلية
page.css("button.buy-now", adaptive=True, auto_save=True)

# في المستقبل، حتى لو تغيرت أسماء الفئات (classes)، سيعثر ScrapeCore على العنصر تلقائياً
button = page.css("button.buy-now", adaptive=True)
```

---

### 4. مراقبة واعتراض حزم شبكة Fetch/XHR

المواقع الحديثة والتطبيقات أحادية الصفحة (SPA) نادراً ما تضع بياناتها داخل كود HTML الثابت، بل تستدعي واجهات برمجة التطبيقات (APIs) في الخلفية لجلب بيانات JSON. اعتراض هذه الحزم مباشرة **أسرع بكثير وأكثر استقراراً ويعطي بيانات JSON نقية ومهيكلة**.

#### أ. الاعتراض الأساسي (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # تفعيل التقاط حزم الشبكة
)

print(f"إجمالي الحزم الملتقطة: {len(page.captured_xhr)}")
print(f"عناوين الروابط التي تم اعتراضها: {page.xhr_urls}")
```

#### ب. التصفية بواسطة التعبيرات النمطية (Regex) أو الدوال

```python
# 1. التصفية بنمط تعبير نمطي (Regex):
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. التصفية بدالة مخصصة:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### ج. دوال كائن `Response` للتعامل مع XHR

| الخاصية / الدالة | الوصف |
| :--- | :--- |
| `page.captured_xhr` | قائمة بكافة كائنات `Response` لحزم XHR/Fetch الملتقطة |
| `page.xhr_urls` | قائمة بكافة عناوين URL الملتقطة (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | تعيد **أول** حزمة تطابق الشروط (أو `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | تعيد **جميع** الحزم المطابقة كقائمة (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | تحلل محتوى أول حزمة متطابقة مباشرة كبيانات JSON |
| `xhr.post_data` / `xhr.request_data` | حمولة الطلب أو البيانات التي أرسلها العميل عبر POST |
| `xhr.resource_type` | نوع المورد في Playwright (`"xhr"` أو `"fetch"`) |
| `xhr.method` | طريقة HTTP المستخدمة (`"GET"`, `"POST"`, إلخ) |

#### مثال: استخراج بيانات JSON مباشرة من الـ API الملتقط

```python
# استخراج استجابة JSON مباشرة دون الحاجة لتحليل كود HTML
products_json = page.xhr_json(r"/api/products\?category=electronics")
if products_json:
    for item in products_json.get("items", []):
        print(item["name"], item["price"])

# فحص طلبات POST والحمولة المرسلة
post_requests = page.filter_xhr(method="POST", status=200)
for req in post_requests:
    print(f"عنوان POST: {req.url}")
    print(f"البيانات المرسلة: {req.post_data}")
    print(f"استجابة الخادم (JSON): {req.json()}")
```

#### د. الاستخدام عبر سطر الأوامر (CLI) ومختبر الاختبارات

```powershell
# التقاط حزم XHR من سطر الأوامر وحفظ الصفحة:
scrapecore extract fetch "https://quotes.toscrape.com/js/" output.html --capture-xhr

# تجربة الالتقاط الحية في مختبر التجارب التفاعلي:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. الزحف الواسع النطاق: إطار Spiders

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
    print(f"تم جمع بيانات {len(result.items)} كتاباً بنجاح!")
```

---

### 6. إدارة الجلسات وتدوير البروكسي (Proxy)

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

### 7. الذكاء الاصطناعي وخادم MCP (Model Context Protocol)

```powershell
# تشغيل خادم MCP في وضع stdio
scrapecore-mcp

# أو تشغيله عبر الشبكة في وضع تدفق HTTP
scrapecore-mcp --http --port 8000
```

#### تحويل صفحات الويب إلى Markdown نظيف لخطوط معالجة RAG
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o news.md
```

---

### 8. واجهة سطر الأوامر (دليل CLI)

#### شل الكشط التفاعلي (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### استخراج البيانات مباشرة إلى ملف (`scrapecore extract`)
```powershell
# استخراج نتائج محدد CSS إلى ملف
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o quotes.txt

# استخراج باستخدام متصفح التخفي وتجاوز Cloudflare
scrapecore extract stealthy-fetch "https://target-site.com" --solve-cloudflare -o page.html
```

---

## 📁 هيكلية المشروع

```
ScrapeCore/
│
├── lang/                       # مجلد التوثيق متعدد اللغات
│   ├── readme_en.md            # الإنجليزية
│   ├── readme_es.md            # الإسبانية
│   ├── readme_pt-br.md         # البرتغالية (البرازيل)
│   ├── readme_zh.md            # الصينية المبسطة
│   ├── readme_ja.md            # اليابانية
│   ├── readme_de.md            # الألمانية
│   ├── readme_fr.md            # الفرنسية
│   ├── readme_ru.md            # الروسية
│   ├── readme_ko.md            # الكورية
│   └── readme_ar.md            # العربية
│
├── scrapecore/                 # الشيفرة المصدرية الأساسية للمكتبة
├── tests/                      # حزم الاختبارات البرمجية
├── .venv/                      # البيئة الافتراضية بايثون 3.13
├── pyproject.toml              # ملف التجميع والتبعيات
├── requirements.txt            # متطلبات التثبيت
├── LICENSE                     # ترخيص BSD-3 (Alperen AKKAYA و Karim Shoair)
├── ScrapeCore.py               # المختبر التشخيصي والتفاعلي
└── README.md                   # التوثيق الأساسي (التركية)
```

---

## 🙏 شكر وتقدير (Acknowledgements & Credits)

يستند هذا المشروع إلى العمل الاستثنائي الذي قدمه **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))**، مبتكر مكتبة **[Scrapling](https://github.com/D4Vinci/Scrapling)** الرائدة.

* **المستودع الأصلي:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **المؤلف الأصلي:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **الترخيص الأصلي:** BSD 3-Clause License

نتقدم بجزيل الشكر والامتنان لـ Karim Shoair ومجتمع المصادر المفتوحة على توفير هذه المعمارية المبتكرة. ويواصل مشروع ScrapeCore البناء على هذه الأسس مع التطوير المستقل المستمر.

---

## ⚖️ الترخيص

يخضع هذا المشروع لشروط رخصة **BSD 3-Clause License**:

* **حقوق النشر (c) 2026, Alperen AKKAYA**
* **حقوق النشر (c) 2024, Karim Shoair**

يرجى مراجعة ملف [LICENSE](../LICENSE) للاطلاع على كامل التفاصيل.
