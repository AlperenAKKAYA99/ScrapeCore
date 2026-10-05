#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
🕷️ ScrapeCore - Kapsamlı Test, Deneyim ve Doğrulama Ortamı (Playground)
==============================================================================
Geliştirici : Alperen AKKAYA
Proje Deposu: https://github.com/AlperenAKKAYA99/ScrapeCore
Lisans      : BSD 3-Clause
Orijinal Temel: Karim Shoair (Scrapling)

Bu dosya, ScrapeCore kütüphanesinin tüm çekirdek özelliklerini (statik, asenkron,
dinamik ve görünmez tarayıcı motorları, adaptif seçiciler, spider/crawler,
AI Markdown dönüştürücü ve canlı kabuk) tek bir çatı altında interaktif olarak
test edebilmeniz için tasarlanmış kapsamlı test ve deney laboratuvarıdır.
==============================================================================
"""

import sys
import time
import asyncio
import argparse
from typing import List, Dict, Any, Optional

# Windows konsol Unicode uyumluluğu (cp1254 vb. karakter haritası hatalarını önler)
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Kütüphane içe aktarma
try:
    import scrapecore
    from scrapecore import (
        Fetcher,
        AsyncFetcher,
        DynamicFetcher,
        StealthyFetcher,
        Selector,
    )
    from scrapecore.spiders import Spider, Request
    from scrapecore.fetchers import FetcherSession, ProxyRotator
except ImportError as e:
    print(f"\n❌ Hata: 'scrapecore' kütüphanesi yüklenemedi: {e}")
    print("Lütfen sanal ortamı (.venv) aktif ettiğinizden emin olun:")
    print("  PowerShell: .\\.venv\\Scripts\\Activate.ps1\n")
    sys.exit(1)


# ==============================================================================
# Terminal Renklendirme Yardımcıları (ANSI)
# ==============================================================================
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}================================================================================
🕷️   S C R A P E C O R E   -   T E S T   &   P L A Y G R O U N D
================================================================================{Colors.RESET}
{Colors.DIM}Geliştirici : Alperen AKKAYA
Sürüm       : {scrapecore.__version__}
Depo        : https://github.com/AlperenAKKAYA99/ScrapeCore
Orijinal    : Karim Shoair (Scrapling - BSD-3-Clause){Colors.RESET}
--------------------------------------------------------------------------------
"""
    print(banner)


def print_section(title: str):
    print(f"\n{Colors.BOLD}{Colors.BLUE}▶ {title}{Colors.RESET}")
    print(f"{Colors.DIM}{'-' * 60}{Colors.RESET}")


def print_success(msg: str):
    print(f"{Colors.GREEN}✓ {msg}{Colors.RESET}")


def print_info(msg: str):
    print(f"{Colors.CYAN}ℹ {msg}{Colors.RESET}")


def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.RESET}")


def print_error(msg: str):
    print(f"{Colors.RED}✗ {msg}{Colors.RESET}")


# ==============================================================================
# Modül Test Fonksiyonları
# ==============================================================================

def test_static_fetcher(url: str = "https://quotes.toscrape.com"):
    """1. Statik Fetcher ve CSS/XPath seçici testi"""
    print_section(f"1. Statik Fetcher Testi (curl_cffi / TLS İstemcisi) -> {url}")
    print_info("İstek gönderiliyor...")
    start = time.perf_counter()
    try:
        page = Fetcher.get(url, timeout=15)
        elapsed = (time.perf_counter() - start) * 1000

        print_success(f"Yanıt Alındı: HTTP {page.status} ({elapsed:.1f} ms)")
        print_info(f"Başlık (CSS 'h1 a::text'): {page.css('h1 a::text').get()}")

        # Alıntıları listele
        quotes = page.css("div.quote")
        print_success(f"Sayfada {len(quotes)} adet alıntı öğesi tespit edildi.")

        if quotes:
            first = quotes[0]
            metin = first.css("span.text::text").get()
            yazar = first.css("small.author::text").get()
            etiketler = first.css("div.tags a.tag::text").getall()
            print(f"\n  {Colors.BOLD}Örnek Alıntı:{Colors.RESET}")
            print(f"  Metin    : {metin}")
            print(f"  Yazar    : {yazar}")
            print(f"  Etiketler: {', '.join(etiketler)}")

        # XPath testi
        xpath_author = page.xpath("//small[@class='author']/text()").get()
        print_info(f"XPath Doğrulaması (ilk yazar): {xpath_author}")
        return True
    except Exception as e:
        print_error(f"Statik Fetcher Hatası: {e}")
        return False


def test_async_fetcher(urls: Optional[List[str]] = None):
    """2. Asenkron AsyncFetcher eşzamanlı istek testi"""
    if not urls:
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
            "https://quotes.toscrape.com/page/3/",
        ]
    print_section(f"2. Asenkron İstek Testi (AsyncFetcher) -> {len(urls)} URL Eşzamanlı")

    async def _run():
        print_info(f"{len(urls)} adet sayfa paralel olarak indiriliyor...")
        start = time.perf_counter()
        tasks = [AsyncFetcher.get(u, timeout=15) for u in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        total_time = (time.perf_counter() - start) * 1000

        for idx, res in enumerate(responses):
            if isinstance(res, Exception):
                print_error(f"Sayfa {idx + 1} ({urls[idx]}): Hata -> {res}")
            else:
                quotes_count = len(res.css("div.quote"))
                print_success(f"Sayfa {idx + 1}: HTTP {res.status} | {quotes_count} Alıntı Bulundu")

        print_info(f"Toplam süre: {total_time:.1f} ms (Eşzamanlı hız)")
        return True

    try:
        return asyncio.run(_run())
    except Exception as e:
        print_error(f"Asenkron test hatası: {e}")
        return False


def test_dynamic_fetcher(url: str = "https://quotes.toscrape.com/js/"):
    """3. DynamicFetcher (Playwright) ile JS render testi"""
    print_section(f"3. Dinamik Tarayıcı Testi (Playwright) -> {url}")
    print_info("JavaScript çalıştırılan tarayıcı başlatılıyor (Headless Chromium)...")
    start = time.perf_counter()
    try:
        page = DynamicFetcher.fetch(
            url,
            headless=True,
            network_idle=True,
            timeout=30000,
        )
        elapsed = (time.perf_counter() - start) * 1000
        print_success(f"Tarayıcı Render Tamamlandı: HTTP {page.status} ({elapsed:.1f} ms)")

        js_quotes = page.css("div.quote")
        print_success(f"JS ile oluşturulmuş {len(js_quotes)} adet alıntı başarıyla yakalandı.")
        if js_quotes:
            print(f"  İlk Alıntı: {js_quotes[0].css('span.text::text').get()}")
        return True
    except Exception as e:
        print_error(f"Dinamik Tarayıcı Hatası: {e}")
        print_warning("Not: Chromium yüklü değilse terminalden 'scrapecore install' çalıştırın.")
        return False


def test_stealthy_fetcher(url: str = "https://nowsecure.nl"):
    """4. StealthyFetcher (Patchright + Cloudflare Çözücü) testi"""
    print_section(f"4. Görünmez (Stealth) Tarayıcı & Bot Testi -> {url}")
    print_info("Görünmez Patchright motoru çalıştırılıyor (Cloudflare Turnstile çözücü aktif)...")
    start = time.perf_counter()
    try:
        page = StealthyFetcher.fetch(
            url,
            headless=True,
            solve_cloudflare=True,
            block_ads=True,
            disable_resources=True,
            timeout=45000,
        )
        elapsed = (time.perf_counter() - start) * 1000
        print_success(f"Erişim Başarılı: HTTP {page.status} ({elapsed:.1f} ms)")

        h1 = page.css("h1::text").get() or page.css("title::text").get()
        print_info(f"Sayfa Başlığı / H1: {h1}")
        return True
    except Exception as e:
        print_error(f"Görünmez Tarayıcı Hatası: {e}")
        print_warning("Hedef site zaman aşımına uğramış veya internet bağlantısı yavaş olabilir.")
        return False


def test_page_action(url: str = "https://quotes.toscrape.com/scroll"):
    """5. Sayfa İçi Otomasyon (Page Action) Testi"""
    print_section(f"5. Sayfa İçi Otomasyon (page_action: Sonsuz Kaydırma Testi) -> {url}")
    print_info("Tarayıcı açılıyor ve sayfa kaydırma işlemi yürütülüyor...")

    def scroll_action(page):
        # 2 kez aşağı kaydırıp yeni öğelerin yüklenmesini bekle
        for i in range(2):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)

    try:
        page = StealthyFetcher.fetch(
            url,
            headless=True,
            page_action=scroll_action,
            timeout=30000,
        )
        quotes = page.css("div.quote")
        print_success(f"Kaydırma sonrasında yakalanan toplam alıntı sayısı: {len(quotes)}")
        return True
    except Exception as e:
        print_error(f"Page Action Hatası: {e}")
        return False


def test_adaptive_selectors():
    """6. Kendi Kendini Onaran (Adaptive) Seçici Testi"""
    print_section("6. Kendi Kendini Onaran (Adaptive / Relocate) Seçici Testi")
    print_info("Orijinal HTML DOM yapısı taranıyor...")

    html_v1 = """
    <div id="container">
        <button id="btn-submit" class="primary-btn btn-large" data-role="checkout">Sepeti Onayla</button>
    </div>
    """
    sel_v1 = Selector(html_v1, url="https://magaza.com")
    btn_v1 = sel_v1.find("button", id="btn-submit")
    print_success(f"Sürüm 1 bulundu: <{btn_v1.tag} class='{btn_v1.attrib.get('class')}'>{btn_v1.text}</button>")

    print_info("Sitenin arayüz güncellediğini varsayıyoruz (ID ve Class isimleri değişti)...")
    html_v2 = """
    <div id="wrapper">
        <div class="new-layout">
            <!-- ID kalktı, class ismi değişti, ancak metin ve data-role aynı -->
            <button class="cta-button-v2 modern" data-role="checkout">Sepeti Onayla</button>
        </div>
    </div>
    """
    sel_v2 = Selector(html_v2, url="https://magaza.com")

    print_info("Relocate mekanizması benzerlik skoru hesaplayarak yeni öğeyi arıyor...")
    relocated = sel_v2.relocate(btn_v1, percentage=35, selector_type=True)

    if relocated:
        found = relocated[0]
        print_success(f"Yeni öğe başarıyla bulundu!: Metin='{found.text}' | Class='{found.attrib.get('class')}'")
        return True
    else:
        print_warning("Öğe benzerlik eşiğinin altında kaldı.")
        return False


def test_spider_crawler():
    """7. Spider / Crawler Çerçevesi Testi"""
    print_section("7. Büyük Ölçekli Tarama: Dahili Spider / Crawler Testi")
    print_info("Mini crawler başlatılıyor (quotes.toscrape.com)...")

    class TestSpider(Spider):
        name = "test_crawler"
        start_urls = ["https://quotes.toscrape.com/"]
        concurrent_requests = 1
        max_requests = 2  # Test amaçlı sadece 2 istek

        async def parse(self, response):
            for quote in response.css("div.quote")[:2]:
                yield {
                    "yazar": quote.css("small.author::text").get(),
                    "metin": quote.css("span.text::text").get()[:50] + "...",
                }

            # Sonraki sayfaya geç
            next_page = response.css("li.next a::attr(href)").get()
            if next_page:
                yield Request(url=response.urljoin(next_page), callback=self.parse)

    try:
        spider = TestSpider()
        result = spider.start()
        print_success(f"Tarama Tamamlandı! Toplanan Veri Adedi: {len(result.items)}")
        for idx, item in enumerate(result.items):
            print(f"  [{idx + 1}] {item['yazar']}: \"{item['metin']}\"")
        return True
    except Exception as e:
        print_error(f"Spider Hatası: {e}")
        return False


def test_markdown_conversion(url: str = "https://news.ycombinator.com"):
    """8. AI / Markdown Dönüştürme Testi"""
    print_section(f"8. AI & RAG Testi: Sayfayı Markdown Formatına Dönüştürme -> {url}")
    print_info("Sayfa indiriliyor ve AI için temiz Markdown'a dönüştürülüyor...")
    try:
        page = Fetcher.get(url, timeout=15)
        md = page.markdown()

        print_success(f"Markdown Dönüşümü Başarılı! (Karakter Sayısı: {len(md)})")
        print(f"\n{Colors.BOLD}--- Markdown Önizlemesi (İlk 300 Karakter) ---{Colors.RESET}")
        print(md[:300].strip())
        print(f"{Colors.BOLD}--- Önizleme Sonu ---{Colors.RESET}")
        return True
    except Exception as e:
        print_error(f"Markdown Dönüştürme Hatası: {e}")
        return False


def launch_interactive_repl(url: str = "https://quotes.toscrape.com"):
    """9. Canlı Etkileşimli Python/IPython Kabuğu"""
    print_section(f"9. Canlı Etkileşimli Kazıma Konsolu -> {url}")
    print_info(f"'{url}' adresi indiriliyor ve değişkenler hazırlandıktan sonra kabuk açılacak...")
    try:
        page = Fetcher.get(url, timeout=15)
        print_success("Sayfa yüklendi! Hazır Değişkenler: 'page', 'Fetcher', 'StealthyFetcher', 'Selector'")
        print_info("Çıkmak için: exit() yazıp Enter'a basabilirsiniz.\n")

        scope = {
            "page": page,
            "response": page,
            "Fetcher": Fetcher,
            "AsyncFetcher": AsyncFetcher,
            "DynamicFetcher": DynamicFetcher,
            "StealthyFetcher": StealthyFetcher,
            "Selector": Selector,
            "scrapecore": scrapecore,
        }

        try:
            import IPython
            IPython.start_ipython(argv=[], user_ns=scope)
        except ImportError:
            import code
            code.interact(banner="ScrapeCore Python Shell Hazır:", local=scope)
    except Exception as e:
        print_error(f"Konsol Hatası: {e}")


def test_xhr_capture(url: str = "https://quotes.toscrape.com/js/"):
    """10. Canlı Fetch/XHR Ağ Paketlerini İzleme ve Filtreleme Testi"""
    print_section(f"10. Canlı Fetch/XHR Ağ Paketlerini İzleme & Kazıma -> {url}")
    print_info("Headless tarayıcı başlatılıyor ve Fetch/XHR ağ paketleri dinleniyor...")
    start = time.perf_counter()
    try:
        # capture_xhr=True ile tüm XHR/Fetch çağrılarını yakalayalım
        page = DynamicFetcher.fetch(
            url,
            headless=True,
            network_idle=True,
            capture_xhr=True,
            timeout=35000,
        )
        elapsed = (time.perf_counter() - start) * 1000
        print_success(f"Sayfa ve Ağ Paketleri Yakalandı: HTTP {page.status} ({elapsed:.1f} ms)")

        captured = page.captured_xhr
        print_success(f"Toplam {len(captured)} adet Fetch/XHR ağ paketi yakalandı!")

        if captured:
            print(f"\n{Colors.BOLD}--- Yakalanan İlk Ağ Paketleri (Maks. 5 Adet) ---{Colors.RESET}")
            for idx, req in enumerate(captured[:5]):
                method = getattr(req, "method", "GET")
                res_type = req.resource_type or "xhr/fetch"
                content_len = len(req.body)
                print(f"  [{idx + 1}] {Colors.CYAN}{method}{Colors.RESET} {Colors.GREEN}{req.status}{Colors.RESET} ({res_type}, {content_len} B) -> {req.url}")
            print(f"{Colors.BOLD}-------------------------------------------------{Colors.RESET}\n")

            # XHR URL listesi kontrolü
            urls = page.xhr_urls
            print_info(f"page.xhr_urls listesi: {len(urls)} adet URL içeriyor.")

            # Filtreleme testi (filter_xhr ve find_xhr)
            json_requests = page.filter_xhr(lambda r: "json" in r.url.lower() or "api" in r.url.lower() or "application/json" in str(r.headers).lower())
            if json_requests:
                print_success(f"Filtrelenmiş JSON/API paket sayısı: {len(json_requests)}")
                target = json_requests[0]
                print_info(f"Örnek API Yanıtı: <{target.method} {target.url}>")
                try:
                    data = target.json()
                    print_success(f"JSON verisi başarıyla ayrıştırıldı! Anahtar sayısı: {len(data) if isinstance(data, (dict, list)) else 'N/A'}")
                except Exception:
                    print_info(f"Ham Yanıt Gövdesi (İlk 100 bayt): {target.body[:100]}")
            else:
                first_req = page.find_xhr()
                if first_req:
                    print_info(f"İlk yakalanan XHR isteği: <{first_req.method} {first_req.url}> (Durum: {first_req.status})")

            # POST data kontrolü
            post_requests = page.filter_xhr(method="POST")
            if post_requests:
                print_info(f"Yakalanan POST istek sayısı: {len(post_requests)}")
                for pr in post_requests[:2]:
                    print(f"  POST URL: {pr.url} | Gövde: {pr.post_data}")

        return True
    except Exception as e:
        print_error(f"Fetch/XHR İzleme Hatası: {e}")
        print_warning("Not: Chromium yüklü değilse terminalden 'scrapecore install' çalıştırın.")
        return False


def run_all_diagnostics():
    """Tam Sistem Sağlık Kontrolü (Tüm Özelliklerin Sıralı Testi)"""
    print_section("TÜM SİSTEM SAĞLIK VE FONKSİYONEL TANILAMA")
    results = {}

    print_info("Adım 1/9: Statik Fetcher Test Ediliyor...")
    results["Statik Fetcher (curl_cffi)"] = test_static_fetcher()

    print_info("Adım 2/9: Asenkron Fetcher Test Ediliyor...")
    results["Asenkron Fetcher (AsyncFetcher)"] = test_async_fetcher()

    print_info("Adım 3/9: Dinamik Fetcher (Playwright) Test Ediliyor...")
    results["Dinamik Tarayıcı (Playwright)"] = test_dynamic_fetcher()

    print_info("Adım 4/9: Görünmez Tarayıcı (StealthyFetcher) Test Ediliyor...")
    results["Görünmez Tarayıcı (Patchright / CF)"] = test_stealthy_fetcher()

    print_info("Adım 5/9: Sayfa İçi Otomasyon Test Ediliyor...")
    results["Sayfa İçi Otomasyon (page_action)"] = test_page_action()

    print_info("Adım 6/9: Adaptif Seçici Test Ediliyor...")
    results["Kendi Kendini Onaran Seçiciler"] = test_adaptive_selectors()

    print_info("Adım 7/9: Spider / Crawler Motoru Test Ediliyor...")
    results["Spider & Crawler Çerçevesi"] = test_spider_crawler()

    print_info("Adım 8/9: AI / Markdown Dönüştürücü Test Ediliyor...")
    results["AI / Markdown Dönüştürücü"] = test_markdown_conversion()

    print_info("Adım 9/9: Fetch/XHR Ağ Paketlerini İzleme Test Ediliyor...")
    results["Fetch/XHR Ağ Paketlerini İzleme & Kazıma"] = test_xhr_capture()

    # Rapor Özeti
    print("\n" + "=" * 60)
    print(f"{Colors.BOLD}📊 GENEL TEST VE SAĞLIK RAPORU:{Colors.RESET}")
    print("=" * 60)
    all_passed = True
    for feature, status in results.items():
        if status:
            print(f"  {Colors.GREEN}✓ BAŞARILI{Colors.RESET}   : {feature}")
        else:
            print(f"  {Colors.RED}✗ BAŞARISIZ{Colors.RESET}  : {feature}")
            all_passed = False

    print("-" * 60)
    if all_passed:
        print_success("TEBRİKLER! Tüm ScrapeCore bileşenleri %100 sorunsuz çalışıyor.")
    else:
        print_warning("Bazı testlerde uyarılar veya başarısızlıklar oluştu. Ağ bağlantınızı veya tarayıcı ikililerini kontrol edin.")
    print("=" * 60 + "\n")


# ==============================================================================
# İnteraktif Ana Menü
# ==============================================================================

def interactive_menu():
    """Kullanıcıya interaktif seçim menüsü sunar"""
    while True:
        print_banner()
        print(f"{Colors.BOLD}Lütfen test etmek istediğiniz özelliği seçin:{Colors.RESET}\n")
        print(f"  {Colors.CYAN}[1]{Colors.RESET} Statik İstek & CSS/XPath Ayrıştırma (Fetcher)")
        print(f"  {Colors.CYAN}[2]{Colors.RESET} Eşzamanlı Asenkron İstekler (AsyncFetcher)")
        print(f"  {Colors.CYAN}[3]{Colors.RESET} JavaScript SPA Render (DynamicFetcher / Playwright)")
        print(f"  {Colors.CYAN}[4]{Colors.RESET} Görünmez Tarayıcı & Cloudflare Bypass (StealthyFetcher)")
        print(f"  {Colors.CYAN}[5]{Colors.RESET} Sayfa İçi Otomasyon (page_action: Tıklama / Kaydırma)")
        print(f"  {Colors.CYAN}[6]{Colors.RESET} Kendi Kendini Onaran Seçiciler (Adaptive & Relocate)")
        print(f"  {Colors.CYAN}[7]{Colors.RESET} Büyük Ölçekli Tarama: Spider / Crawler Motoru")
        print(f"  {Colors.CYAN}[8]{Colors.RESET} AI / RAG Temiz Markdown Dönüştürücü")
        print(f"  {Colors.CYAN}[9]{Colors.RESET} Canlı Etkileşimli Kabuk (Interactive REPL)")
        print(f"  {Colors.CYAN}[10]{Colors.RESET} 🔥 Canlı Fetch/XHR Ağ Paketlerini İzleme & Kazıma (capture_xhr)")
        print(f"  {Colors.CYAN}[11]{Colors.RESET} 🚀 TÜM ÖZELLİKLERİ SIRAYLA TEST ET (Tam Sağlık Kontrolü)")
        print(f"  {Colors.RED}[0]{Colors.RESET} Çıkış\n")

        secim = input(f"{Colors.BOLD}Seçiminiz [0-11]: {Colors.RESET}").strip()

        if secim == "0":
            print_info("ScrapeCore Playground'dan çıkılıyor. İyi çalışmalar!")
            break
        elif secim == "1":
            custom_url = input("Test edilecek URL (Varsayılan için Enter): ").strip()
            test_static_fetcher(custom_url or "https://quotes.toscrape.com")
        elif secim == "2":
            test_async_fetcher()
        elif secim == "3":
            custom_url = input("Test edilecek JS sitesi (Varsayılan için Enter): ").strip()
            test_dynamic_fetcher(custom_url or "https://quotes.toscrape.com/js/")
        elif secim == "4":
            custom_url = input("Test edilecek korumalı site (Varsayılan için Enter): ").strip()
            test_stealthy_fetcher(custom_url or "https://nowsecure.nl")
        elif secim == "5":
            test_page_action()
        elif secim == "6":
            test_adaptive_selectors()
        elif secim == "7":
            test_spider_crawler()
        elif secim == "8":
            custom_url = input("Markdown'a çevrilecek URL (Varsayılan için Enter): ").strip()
            test_markdown_conversion(custom_url or "https://news.ycombinator.com")
        elif secim == "9":
            custom_url = input("Kabuğa yüklenecek URL (Varsayılan için Enter): ").strip()
            launch_interactive_repl(custom_url or "https://quotes.toscrape.com")
        elif secim == "10":
            custom_url = input("XHR paketleri izlenecek URL (Varsayılan için Enter): ").strip()
            test_xhr_capture(custom_url or "https://quotes.toscrape.com/js/")
        elif secim == "11":
            run_all_diagnostics()
        else:
            print_warning("Geçersiz seçim! Lütfen 0 ile 11 arasında bir rakam girin.")

        input(f"\n{Colors.DIM}Devam etmek için Enter tuşuna basın...{Colors.RESET}")


# ==============================================================================
# Komut Satırı Argüman Girişi (CLI)
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="ScrapeCore - Kapsamlı Test & Deneyim Ortamı (Playground)"
    )
    parser.add_argument(
        "--test-all",
        action="store_true",
        help="Tüm modül ve motorları sırayla otomatik test eder.",
    )
    parser.add_argument(
        "--fetch",
        metavar="URL",
        type=str,
        help="Verilen URL adresini Fetcher ile indirir ve özetler.",
    )
    parser.add_argument(
        "--stealth",
        metavar="URL",
        type=str,
        help="Verilen URL adresini StealthyFetcher ile indirir.",
    )
    parser.add_argument(
        "--markdown",
        metavar="URL",
        type=str,
        help="Verilen URL içeriğini Markdown formatına dönüştürür.",
    )
    parser.add_argument(
        "--xhr",
        metavar="URL",
        nargs="?",
        const="https://quotes.toscrape.com/js/",
        help="Verilen URL'deki Fetch/XHR ağ paketlerini yakalar ve analiz eder.",
    )
    parser.add_argument(
        "--shell",
        nargs="?",
        const="https://quotes.toscrape.com",
        help="Etkileşimli ScrapeCore kabuğunu başlatır.",
    )

    args = parser.parse_args()

    if args.test_all:
        print_banner()
        run_all_diagnostics()
    elif args.fetch:
        print_banner()
        test_static_fetcher(args.fetch)
    elif args.stealth:
        print_banner()
        test_stealthy_fetcher(args.stealth)
    elif args.markdown:
        print_banner()
        test_markdown_conversion(args.markdown)
    elif args.xhr:
        print_banner()
        test_xhr_capture(args.xhr)
    elif args.shell:
        print_banner()
        launch_interactive_repl(args.shell)
    else:
        # Parametre verilmemişse etkileşimli menüyü aç
        interactive_menu()


if __name__ == "__main__":
    main()
