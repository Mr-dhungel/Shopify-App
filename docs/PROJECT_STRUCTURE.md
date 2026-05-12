# Project Structure

## Directory Layout

```
shopify-app/
├── src/                          # Source code
│   ├── __init__.py
│   ├── shopify/                  # Shopify OAuth & API
│   │   ├── __init__.py
│   │   ├── oauth.py             # FastAPI OAuth endpoints
│   │   └── api.py               # Shopify REST API client
│   ├── scrapers/                # Web scraping
│   │   ├── __init__.py
│   │   └── nywd_scraper.py      # NYWD product scraper
│   ├── browser/                 # Browser automation
│   │   ├── __init__.py
│   │   └── launcher.py          # Brave browser CDP launcher
│   └── utils/                   # Utilities
│       ├── __init__.py
│       └── tunnel.py            # ngrok tunnel setup
├── config/                       # Configuration
│   ├── __init__.py
│   └── settings.py              # Environment & app config
├── scripts/                      # Executable scripts
│   ├── run_scraper.py           # Scraper runner
│   └── run_tunnel.py            # ngrok tunnel runner
├── docs/                         # Documentation
│   ├── INDEX.md                 # Documentation index
│   ├── SETUP.md                 # Installation guide
│   ├── SHOPIFY_OAUTH_SETUP.md  # OAuth configuration
│   ├── SHOPIFY_API.md           # API module docs
│   ├── NYWD_SCRAPER.md          # Scraper docs
│   └── PROJECT_STRUCTURE.md     # This file
├── .env.example                 # Environment template
├── .env                         # Environment (gitignored)
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── README.md                    # Project overview
└── .git/                        # Git repository
```

## Module Descriptions

### `src/shopify/`

**OAuth & Shopify API Integration**

- `oauth.py`: FastAPI server with OAuth endpoints
  - `/install` - Initiate OAuth flow
  - `/auth/callback` - OAuth callback handler

- `api.py`: REST API client for Shopify Admin API
  - `ShopifyAPI` class with methods for products, orders, etc.

### `src/scrapers/`

**Web Scraping Modules**

- `nywd_scraper.py`: Playwright-based scraper for NYWD products
  - Search, extract, and pipeline methods
  - Configurable selectors for easy adaptation

### `src/browser/`

**Browser Automation**

- `launcher.py`: Brave browser launcher with Chrome DevTools Protocol
  - `BrowserLauncher` class for CDP connections
  - Configured for remote debugging

### `src/utils/`

**Utility Functions**

- `tunnel.py`: ngrok tunnel setup and management
  - Public URL generation for development
  - Tunnel lifecycle management

### `config/`

**Application Configuration**

- `settings.py`: Centralized configuration
  - Loads environment variables
  - Defines application constants
  - Easy to extend with new settings

### `scripts/`

**Executable Entry Points**

- `run_scraper.py`: Main scraper execution script
- `run_tunnel.py`: ngrok tunnel setup script

### `docs/`

**Documentation**

- Setup guides
- API documentation
- Module references
- Troubleshooting

## Configuration Flow

```
.env
  ↓
config/settings.py (loads .env)
  ↓
src/shopify/oauth.py
src/shopify/api.py
src/scrapers/nywd_scraper.py
src/browser/launcher.py
src/utils/tunnel.py
```

## Dependencies

All Python dependencies are in `requirements.txt`:

```
fastapi==0.136.1          # Web framework
uvicorn==0.46.0           # ASGI server
playwright==1.59.0        # Browser automation
requests==2.34.0          # HTTP client
python-dotenv==1.2.2      # Environment variables
pyngrok==8.1.2            # ngrok tunneling
pydantic==2.13.4          # Data validation
click==8.3.3              # CLI utilities
```

## Design Patterns

### 1. Separation of Concerns

- Business logic separated from configuration
- Each module has a single responsibility
- Clear import paths

### 2. Configuration Management

- Environment-based configuration
- No hardcoded secrets
- Easy to switch environments

### 3. Class-Based Organization

- `ShopifyAPI` - API interactions
- `NYWDScraper` - Web scraping
- `BrowserLauncher` - Browser management

### 4. Utility Functions

- `setup_ngrok_tunnel()` - Reusable tunnel setup
- `launch_brave_browser()` - Convenience function

## Adding New Modules

### To add a new scraper:

1. Create `src/scrapers/new_scraper.py`
2. Define scraper class inheriting common patterns
3. Add to `__init__.py`
4. Create `docs/NEW_SCRAPER.md`

### To add a new API client:

1. Create `src/shopify/new_api.py`
2. Implement with `ShopifyAPI` as template
3. Add configuration to `config/settings.py`

## Import Guidelines

**Correct imports:**
```python
from src.shopify.api import ShopifyAPI
from config.settings import SHOPIFY_SHOP
from src.utils.tunnel import setup_ngrok_tunnel
```

**From within package:**
```python
from ..config.settings import NGROK_AUTH_TOKEN
```

## Git Organization

- `main` branch: Production-ready code
- Feature branches: New features and fixes
- All changes should include documentation updates
