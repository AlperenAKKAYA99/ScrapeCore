# 🕷️ ScrapeCore

> **Bibliothèque de Web Scraping Invisible, Rapide et Intelligente pour le Web Moderne**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-brightgreen.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-blueviolet.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)
[![Repository](https://img.shields.io/badge/GitHub-ScrapeCore-orange.svg)](https://github.com/AlperenAKKAYA99/ScrapeCore)

<p align="center">
  <b>🌐 Langues / Languages:</b><br>
  <a href="../README.md">🇹🇷 Türkçe</a> • 
  <a href="readme_en.md">🇬🇧 English</a> • 
  <a href="readme_es.md">🇪🇸 Español</a> • 
  <a href="readme_pt-br.md">🇧🇷 Português (Brasil)</a> • 
  <a href="readme_zh.md">🇨🇳 简体中文</a> • 
  <a href="readme_ja.md">🇯🇵 日本語</a> • 
  <a href="readme_de.md">🇩🇪 Deutsch</a> • 
  <b>🇫🇷 Français</b> • 
  <a href="readme_ru.md">🇷🇺 Русский</a> • 
  <a href="readme_ko.md">🇰🇷 한국어</a> • 
  <a href="readme_ar.md">🇸🇦 العربية</a>
</p>

**ScrapeCore** est une bibliothèque Python de web scraping de nouvelle génération, conçue pour contourner les protections anti-robots modernes (Cloudflare Turnstile, DataDome, WAFs, etc.), exécuter un parsing DOM ultra-rapide, intercepter les paquets réseau Fetch/XHR en arrière-plan pour en extraire directement les données, et orchestrer des collectes asynchrones à grande échelle.

> **Avis de Licence et de Fork :**
> Ce projet est développé et maintenu par **Alperen AKKAYA**. L'architecture fondamentale repose sur la bibliothèque Scrapling créée par Karim Shoair, forkée et développée de manière indépendante selon les termes de la licence **BSD-3-Clause**, tout en préservant l'intégralité des droits d'auteur originaux.

---

## 🚀 Fonctionnalités Clés

* 🛡️ **Moteur Furtif Avancé (Stealth Engine) :** Émulation réaliste des empreintes TLS/JA3 et des en-têtes de navigateurs grâce à `patchright`, `curl_cffi` et `browserforge`.
* 📡 **Surveillance et Extraction des Paquets Fetch/XHR :** Capturez l'ensemble des flux réseau AJAX, Fetch et JSON en arrière-plan (`capture_xhr=True`) et extrayez directement les données structurées sans analyser le code HTML.
* 🧩 **Résolution Automatique de Cloudflare Turnstile :** Franchissez automatiquement les vérifications Turnstile et les écrans interstitiels avec un simple paramètre (`solve_cloudflare=True`).
* ⚡ **Analyseur DOM Ultra-Performant :** Moteur unifié `Selector` optimisé sur `lxml` et `cssselect`, largement plus rapide que BeautifulSoup.
* 🔄 **Sélecteurs Auto-Régénérants (Adaptive) :** Algorithme intelligent `relocate` capable de retrouver des éléments par similarité structurelle même après une refonte du site.
* 🕷️ **Framework de Spiders et Crawlers Intégré :** Crawling asynchrone avec autothrottle, gestion de sessions, respect du robots.txt et points de reprise (checkpointing).
* 🤖 **Intégration IA et MCP :** Serveur Model Context Protocol (`scrapecore-mcp`) natif pour les agents d'IA et LLMs, avec convertisseur propre de HTML en Markdown pour les pipelines RAG.
* 💻 **Console Interactive et Laboratoire de Test :** Environnement REPL en direct avec `scrapecore shell` et suite de tests complète `ScrapeCore.py`.

---

## 📦 Installation (Multiplateforme)

ScrapeCore est entièrement compatible avec **Windows**, **Linux** (Ubuntu, Debian, CentOS, Arch, etc.) et **macOS**.

### 1. Préparation de l'Environnement Virtuel (Recommandé)
Compatible avec Python 3.10 et versions ultérieures (Recommandé : **Python 3.13**).

**Windows (PowerShell) :**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS (Bash / Zsh) :**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Installation des Dépendances

```bash
pip install -r requirements.txt
```

### 3. Installation des Fichiers Binaires des Navigateurs et Dépendances Système
Pour les moteurs dynamiques et furtifs (Playwright / Patchright), téléchargez Chromium et ses bibliothèques système.

**Windows :**
```powershell
scrapecore install
# ou
playwright install chromium
```

**Linux (Ubuntu/Debian / Docker / Serveurs Headless) :**
Sur les serveurs Linux, les bibliothèques système partagées peuvent être installées automatiquement :
```bash
scrapecore install
# ou avec toutes les dépendances système de l'OS :
playwright install --with-deps chromium
```

### 4. Laboratoire de Test Interactif (`ScrapeCore.py`)
Lancez le laboratoire interactif pour tester l'ensemble des fonctionnalités :

**Windows :**
```powershell
python ScrapeCore.py
```

**Linux / macOS :**
```bash
python3 ScrapeCore.py
```

---

## 📖 Guide d'Utilisation Complet

### 1. Démarrage Rapide (Quickstart)

```python
from scrapecore import Fetcher

# Requête GET ultra-rapide avec usurpation d'empreinte TLS via curl_cffi
page = Fetcher.get("https://quotes.toscrape.com")

print("Code d'état :", page.status)

# Extraire la première citation avec un sélecteur CSS
first_quote = page.css("span.text::text").get()
print("Citation :", first_quote)

# Lister l'ensemble des auteurs
authors = page.css("small.author::text").getall()
print(f"Total d'auteurs trouvés : {len(authors)}: {authors[:3]}")
```

---

### 2. Moteurs de Requête (Guide des Fetchers)

ScrapeCore dispose de 4 moteurs spécialisés selon les contraintes du site cible :

| Moteur | Technologie | Cas d'Usage | JavaScript ? | Défense Anti-Robot |
| :--- | :--- | :--- | :---: | :---: |
| `Fetcher` | `curl_cffi` | HTML statique, APIs REST, vitesse maximale | ❌ | Modérée (TLS/JA3) |
| `AsyncFetcher` | `curl_cffi` (async) | Requêtes asynchrones hautement concurrentes | ❌ | Modérée (TLS/JA3) |
| `DynamicFetcher` | `playwright` | Applications monopages (SPA), rendu JS | ✅ | Standard |
| `StealthyFetcher` | `patchright` | Cloudflare, DataDome, défenses complexes | ✅ | **Maximale (Invisible)** |

#### A. Requêtes Statiques à Haute Vitesse (`Fetcher` & `AsyncFetcher`)

```python
from scrapecore import Fetcher, AsyncFetcher
import asyncio

# Requête synchrone
res = Fetcher.get("https://httpbin.org/headers", headers={"Custom-Header": "Valeur"})
print(res.json())

# Requête asynchrone
async def main():
    res = await AsyncFetcher.get("https://quotes.toscrape.com")
    print(res.css("h1 a::text").get())

asyncio.run(main())
```

#### B. Rendu JavaScript Dynamique (`DynamicFetcher`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://quotes.toscrape.com/js/",
    headless=True,
    network_idle=True  # Attend que l'activité réseau soit calme
)

print(page.css("span.text::text").get())
```

#### C. Contournement Avancé de Cloudflare (`StealthyFetcher`)

```python
from scrapecore import StealthyFetcher

page = StealthyFetcher.fetch(
    "https://nowsecure.nl",             # Site protégé par Cloudflare
    solve_cloudflare=True,              # Résout Turnstile automatiquement
    headless=True,                      # Exécution en arrière-plan
    block_ads=True,                     # Bloque plus de 3500 domaines publicitaires
    disable_resources=True,             # Ignore images et polices pour tripler la vitesse
    timeout=60000                       # Délai d'expiration de 60s
)

print("Accès réussi ! Titre :", page.css("h1::text").get())
```

#### D. Automatisation sur la Page (`page_action`)

```python
from scrapecore import StealthyFetcher

def defilement_infini(page):
    for _ in range(3):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

page = StealthyFetcher.fetch(
    "https://example.com/feed",
    page_action=defilement_infini
)
```

---

### 3. Extraction de Données et Sélecteurs

Tous les fetchers renvoient un objet unifié **`Response`** héritant de `Selector`.

#### Sélecteurs CSS et XPath
```python
# Extraction d'un texte simple avec CSS
titre = page.css("h1.main-title::text").get()

# Extraction d'une liste d'attributs
liens = page.css("div.menu a::attr(href)").getall()

# Prise en charge intégrale de XPath
paragraphes = page.xpath("//div[@id='content']//p/text()").getall()
```

#### Recherche Façon BeautifulSoup (`find` & `find_all`)
```python
entete = page.find("h1", class_="title")
print(entete.text)

boutons = page.find_all("button", type="submit")
for btn in boutons:
    print(btn.attrib.get("id"))
```

#### Nettoyage Intelligent du Texte (`clean_text`)
```python
element = page.css("div.description").first
print(element.clean_text())
```

#### Sélecteurs Auto-Régénérants (Adaptive)
```python
# Enregistre l'empreinte structurelle dans la base SQLite locale
page.css("button.acheter", adaptive=True, auto_save=True)

# Même en cas de modification de classe CSS future, ScrapeCore relocalise l'élément
bouton = page.css("button.acheter", adaptive=True)
```

---

### 4. Surveillance et Capture des Paquets Fetch/XHR

Les sites web modernes chargent majoritairement leurs contenus via des requêtes API asynchrones en arrière-plan. Intercepter ces flux réseau directement est **nettement plus rapide, plus fiable et fournit des données JSON structurées** sans avoir à analyser le DOM HTML.

#### A. Capture Basique (`capture_xhr=True`)

```python
from scrapecore import DynamicFetcher

page = DynamicFetcher.fetch(
    "https://example.com/products",
    headless=True,
    network_idle=True,
    capture_xhr=True  # Active l'interception réseau
)

print(f"Paquets réseau interceptés : {len(page.captured_xhr)}")
print(f"URLs capturées : {page.xhr_urls}")
```

#### B. Filtrage Ciblé par Regex ou Fonctions

```python
# 1. Filtre par expression régulière :
page = DynamicFetcher.fetch("https://example.com", capture_xhr=r"/api/v\d+/")

# 2. Filtre par fonction personnalisée :
page = DynamicFetcher.fetch(
    "https://example.com",
    capture_xhr=lambda res: "products" in res.url and res.status == 200
)
```

#### C. Méthodes Disponibles sur l'Objet `Response`

| Propriété / Méthode | Description |
| :--- | :--- |
| `page.captured_xhr` | Liste des objets `Response` interceptés via XHR/Fetch |
| `page.xhr_urls` | Liste de toutes les URLs interceptées (`List[str]`) |
| `page.find_xhr(url_pattern=..., method=..., status=...)` | Renvoie le **premier** paquet correspondant (ou `None`) |
| `page.filter_xhr(url_pattern=..., method=..., status=...)` | Renvoie **tous** les paquets correspondants (`List[Response]`) |
| `page.xhr_json(url_pattern=..., default=None)` | Parse directement le corps du premier paquet trouvé en JSON |
| `xhr.post_data` / `xhr.request_data` | Données ou corps POST transmis par le client |
| `xhr.resource_type` | Type de ressource Playwright (`"xhr"` ou `"fetch"`) |
| `xhr.method` | Méthode HTTP (`"GET"`, `"POST"`, etc.) |

#### Exemple : Extraction Directe du JSON depuis l'API Interceptée

```python
# Traiter directement la réponse JSON sans parser le HTML
donnees_produits = page.xhr_json(r"/api/products\?category=electronics")
if donnees_produits:
    for item in donnees_produits.get("items", []):
        print(item["name"], item["price"])

# Inspecter les requêtes POST et les paramètres envoyés
requetes_post = page.filter_xhr(method="POST", status=200)
for req in requetes_post:
    print(f"URL POST : {req.url}")
    print(f"Corps envoyé (Payload) : {req.post_data}")
    print(f"Réponse JSON reçue : {req.json()}")
```

#### D. Utilisation en Ligne de Commande (CLI) et Laboratoire

```powershell
# Intercepter les paquets XHR via la CLI :
scrapecore extract fetch "https://quotes.toscrape.com/js/" sortie.html --capture-xhr

# Tester l'interception dans le laboratoire interactif :
python ScrapeCore.py --xhr "https://quotes.toscrape.com/js/"
```

---

### 5. Crawling à Grande Échelle : Framework Spiders

```python
from scrapecore.spiders import Spider, Request

class LivresSpider(Spider):
    name = "livres_crawler"
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
    spider = LivresSpider()
    resultat = spider.start()
    print(f"{len(resultat.items)} livres collectés avec succès !")
```

---

### 6. Gestion des Sessions et Rotation de Proxies

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

### 7. Intelligence Artificielle et Serveur MCP

```powershell
# Démarrer le serveur MCP en mode stdio
scrapecore-mcp

# Ou en mode flux HTTP sur le réseau
scrapecore-mcp --http --port 8000
```

#### Conversion Propre en Markdown pour les Pipelines RAG
```powershell
scrapecore extract "https://news.ycombinator.com" --ai-targeted -o actualites.md
```

---

### 8. Interface en Ligne de Commande (CLI)

#### Console Interactive (`scrapecore shell`)
```powershell
scrapecore shell "https://quotes.toscrape.com"
```

#### Extraction Directe vers un Fichier (`scrapecore extract`)
```powershell
# Sauvegarder les résultats d'un sélecteur CSS dans un fichier
scrapecore extract "https://quotes.toscrape.com" -s "span.text" -o citations.txt

# Navigation furtive avec résolution de Cloudflare
scrapecore extract stealthy-fetch "https://site-protege.com" --solve-cloudflare -o page.html
```

---

## 📁 Structure du Répertoire

```
ScrapeCore/
│
├── lang/                       # Documentation multilingue
│   ├── readme_en.md            # Anglais
│   ├── readme_es.md            # Espagnol
│   ├── readme_pt-br.md         # Portugais (Brésil)
│   ├── readme_zh.md            # Chinois simplifié
│   ├── readme_ja.md            # Japonais
│   ├── readme_de.md            # Allemand
│   ├── readme_fr.md            # Français
│   ├── readme_ru.md            # Russe
│   ├── readme_ko.md            # Coréen
│   └── readme_ar.md            # Arabe
│
├── scrapecore/                 # Code source de la bibliothèque
├── tests/                      # Tests unitaires et d'intégration
├── .venv/                      # Environnement virtuel Python 3.13
├── pyproject.toml              # Métadonnées et dépendances de packaging
├── requirements.txt            # Liste des dépendances d'installation
├── LICENSE                     # Licence BSD-3 (Alperen AKKAYA & Karim Shoair)
├── ScrapeCore.py               # Laboratoire de test et de diagnostic
└── README.md                   # Documentation principale (Turc)
```

---

## 🙏 Remerciements et Crédits

Ce projet s'appuie sur le remarquable travail de **Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))**, créateur de la bibliothèque **[Scrapling](https://github.com/D4Vinci/Scrapling)**.

* **Dépôt d'Origine :** [https://github.com/D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
* **Auteur d'Origine :** Karim Shoair ([@D4Vinci](https://github.com/D4Vinci))
* **Licence d'Origine :** BSD 3-Clause License

Nous adressons nos plus sincères remerciements à Karim Shoair et à la communauté open-source pour cette architecture innovante. ScrapeCore poursuit cette démarche avec un développement indépendant et continu.

---

## ⚖️ Licence

Ce projet est sous **Licence BSD 3-Clause** :

* **Copyright (c) 2026, Alperen AKKAYA**
* **Copyright (c) 2024, Karim Shoair**

Consultez le fichier [LICENSE](../LICENSE) pour plus d'informations.
