# Shopify App

A comprehensive Shopify application that combines OAuth authentication, product scraping, and API management.

## Features

- 🔐 Shopify OAuth 2.0 Authentication
- 🛍️ Shopify REST API Integration
- 🕷️ NYWD Web Scraper (Playwright-based)
- 🌐 ngrok Tunnel Support
- 🎯 Professional Project Structure

## Project Structure

```
shopify-app/
├── src/
│   ├── shopify/          # Shopify OAuth & API modules
│   ├── scrapers/         # Web scraping modules
│   ├── browser/          # Browser automation modules
│   └── utils/            # Utility functions
├── config/
│   └── settings.py       # Configuration management
├── scripts/
│   ├── run_scraper.py    # Scraper runner
│   └── run_tunnel.py     # ngrok tunnel runner
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
├── .env.example          # Environment template
└── README.md
```

## Setup

### 1. Create Virtual Environment

```bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

### 4. Install Playwright Browsers

```bash
playwright install chromium
```

## Usage

### Shopify OAuth

Start the FastAPI server:

```bash
python -m src.shopify.oauth
```

Navigate to: `http://localhost:8000/install?shop=your-store.myshopify.com`

### Run NYWD Scraper

```bash
# Make sure Brave browser is running with CDP
python scripts/run_scraper.py
```

### Setup ngrok Tunnel

```bash
python scripts/run_tunnel.py
```

## Configuration

All configuration is managed in `config/settings.py`:

- Shopify API credentials
- Browser settings
- NYWD scraper defaults
- ngrok configuration

## Modules

### `src/shopify/`
- `oauth.py` - FastAPI OAuth endpoints
- `api.py` - Shopify REST API client

### `src/scrapers/`
- `nywd_scraper.py` - NYWD product scraper class

### `src/browser/`
- `launcher.py` - Brave browser launcher for CDP

### `src/utils/`
- `tunnel.py` - ngrok tunnel setup utilities

## License

Your License Here
