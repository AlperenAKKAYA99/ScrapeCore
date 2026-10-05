# 🕷️ ScrapeCore

> **Biblioteca de Web Scraping Invisível, Rápida e Inteligente para a Web Moderna**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Idiomas / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <b>🇧🇷 Português (Brasil)</b> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <a href="readme_fr.md">🇫🇷 Français</a> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** é uma biblioteca de web scraping de nova geração para Python, projetada para contornar proteções avançadas contra bots (Cloudflare Turnstile, DataDome, WAFs, etc.), realizar análise DOM de altíssimo desempenho, monitorar pacotes de rede Fetch/XHR em tempo real e orquestrar rastreamento assíncrono em larga escala com facilidade.

> **Aviso de Licença e Fork:**
> Este projeto é ativamente desenvolvido e mantido por **Alperen AKKAYA**. A arquitetura central é baseada na biblioteca Scrapling desenvolvida por Karim Shoair, bifurcada e desenvolvida de forma independente sob os termos da licença **BSD-3-Clause**, respeitando integralmente os direitos autorais originais.

---

## 🚀 Recursos em Destaque

* 🛡️ **Motor Furtivo Avançado (Stealth Engine):** Simulação fidedigna de impressões digitais TLS/JA3 e cabeçalhos de navegador reais via `patchright`, `curl_cffi` e `browserforge`.
* 📡 **Monitoramento e Raspagem de Pacotes Fetch/XHR:** Intercepte todas as requisições AJAX, Fetch e JSON em segundo plano (`capture_xhr=True`) e extraia dados estruturados diretamente, sem necessidade de analisar o HTML.
* 🧩 **Resolução Automática do Cloudflare Turnstile:** Supere telas de validação Turnstile e verificações intersticiais com um único parâmetro (`solve_cloudflare=True`).
* ⚡ **Analisador DOM Ultrarrápido:** Motor unificado `Selector` otimizado sobre `lxml` e `cssselect`, operando com velocidade muito superior ao BeautifulSoup.
* 🔄 **Seletores Autocicatrizantes (Adaptive):** Mecanismo inteligente `relocate` capaz de reencontrar elementos por similaridade estrutural mesmo após mudanças no layout da página.
* 🕷️ **Estrutura Completa de Spiders e Crawlers:** Rastreamento assíncrono com controle automático de taxa (autothrottle), gestão de sessões, conformidade com robots.txt e pontos de recuperação (checkpoints).
* 🤖 **Pronto para IA e MCP:** Servidor Model Context Protocol (`scrapecore-mcp`) nativo para agentes de IA/LLMs e conversor limpo de HTML para Markdown para pipelines de RAG.
* 💻 **Console Interativo e Laboratório de Testes:** Ambiente REPL dinâmico com `scrapecore shell` e suíte de testes `ScrapeCore.py`.

---

## 📦 Instalação e Compatibilidade de Plataformas (Windows & Linux / macOS)

O ScrapeCore é 100% compatível com **Windows**, **Linux** (Ubuntu, Debian, Fedora, Arch, CentOS, etc.) e **macOS**. Compatível com Python 3.10 ou superior (Recomendado: **Python 3.13**).

### 1. Preparar Ambiente Virtual

**🪟 Windows (PowerShell / CMD):**
```powershell
# Criar ambiente virtual
python -m venv .venv

# Ativar no PowerShell
.\.venv\Scripts\Activate.ps1

# (Se estiver usando CMD)
.\.venv\Scripts\activate.bat
```

**🐧 Linux & 🍎 macOS (Bash / Zsh):**
```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate
```

---

### 2. Instalar Dependências

Instale todos os motores centrais, automação de navegadores e ferramentas de IA:

**Windows e Linux:**
```bash
pip install -r requirements.txt
```

---

### 3. Instalar Binários do Navegador e Bibliotecas do Sistema

Instale os binários do Chromium necessários para os motores dinâmicos e invisíveis (`Playwright` / `Patchright`):

**🪟 Windows:**
```powershell
scrapecore install
# ou
playwright install chromium
```

**🐧 Linux (Servidores, Docker e Distribuições):**
> 💡 *Em servidores Linux sem interface gráfica (Ubuntu/Debian, etc.), o Chromium requer bibliotecas compartilhadas do sistema operacional para rodar em modo headless:*
```bash
# Instalar Chromium com as bibliotecas do sistema necessárias
playwright install --with-deps chromium
# ou via comando integrado
scrapecore install
```

---

### 4. Laboratório de Testes e Playground (`ScrapeCore.py`)

Execute o laboratório de testes e diagnósticos para experimentar todos os recursos:

**🪟 Windows:**
```powershell
python ScrapeCore.py
```

**🐧 Linux & 🍎 macOS:**
```bash
python3 ScrapeCore.py
```
*(Ver parâmetros disponíveis: `python3 ScrapeCore.py --help`)*

---

## 📖 Guia de Uso Completo

### 1. Início Rápido (Quickstart)

```python
from scrapecore import Fetcher

# Requisição GET rápida baseada em curl_cffi com personificação de TLS
page = Fetcher.get("https://quotes.toscrape.com")

print("Código de Status:", page.status)

# Extrair texto da primeira citação com seletor CSS
first_quote = page.css("span.text::text").get()
print("Citação:", first_quote)

# Listar todos os autores
authors = page.css("small.author::text").getall()
print(f"Total de autores: {len(authors)}: {authors[:3]}")
```

---

### 2. Motores de Requisição (Guia de Fetchers)

O ScrapeCore oferece 4 motores especializados de acordo com a sofisticação do site alvo:

| Motor | Base | Finalidade | Suporta JavaScript? | Defesa Anti-Bot |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | HTML estático, APIs REST, máxima velocidade | ❌ | Moderada (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | Requisições assíncronas concorrentes | ❌ | Moderada (TLS/JA3) |
| `DynamicFetcher` | `playwright` | SPAs e páginas com renderização pesada em JS | ✅ | Padrão |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome e barreiras rigorosas | ✅ | **Máxima (Invisível)** |

#### A. Requisições Estáticas de Alta Performance (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Requisição síncrona
res = Fetcher.get("https://httpbin.org/headers", headers={"Cabecalho-Customizado": "Valor"})
print(res.json())

# Requisição assíncrona
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. Páginas Dinâmicas com JavaScript (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Aguarda o término da atividade de rede
)

print(page.css("span.text::text").get())
```

#### C. Evasão Avançada de Cloudflare e Bots (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Site protegido por Cloudflare
    solve_cloudflare=True,              # Resolve desafios Turnstile automaticamente
    headless=True,                      # Executa em segundo plano
    block_ads=True,                     # Bloqueia mais de 3500 domínios de rastreamento
    disable_resources=True,             # Ignora imagens e fontes para triplicar a velocidade
    timeout=60000                       # Timeout de 60s
)

print("Acesso realizado com sucesso! Título:", page.css("h1::text").get())
```

#### D. Automação na Página (`page_action`)

```python
from scrapecore import StealthyFetcher

def rolagem_infinita(page):
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=rolagem_infinita
)
```

---

### 3. Extração de Dados e Seletores

Cada fetcher retorna um objeto **`Response`** que herda diretamente de `Selector`.

#### Seletores CSS e XPath
```python
# Extrair texto com CSS
titulo = page.css("h1.main-title::text").get()

# Extrair lista de links
links = page.css("div.menu a::attr(href)").getall()

# Suporte completo a XPath
paragrafos = page.xpath("//div[@id='content']//p/text()").getall()
```

#### Localização Estilo BeautifulSoup (`find` & `find_all`)
```python
header = page.find("h1", class_="title")
print(header.text)

botoes = page.find_all("button", type="submit")
for btn in botoes:
    print(btn.attrib.get("id"))
```

#### Limpeza Inteligente de Texto (`clean_text`)
```python
elemento = page.css("div.descricao").first
print(elemento.clean_text())
```

#### Seletores Autocicatrizantes (Adaptive)
```python
# Registra a assinatura estrutural no banco SQLite local
page.css("button.comprar", adaptive=True, auto_save=True)

# Mesmo que a classe CSS mude no futuro, o ScrapeCore reencontra o elemento
botao = page.css("button.comprar", adaptive=True)
```

---

### 4. Monitoramento e Raspagem de Pacotes Fetch/XHR

Aplicações web modernas com frequência não entregam dados no HTML bruto, mas sim via requisições de API em segundo plano. Capturar esses pacotes de rede é **muito mais rápido, resiliente e entrega dados JSON limpos**.

#### A. Captura Básica (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Habilita a captura de pacotes de rede
)

print(f"Total de requisições capturadas: {len(page.captured_xhr)}")
print(f"URLs interceptadas: {page.xhr_urls}")
```

#### B. Filtragem com Regex ou Callables

```python
# 1. Filtro com expressão regular:
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Filtro com função personalizada:
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. Métodos para Consulta XHR no `Response`

| Propriedade / Método | Descrição |
| :--- | :--- |
| `page.captured_xhr` | Lista de objetos `Response` interceptados |
| `page.xhr_urls` | Lista de todas as URLs capturadas (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Retorna o **primeiro** pacote correspondente (ou `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Retorna **todos** os pacotes correspondentes (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | Converte diretamente o corpo do pacote em JSON |
| `xhr.post_data` / `xhr.request_data` | Dados ou corpo POST enviado pelo cliente |
| `xhr.resource_type` | Tipo de recurso no Playwright (`"xhr"` ou `"fetch"`) |
| `xhr.method` | Método HTTP (`"GET"`, `"POST"`, etc.) |

#### Exemplo: Extraindo JSON Diretamente da API Interceptada

```python
# Obter dados JSON sem analisar HTML
dados_produtos = page.xhr_json(r"/api/products\?category=electronics")
if dados_produtos:
    for item in dados_produtos.get("items", []):
        print(item["name"], item["price"])

# Inspecionar requisições POST e payloads enviados
requisicoes_post = page.filter_xhr(method="POST", status=200)
for req in requisicoes_post:
    print(f"URL POST: {req.url}")
    print(f"Corpo enviado: {req.post_data}")
    print(f"Resposta JSON: {req.json()}")
```

#### D. Uso na Linha de Comando (CLI) e no Playground

```powershell
# Interceptar pacotes XHR pela CLI:
scrapecore extract fetch "https://quotes.toscrape.com/js/" saida.html --capture-xhr

# Testar interativamente no laboratório de diagnósticos:
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Rastreamento em Larga Escala: Framework Spiders

```python
from scrapecore.spiders import Spider, Request

class LivrosSpider(Spider):
    name = "livros_bot"
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
    spider = LivrosSpider()
    resultado = spider.start()
    print(f"Total de {len(resultado.items)} livros coletados!")
```

---

### 6. Gestão de Sessões e Rotação de Proxies

```python
from scrapecore.fetchers import FetcherSession, ProxyRotator

rotator = ProxyRotator([
    "http://usuario:senha@proxy1.com:8000",
    "http://usuario:senha@proxy2.com:8000",
])

session = FetcherSession(proxy=rotator)
session.post("https://example.com/login", data={"user": "admin", "pass": "segredo"})

dashboard = session.get("https://example.com/dashboard")
print(dashboard.css("h2::text").get())
```

---

### 7. Inteligência Artificial e Servidor MCP

```powershell
# Iniciar servidor MCP em modo stdio
scrapecore-mcp

# Ou em modo HTTP na rede
scrapecore-mcp --http --port 8000
```

#### Conversão para Markdown para Pipelines de RAG
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o noticias.md
```

---

### 8. Linha de Comando (Guia CLI)

#### Shell Interativo (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### Extração Direta para Arquivo (`scrapecore extract`)
```powershell
# Extrair seletor CSS para arquivo
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o citacoes.txt

# Extrair com navegador invisível e bypass de Cloudflare
scrapecore extract stealthy-fetch "https://site-protegido.com" --solve-cloudflare -o pagina.html
```

---

## 📁 Estrutura de Diretórios

```
ScrapeCore/
│
├── lang/                       # Documentação multilíngue
│   ├── readme_en.md            # Inglês
│   ├── readme_es.md            # Espanhol
│   ├── readme_pt-br.md         # Português (Brasil)
│   ├── readme_zh.md            # Chinês Simplificado
│   ├── readme_ja.md            # Japonês
│   ├── readme_de.md            # Alemão
│   ├── readme_fr.md            # Francês
│   ├── readme_ru.md            # Russo
│   ├── readme_ko.md            # Coreano
│   └── readme_ar.md            # Árabe
│
├── scrapecore/                 # Código-fonte da biblioteca
├── tests/                      # Testes unitários e de integração
├── .venv/                      # Ambiente virtual Python 3.13
├── pyproject.toml              # Empacotamento e dependências
├── requirements.txt            # Dependências de instalação
├── LICENSE                     # Licença BSD-3 (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # Laboratório de testes e diagnóstico
└── README.md                   # Documentação principal (Turco)
```

---

## 🙏 Agradecimentos e Créditos

Este projeto é construído a partir do trabalho fundamental de **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))**, desenvolvedor da biblioteca **[Scrapling](https://github.com/D4Vinci/Scrapling)**.

* **Repositório Original:** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Autor Original:** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Licença Original:** BSD 3-Clause License

Expressamos nossa sincera gratidão a Karim Shoair e à comunidade de código aberto por criarem esta arquitetura inovadora. O ScrapeCore dá continuidade a essa base com desenvolvimento independente e novas capacidades.

---

## ⚖️ Licença

Este projeto é distribuído sob os termos da **Licença BSD 3-Clause**:

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

Consulte o arquivo [LICENSE](../LICENSE) para obter mais informações.
