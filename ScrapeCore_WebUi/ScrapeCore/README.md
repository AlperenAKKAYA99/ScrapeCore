# 🕷️ ScrapeCore

> **Modern Web İçin Görünmez, Hızlı ve Akıllı Web Kazıma (Web Scraping) Kütüphanesi**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Diller / Languages:</b><br>
  <b>🇹🇷 Türkçe</b> • 
  <a href="lang/readme_en.md">🇬🇧 English</a> • 
  <a href="lang/readme_es.md">🇪🇸 Español</a> • 
  <a href="lang/readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="lang/readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="lang/readme_ja.md">🇯🇵 日本語</a> • 
  <a href="lang/readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="lang/readme_fr.md">🇫🇷 Français</a> • 
  <a href="lang/readme_ru.md">🇷🇺 Русский</a> • 
  <a href="lang/readme_ko.md">🇰🇷 한국어</a> • 
  <a href="lang/readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore**, modern web sitelerindeki gelişmiş bot engellerini (Cloudflare Turnstile, DataDome, WAF vb.) aşmak, yüksek performanslı DOM ayrıştırması yapmak ve büyük ölçekli asenkron tarama (crawling) işlemlerini zahmetsizce yürütmek üzere revize edilmiş yeni nesil bir Python web kazıma kütüphanesidir.

> **Lisans & Çatallanma (Fork) Bildirimi:**
> Bu proje, **Alperen AKKAYA** tarafından geliştirilmekte ve sürdürülmektedir. Çekirdek altyapı, Karim Shoair tarafından geliştirilen Scrapling kütüphanesinin **BSD-3-Clause** lisansı koşulları doğrultusunda çatallanmış (fork) ve bağımsız hale getirilmiştir. Orijinal telif hakları korunarak lisans koşullarına tam uyum sağlanmıştır.

---

## 🚀 Öne Çıkan Özellikler

* 🛡️ **Gelişmiş Görünmezlik (Stealth Engine):** `patchright`, `curl_cffi` ve `browserforge` desteğiyle gerçekçi TLS/JA3 parmak izi ve tarayıcı başlıkları simülasyonu.
* 📡 **Fetch/XHR Ağ Paketlerini İzleme & Kazıma:** Tarayıcının arka planda yaptığı tüm API, JSON ve AJAX çağrılarını (`capture_xhr=True`) anında yakalayıp doğrudan veri çıkarma.
* 🧩 **Otomatik Cloudflare Turnstile Çözümü:** Tek bir parametre (`solve_cloudflare=True`) ile Turnstile ve interstitial ekranlarını otomatik olarak geçer.
* ⚡ **Ultra Hızlı DOM Ayrıştırıcı:** `lxml` ve `cssselect` üzerinde optimize edilmiş, BeautifulSoup'tan çok daha hızlı çalışan birleşik `Selector` motoru.
* 🔄 **Kendi Kendini Onaran (Adaptive) Seçiciler:** Sayfa yapısı değiştiğinde yapay benzerlik algoritmalarıyla hedef öğeleri yeniden bulabilen akıllı `relocate` mekanizması.
* 🕷️ **Dahili Spider ve Crawler Çerçevesi:** Otomatik hız sınırlama (autothrottle), oturum yönetimi, robots.txt uyumu ve duraklat/devam et (checkpointing) desteği.
* 🤖 **Yapay Zeka & MCP Desteği:** LLM'ler ve AI ajanları için Model Context Protocol (`scrapecore-mcp`) sunucusu ve HTML-Markdown dönüştürücü.
* 💻 **Etkileşimli Terminal Arayüzü:** Canlı web sayfaları üzerinde anında seçici test etmek için `scrapecore shell` ve `ScrapeCore.py`.

---

## 📦 Kurulum ve Platform Uyumluluğu (Windows & Linux / macOS)

ScrapeCore; **Windows**, **Linux** (Ubuntu, Debian, Fedora, Arch, CentOS vb.) ve **macOS** işletim sistemleriyle %100 tam uyumludur. Python 3.10 ve üzeri sürümleri destekler (Önerilen: **Python 3.13**).

### 1. Sanal Ortamı Hazırlama (Virtual Environment)

**🪟 Windows (PowerShell / CMD):**
```powershell
# Sanal ortam oluşturma
python -m venv .venv

# Sanal ortamı aktif etme (PowerShell)
.\.venv\Scripts\Activate.ps1

# (CMD kullanıyorsanız)
.\.venv\Scripts\activate.bat
```

**🐧 Linux & 🍎 macOS (Bash / Zsh):**
```bash
# Sanal ortam oluşturma
python3 -m venv .venv

# Sanal ortamı aktif etme
source .venv/bin/activate
```

---

### 2. Bağımlılıkların Kurulması

Tüm çekirdek motorları, tarayıcı otomasyonunu ve AI bileşenlerini kurmak için:

**Windows & Linux:**
```bash
pip install -r requirements.txt
```

---

### 3. Tarayıcı İkillerinin ve Sistem Kütüphanelerinin Kurulması

Dinamik ve görünmez tarayıcı motorlarının (`Playwright` / `Patchright`) çalışabilmesi için Chromium ikililerini yükleyin:

**🪟 Windows:**
```powershell
scrapecore install
# veya
playwright install chromium
```

**🐧 Linux (Sunucu, Docker & Dağıtımlar):**
> 💡 *Linux sunucularda (Ubuntu/Debian vb.) Chromium'un grafik ve ses bağımlılıkları olmadan headless modda çalışması için gerekli sistem paketleriyle birlikte kurulması gerekir:*
```bash
# Gerekli sistem kütüphaneleriyle birlikte Chromium kurulumu
playwright install --with-deps chromium
# veya dahili komutla
scrapecore install
```

---

### 4. İnteraktif Test & Deneyim Laboratuvarı (`ScrapeCore.py`)

Kütüphanenin tüm özelliklerini (statik, dinamik, stealth, spider, AI, XHR izleme vb.) canlı olarak denemek ve test etmek için dahili test ortamını başlatabilirsiniz:

**🪟 Windows:**
```powershell
python ScrapeCore.py
```

**🐧 Linux & 🍎 macOS:**
```bash
python3 ScrapeCore.py
```
*(Komut satırı parametrelerini görmek için: `python3 ScrapeCore.py --help`)*

---

## 📖 Kapsamlı Kullanım Kılavuzu

### 1. Hızlı Başlangıç (Quickstart)

```python
from scrapecore import Fetcher

# curl_cffi tabanlı TLS taklit eden hızlı GET isteği
page = Fetcher.get("https://quotes.toscrape.com")

print("Durum Kodu:", page.status)

# CSS seçici ile ilk alıntıyı çekme
first_quote = page.css("span.text::text").get()
print("Alıntı:", first_quote)

# Tüm yazarları listeleme
authors = page.css("small.author::text").getall()
print(f"Toplam {len(authors)} yazar bulundu: {authors[:3]}")
```

---

### 2. İstek Motorları (Fetchers Rehberi)

ScrapeCore, hedef sitenin koruma düzeyine ve dinamizmine göre seçebileceğiniz 4 farklı istek motoru sunar:

| Motor | Taban | Kullanım Amacı | JavaScript? | Bot Koruması |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | Statik HTML, API istekleri, yüksek hız | ❌ | Orta (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | Eşzamanlı yüksek hacimli asenkron istekler | ❌ | Orta (TLS/JA3) |
| `DynamicFetcher` | `playwright` | Tek Sayfa Uygulamaları (SPA), JS render gerektiren sayfalar | ✅ | Standart |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome ve gelişmiş anti-bot korumalı siteler | ✅ | **Maksimum (Görünmez)** |

#### A. Hızlı Statik İstekler (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Statik istek
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Değer"})
print(res.json())

# Asenkron istek
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. JavaScript Render Eden Dinamik İstekler (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

# JavaScript çalıştıktan sonraki DOM'u yakalama
page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Ağ istekleri durulana kadar bekle
)

print(page.css("span.text::text").get())
```

#### C. Gelişmiş Anti-Bot & Cloudflare Aşma (`StealthyFetcher`)

`StealthyFetcher`, gerçek bir kullanıcının tarayıcısını birebir taklit eder ve Turnstile ekranlarını otomatik aşar:

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Cloudflare korumalı örnek adres
    solve_cloudflare=True,              # Turnstile doğrulamasını otomatik çöz
    headless=True,                      # Arka planda çalıştır (False yapılırsa tarayıcı görünür)
    block_ads=True,                     # 3500+ bilinen reklam/takipçi alan adını engelle
    disable_resources=True,             # Resim, font, medya indirmelerini kapatarak %300 hızlan
    timeout=60000                       # 60 saniye zaman aşımı
)

print("Erişim Başarılı! Başlık:", page.css("h1::text").get())
```

#### D. Sayfa İçi Otomasyon (`page_action`)
Tıklama, form doldurma veya sonsuz kaydırma (infinite scroll) gibi işlemler için Playwright `page` nesnesi üzerinden işlem yapabilirsiniz:

```python
from scrapecore import StealthyFetcher

def sonsuz_kaydirma(page):
    # Sayfayı 3 kez aşağı kaydır
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=sonsuz_kaydirma
)
```

---

### 3. Veri Ayrıştırma ve Seçiciler (Selectors)

Tüm fetcher'lar sonuç olarak doğrudan bir **`Response`** nesnesi döner. `Response`, `Selector` sınıfından türediği için sayfayı anında sorgulayabilirsiniz.

#### CSS ve XPath Seçicileri
```python
# CSS ile tek değer alma
title = page.css("h1.main-title::text").get()

# CSS ile liste alma
links = page.css("div.menu a::attr(href)").getall()

# XPath kullanımı
paragraphs = page.xpath("//div[@id='content']//p/text()").getall()
```

#### BeautifulSoup Benzeri Basit Arama (`find` & `find_all`)
```python
# İlk eşleşen öğeyi bul
header = page.find("h1", class_="title")
print(header.text)

# Tüm eşleşenleri bul
all_buttons = page.find_all("button", type="submit")
for btn in all_buttons:
    print(btn.attrib.get("id"))
```

#### Akıllı Metin Temizleme (`clean_text`)
Gereksiz boşlukları, satır başlarını ve HTML kaçış karakterlerini otomatik temizler:
```python
dirty_div = page.css("div.description").first
print(dirty_div.clean_text())
```

#### Kendi Kendini Onaran (Adaptive) Seçiciler
Hedef site arayüz değiştirdiğinde seçicilerinizin kırılmasını önler:
```python
# auto_save=True ile öğenin yapısal izi yerel veritabanına kaydedilir
page.css("button.satinal-butonu", adaptive=True, auto_save=True)

# Gelecekte sınıf adı değişse bile benzerlik analiziyle öğe yeniden bulunur
hedef_buton = page.css("button.satinal-butonu", adaptive=True)
```

---

### 4. Fetch/XHR Ağ Paketlerini İzleme ve Kazıma (Network Monitoring)

Modern web siteleri ve Tek Sayfa Uygulamaları (SPA), verileri doğrudan HTML içinde sunmak yerine arka planda AJAX, Fetch ve XHR çağrılarıyla JSON API'leri üzerinden yükler. Karmaşık DOM ağaçlarını ayrıştırmak yerine doğrudan bu ağ paketlerini yakalamak **çok daha hızlı, kararlı ve doğrudan yapılandırılmış veri sağlar**.

ScrapeCore; hem `DynamicFetcher` hem de `StealthyFetcher` motorlarında ağ trafiğini arka planda dinleyerek tüm XHR/Fetch paketlerini otomatik olarak birer `Response` nesnesi olarak yakalamanızı sağlar.

#### A. Temel Kullanım (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

# capture_xhr=True ile tüm XHR/Fetch çağrılarını yakalayalım
page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Ağ paketlerini dinlemeyi etkinleştirir
)

print(f"Toplam yakalanan ağ paketi: {len(page.captured_xhr)}")
print(f"Yakalanan istek URL'leri: {page.xhr_urls}")
```

#### B. Desen / Regex veya Fonksiyon ile Hedefli Dinleme

Yalnızca ilgilendiğiniz API veya JSON paketlerini yakalamak için `capture_xhr` parametresine regex deseni veya filtre fonksiyonu verebilirsiniz:

```python
# 1. Regex deseni ile yalnızca /api/ veya /v1/ geçen istekleri yakala:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Özel bir filtre fonksiyonu ile hedefli yakalama:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. `Response` Üzerindeki XHR Arama ve Filtreleme Metotları

Yakalanan paketler ana `page` nesnesi üzerinde saklanır ve zengin filtreleme metotlarıyla kolayca sorgulanabilir:

| Özellik / Metot | Açıklama |
| :--- | :--- |
| `page.captured_xhr` | Yakalanan tüm XHR/Fetch paketlerinin `Response` nesnesi listesi |
| `page.xhr_urls` | Yakalanan tüm isteklerin URL adresleri listesi (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Kriterlere uyan **ilk** paketi döner (veya `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Kriterlere uyan **tüm** paketleri döner (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | İlk eşleşen paketin gövdesini JSON olarak ayrıştırıp doğrudan döner |
| `xhr.post_data` / `xhr.request_data` | İstemcinin gönderdiği POST / form yükü metni |
| `xhr.resource_type` | Playwright kaynak tipi (`"xhr"` veya `"fetch"`) |
| `xhr.method` | İsteğin HTTP metodu (`"GET"`, `"POST"` vb.) |

#### Örnek: API Yanıtını Doğrudan JSON Olarak Çekme

```python
# Belirli bir API uç noktasını bulup JSON verisini alalım
urun_json = page.xhr_json(r"/api/products\?category=electronics")
if urun_json:
    for urun in urun_json.get("items", []):
        print(urun["name"], urun["price"])

# Veya POST isteklerini ve gönderilen yükü inceleyelim
post_istekleri = page.filter_xhr(method="POST", status=200)
for req in post_istekleri:
    print(f"Gönderilen POST URL: {req.url}")
    print(f"Gönderilen Yük (Payload): {req.post_data}")
    print(f"Gelen Yanıt (JSON): {req.json()}")
```

#### D. Komut Satırından (CLI) ve Test Ortamından (Playground) Kullanım

```powershell
# Terminalden XHR paketlerini de yakalayarak sayfayı kaydetme:
scrapecore extract fetch "https://quotes.toscrape.com/js/" cikti.html --capture-xhr

# Etkileşimli Test Ortamında (ScrapeCore.py) canlı test:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Büyük Ölçekli Tarama: Spiders Çerçevesi

ScrapeCore, modern `asyncio`/`anyio` temelli güçlü bir Spider altyapısına sahiptir:

```python
from scrapecore.spiders import Spider, Request

class KitapTarayici(Spider):
    name = "kitap_botu"
    start_urls = ["https://books.toscrape.com/"]
    
    # Otomatik hız sınırlama ayarları
    autothrottle_enabled = True
    concurrent_requests = 4

    async def parse(self, response):
        # Sayfadaki kitapları topla
        for book in response.css("article.product_pod"):
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
            }

        # Sonraki sayfaya geç (Pagination)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield Request(url=response.urljoin(next_page), callback=self.parse)

if __name__ == "__main__":
    spider = KitapTarayici()
    sonuc = spider.start()
    print(f"Toplam {len(sonuc.items)} kitap toplandı!")
```

---

### 6. Oturum Yönetimi ve Proxy Rotasyonu

İstekler arasında çerezleri ve oturum durumunu saklamak veya IP engellerinden kaçınmak için oturum yöneticilerini kullanabilirsiniz:

```python
from scrapecore.fetchers import FetcherSession, ProxyRotator

# Proxy havuzu tanımlama
rotator = ProxyRotator([
    "http://kullanici:sifre@proxy1.com:8000",
    "http://kullanici:sifre@proxy2.com:8000",
])

# Oturum başlatma
session = FetcherSession(proxy=rotator)

# İlk istek ile login olma
session.post("https://example.com/login", data={"user": "admin", "pass": "123"})

# Giriş yapılmış oturum üzerinden sayfa çekme
dashboard = session.get("https://example.com/dashboard")
print(dashboard.css("h2::text").get())
```

---

### 7. Yapay Zeka & MCP (Model Context Protocol)

ScrapeCore, Claude Desktop, Cursor veya diğer AI ajanlarının doğrudan internetten veri çekebilmesini sağlayan yerleşik bir MCP sunucusu içerir.

```powershell
# MCP sunucusunu stdio modunda başlatma
scrapecore-mcp

# Veya HTTP modunda ağ üzerinden sunma
scrapecore-mcp --http --port 8000
```

#### Web Sayfalarını AI İçin Markdown'a Çevirme
ScrapeCore, web sayfalarını reklamlardan arındırarak RAG ve LLM modellerinin kolayca okuyabileceği Markdown formatına çevirir:
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o hacker_news.md
```

---

### 8. Komut Satırı Arayüzü (CLI Kılavuzu)

#### Canlı Kazıma Kabuğu (`scrapecore shell`)
Hedef sayfa üzerinde etkileşimli IPython konsolu açarak seçicilerinizi anlık deneyin:

```powershell
scrapecore shell "https://quotes.toscrape.com"
```
*Açılan kabukta `page`, `Fetcher` ve seçiciler önceden yüklenmiş olarak gelir:*
```python
In [1]: page.css("span.text::text").get()
Out[1]: '“The world as we have created it is a process of our thinking...”'
```

#### Terminalden Hızlı Veri Çıkarma (`scrapecore extract`)
```powershell
# Belirli bir CSS seçiciyi çekip JSON/TXT olarak kaydetme
scrapecore extract "https://quotes.toscrape.com" -c "span.text" -o alintilar.txt

# Cloudflare korumalı bir sayfadan gizli tarayıcı ile veri alma
scrapecore extract "https://hedef-site.com" --fetcher stealthy --solve-cloudflare -o sayfa.html
```

---

## 📁 Proje Dizin Yapısı

```
ScrapeCore/
│
├── lang/                       # Çok dilli dokümantasyon klasörü (10 Dil)
│   ├── readme_en.md            # İngilizce (English)
│   ├── readme_es.md            # İspanyolca (Español)
│   ├── readme_pt-br.md         # Portekizce - Brezilya (Português)
│   ├── readme_zh.md            # Basitleştirilmiş Çince (简体中文)
│   ├── readme_ja.md            # Japonca (日本語)
│   ├── readme_de.md            # Almanca (Deutsch)
│   ├── readme_fr.md            # Fransızca (Français)
│   ├── readme_ru.md            # Rusça (Русский)
│   ├── readme_ko.md            # Korece (한국어)
│   └── readme_ar.md            # Arapça (العربية)
│
├── scrapecore/                 # Kütüphane çekirdek kaynak kodları
│   ├── core/                   # DOM motoru, depolama, tip tanımları, AI/MCP araçları
│   ├── engines/                # Tarayıcı motorları, stealth eklentileri, araçlar
│   ├── fetchers/               # Fetcher, AsyncFetcher, DynamicFetcher, StealthyFetcher
│   ├── parser/                 # lxml tabanlı Selector motoru ve adaptif algoritmalar
│   ├── spiders/                # Asenkron crawler ve hazır şablonlar (Shopify, Sitemap vb.)
│   └── cli.py                  # Komut satırı araçları (scrapecore, scrapecore-mcp)
│
├── tests/                      # Birim ve entegrasyon testleri
├── .venv/                      # Python 3.13 sanal ortamı
├── pyproject.toml              # Paketleme ve bağımlılık tanımları
├── requirements.txt            # Proje kurulum bağımlılıkları listesi
├── pytest.ini & tox.ini        # Test yapılandırma dosyaları
├── setup.cfg & MANIFEST.in     # Paket meta verileri
├── LICENSE                     # BSD-3 Lisans metni (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # İnteraktif Test & Deneyim Laboratuvarı
└── README.md                   # Ana Kullanım Kılavuzu (Türkçe)
```

## 🙏 Teşekkür ve Atıf (Acknowledgements & Credits)

Bu proje, **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))** tarafından geliştirilen muazzam **[Scrapling](https://github.com/D4Vinci/Scrapling)** projesini temel almaktadır.

* **Orijinal Depo:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Orijinal Geliştirici:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Orijinal Lisans:** BSD 3-Clause License

Açık kaynak dünyasına ve modern web kazıma ekosistemine kazandırdığı bu yenilikçi mimari, stealth yetenekleri ve ilham verici çalışmaları için **Karim Shoair**'e ve Scrapling topluluğuna teşekkür ederiz. ScrapeCore, bu sağlam temelin üzerine inşa edilerek bağımsız bir çizgide geliştirilmektedir.

---

## ⚖️ Lisans

Bu proje **BSD 3-Clause Lisansı** ile lisanslanmıştır:

* **Telif Hakkı (c) 2026, Alperen AKKAYA**
* **Telif Hakkı (c) 2024, Karim Shoair**

Detaylar için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.
