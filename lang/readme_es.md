# 🕷️ ScrapeCore

> **Biblioteca de Web Scraping Invisible, Rápida e Inteligente para la Web Moderna**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Idiomas / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <b>🇪🇸 Español</b> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** es una biblioteca de web scraping de última generación en Python, diseñada para evadir sistemas modernos de protección contra bots (Cloudflare Turnstile, DataDome, WAF, etc.), ejecutar análisis DOM de ultra alto rendimiento, monitorear paquetes de red Fetch/XHR en tiempo real y realizar rastreo asíncrono a gran escala de forma sencilla.

> **Aviso de Licencia y Bifurcación (Fork):**
> Este proyecto es desarrollado y mantenido por **Alperen AKKAYA**. La arquitectura central se basa en la biblioteca Scrapling creada por Karim Shoair, bifurcada y desarrollada de forma independiente bajo los términos de la licencia **BSD-3-Clause**, preservando en su totalidad los derechos de autor originales.

---

## 🚀 Características Principales

* 🛡️ **Motor Sigiloso Avanzado (Stealth Engine):** Simulación hiperrealista de huellas digitales TLS/JA3 y cabeceras de navegador mediante `patchright`, `curl_cffi` y `browserforge`.
* 📡 **Monitoreo y Extracción de Paquetes Fetch/XHR:** Intercepta todas las llamadas de red AJAX, Fetch y JSON de fondo (`capture_xhr=True`) para extraer datos directamente sin necesidad de analizar el HTML.
* 🧩 **Resolución Automática de Cloudflare Turnstile:** Resuelve desafíos de verificación Turnstile e pantallas intersticiales con un único parámetro (`solve_cloudflare=True`).
* ⚡ **Analizador DOM Ultrarrápido:** Motor unificado `Selector` optimizado sobre `lxml` y `cssselect`, con un rendimiento muy superior a BeautifulSoup.
* 🔄 **Selectores Autoreparables (Adaptive):** Algoritmo inteligente `relocate` capaz de reencontrar elementos mediante similitud estructural incluso tras cambios de diseño web.
* 🕷️ **Marco de Trabajo para Spiders y Crawlers:** Rastreo asíncrono con control automático de frecuencia (autothrottle), gestión de sesiones, soporte para robots.txt y puntos de control (checkpointing).
* 🤖 **Integración con IA y MCP:** Servidor Model Context Protocol (`scrapecore-mcp`) nativo para agentes de IA/LLMs y conversor limpio de HTML a Markdown para pipelines RAG.
* 💻 **Consola Interactiva y Laboratorio de Pruebas:** Entorno REPL en vivo vía `scrapecore shell` y suite de diagnóstico `ScrapeCore.py`.

---

## 📦 Instalación y Compatibilidad de Plataformas (Windows & Linux / macOS)

ScrapeCore es 100% compatible con **Windows**, **Linux** (Ubuntu, Debian, Fedora, Arch, CentOS, etc.) y **macOS**. Admite Python 3.10 o superior (Recomendado: **Python 3.13**).

### 1. Preparar Entorno Virtual

**🪟 Windows (PowerShell / CMD):**
```powershell
# Crear entorno virtual
python -m venv .venv

# Activar en PowerShell
.\.venv\Scripts\Activate.ps1

# (Si usa CMD)
.\.venv\Scripts\activate.bat
```

**🐧 Linux & 🍎 macOS (Bash / Zsh):**
```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate
```

---

### 2. Instalar Dependencias

Instale todos los motores principales, automatización de navegadores y herramientas de IA:

**Windows y Linux:**
```bash
pip install -r requirements.txt
```

---

### 3. Instalar Binarios de Navegador y Bibliotecas del Sistema

Instale los binarios de Chromium requeridos para los motores dinámicos y sigilosos (`Playwright` / `Patchright`):

**🪟 Windows:**
```powershell
scrapecore install
# o
playwright install chromium
```

**🐧 Linux (Servidores, Docker y Distribuciones):**
> 💡 *En servidores Linux sin entorno gráfico (Ubuntu/Debian, etc.), Chromium requiere bibliotecas compartidas del sistema operativo para funcionar en modo headless:*
```bash
# Instalar Chromium con las bibliotecas de sistema necesarias
playwright install --with-deps chromium
# o mediante el comando integrado
scrapecore install
```

---

### 4. Laboratorio de Pruebas Interactivo (`ScrapeCore.py`)

Inicie el laboratorio interactivo para probar todas las funciones:

**🪟 Windows:**
```powershell
python ScrapeCore.py
```

**🐧 Linux & 🍎 macOS:**
```bash
python3 ScrapeCore.py
```
*(Ver parámetros disponibles: `python3 ScrapeCore.py --help`)*

---

## 📖 Guía de Uso Completa

### 1. Inicio Rápido (Quickstart)

```python
from scrapecore import Fetcher

# Petición GET rápida basada en curl_cffi con suplantación de TLS
page = Fetcher.get("https://quotes.toscrape.com")

print("Código de Estado:", page.status)

# Extraer el texto de la primera cita con selector CSS
first_quote = page.css("span.text::text").get()
print("Cita:", first_quote)

# Listar todos los autores
authors = page.css("small.author::text").getall()
print(f"Total de autores: {len(authors)}: {authors[:3]}")
```

---

### 2. Motores de Petición (Guía de Fetchers)

ScrapeCore incluye 4 motores especializados según la complejidad de la página objetivo:

| Motor | Base | Caso de Uso | ¿JavaScript? | Protección Anti-Bot |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | HTML estático, APIs REST, máxima velocidad | ❌ | Moderada (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | Peticiones asíncronas masivas concurrentes | ❌ | Moderada (TLS/JA3) |
| `DynamicFetcher` | `playwright` | Aplicaciones de Página Única (SPA), renderizado JS | ✅ | Estándar |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome, defensas anti-bot estrictas | ✅ | **Máxima (Invisible)** |

#### A. Peticiones Estáticas Ultrarrápidas (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Petición síncrona
res = Fetcher.get("https://httpbin.org/headers", headers={"Cabecera-Personalizada": "Valor"})
print(res.json())

# Petición asíncrona
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. Páginas con Renderizado JavaScript (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Esperar a que cese la actividad de red
)

print(page.css("span.text::text").get())
```

#### C. Evasión Avanzada de Anti-Bot y Cloudflare (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Sitio demo protegido por Cloudflare
    solve_cloudflare=True,              # Resolver Turnstile automáticamente
    headless=True,                      # Ejecutar en segundo plano
    block_ads=True,                     # Bloquear más de 3500 dominios de anuncios
    disable_resources=True,             # Omitir imágenes y fuentes para triplicar la velocidad
    timeout=60000                       # Tiempo de espera de 60s
)

print("¡Acceso exitoso! Título:", page.css("h1::text").get())
```

#### D. Automatización en Página (`page_action`)

```python
from scrapecore import StealthyFetcher

def desplazamiento_infinito(page):
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=desplazamiento_infinito
)
```

---

### 3. Extracción de Datos y Selectores

Cada fetcher devuelve un objeto **`Response`** que hereda de `Selector`.

#### Selectores CSS y XPath
```python
# Extracción de texto único con CSS
titulo = page.css("h1.main-title::text").get()

# Extracción de lista de atributos
enlaces = page.css("div.menu a::attr(href)").getall()

# Soporte completo de XPath
parrafos = page.xpath("//div[@id='content']//p/text()").getall()
```

#### Búsqueda al Estilo BeautifulSoup (`find` & `find_all`)
```python
# Encontrar primer elemento coincidente
encabezado = page.find("h1", class_="title")
print(encabezado.text)

# Encontrar todos los elementos coincidentes
botones = page.find_all("button", type="submit")
for btn in botones:
    print(btn.attrib.get("id"))
```

#### Limpieza Inteligente de Texto (`clean_text`)
```python
nodo = page.css("div.descripcion").first
print(nodo.clean_text())
```

#### Selectores Autoreparables (Adaptive)
```python
# Guardar huella estructural en base de datos SQLite local
page.css("button.comprar", adaptive=True, auto_save=True)

# Si la clase cambia en el futuro, ScrapeCore lo reubica automáticamente
boton = page.css("button.comprar", adaptive=True)
```

---

### 4. Monitoreo y Extracción de Paquetes Fetch/XHR

Las aplicaciones web modernas cargan información mediante llamadas AJAX y JSON en segundo plano. Capturar directamente estos paquetes de red es **mucho más rápido, estable y limpio** que analizar el código HTML.

#### A. Captura Básica (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Habilita la captura de paquetes de red
)

print(f"Total de paquetes capturados: {len(page.captured_xhr)}")
print(f"URLs interceptadas: {page.xhr_urls}")
```

#### B. Filtrado con Regex o Funciones

```python
# 1. Filtro por expresión regular:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Filtro mediante función personalizada:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. Métodos de Consulta XHR en `Response`

| Propiedad / Método | Descripción |
| :--- | :--- |
| `page.captured_xhr` | Lista de objetos `Response` capturados de tipo XHR/Fetch |
| `page.xhr_urls` | Lista de todas las URLs interceptadas (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Devuelve el **primer** paquete que coincide (o `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Devuelve **todos** los paquetes que coinciden (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | Decodifica directamente el cuerpo del paquete como JSON |
| `xhr.post_data` / `xhr.request_data` | Carga útil o cuerpo POST enviado por el cliente |
| `xhr.resource_type` | Tipo de recurso en Playwright (`"xhr"` o `"fetch"`) |
| `xhr.method` | Método HTTP (`"GET"`, `"POST"`, etc.) |

#### Ejemplo: Obtener Datos JSON Directamente de la API

```python
# Interceptar y decodificar la respuesta JSON de la API
datos_productos = page.xhr_json(r"/api/products\?category=electronics")
if datos_productos:
    for item in datos_productos.get("items", []):
        print(item["name"], item["price"])

# Inspeccionar peticiones POST y sus datos enviados
peticiones_post = page.filter_xhr(method="POST", status=200)
for req in peticiones_post:
    print(f"URL POST: {req.url}")
    print(f"Carga útil enviada: {req.post_data}")
    print(f"Respuesta JSON: {req.json()}")
```

#### D. Uso desde CLI y Laboratorio de Pruebas

```powershell
# Capturar paquetes XHR desde la consola CLI:
scrapecore extract fetch "https://quotes.toscrape.com/js/" salida.html --capture-xhr

# Probar la captura en vivo en el laboratorio interactivo:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Rastreo a Gran Escala: Marco Spiders

```python
from scrapecore.spiders import Spider, Request

class LibrosSpider(Spider):
    name = "libros_crawler"
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
    spider = LibrosSpider()
    resultado = spider.start()
    print(f"¡Se recolectaron {len(resultado.items)} libros!")
```

---

### 6. Gestión de Sesiones y Rotación de Proxies

```python
from scrapecore.fetchers import FetcherSession, ProxyRotator

rotator = ProxyRotator([
    "http://usuario:clave@proxy1.com:8000",
    "http://usuario:clave@proxy2.com:8000",
])

session = FetcherSession(proxy=rotator)
session.post("https://example.com/login", data={"user": "admin", "pass": "secreto"})

dashboard = session.get("https://example.com/dashboard")
print(dashboard.css("h2::text").get())
```

---

### 7. Inteligencia Artificial y Servidor MCP

```powershell
# Iniciar servidor MCP en modo stdio
scrapecore-mcp

# O iniciar servidor HTTP en red
scrapecore-mcp --http --port 8000
```

#### Conversión Limpia a Markdown para RAG
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o noticias.md
```

---

### 8. Interfaz de Línea de Comandos (CLI)

#### Consola Interactiva (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### Extracción Directa a Archivo (`scrapecore extract`)
```powershell
# Extraer selector CSS a un archivo
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o citas.txt

# Extraer con navegador sigiloso y bypass de Cloudflare
scrapecore extract stealthy-fetch "https://sitio-protegido.com" --solve-cloudflare -o pagina.html
```

---

## 📁 Estructura del Proyecto

```
ScrapeCore/
│
├── lang/                       # Documentación en múltiples idiomas
│   ├── readme_en.md            # Inglés
│   ├── readme_es.md            # Español
│   ├── readme_pt-br.md         # Portugués (Brasil)
│   ├── readme_zh.md            # Chino simplificado
│   ├── readme_ja.md            # Japonés
│   ├── readme_de.md            # Alemán
│   ├── readme_fr.md            # Francés
│   ├── readme_ru.md            # Ruso
│   ├── readme_ko.md            # Coreano
│   └── readme_ar.md            # Árabe
│
├── scrapecore/                 # Código fuente principal
├── tests/                      # Pruebas unitarias y de integración
├── .venv/                      # Entorno virtual Python 3.13
├── pyproject.toml              # Empaquetado y dependencias
├── requirements.txt            # Dependencias de instalación
├── LICENSE                     # Licencia BSD-3 (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # Laboratorio de pruebas y diagnóstico interactivo
└── README.md                   # Documentación principal (Turco)
```

---

## 🙏 Agradecimientos y Créditos

Este proyecto se fundamenta en el excelente trabajo de **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))**, creador de la biblioteca **[Scrapling](https://github.com/D4Vinci/Scrapling)**.

* **Repositorio Original:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Autor Original:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Licencia Original:** BSD 3-Clause License

Agradecemos sinceramente a Karim Shoair y a la comunidad de código abierto por sus valiosas contribuciones. ScrapeCore continúa este legado con un desarrollo independiente y mejoras continuas.

---

## ⚖️ Licencia

Este proyecto está bajo la **Licencia BSD 3-Clause**:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

Consulte el archivo [LICENSE](../LICENSE) para más detalles.
