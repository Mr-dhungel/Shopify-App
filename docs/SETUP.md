# Setup Guide

## Prerequisites

- Python 3.8+
- Windows (for Brave browser integration)
- Git
- Shopify Partner Account

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/Mr-dhungel/Shopify-App.git
cd Shopify-App
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

Activate it:
- **Windows (PowerShell):**
  ```bash
  .\myenv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```bash
  myenv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source myenv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install chromium
```

### 5. Configure Environment

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
SHOPIFY_API_KEY=your_api_key_here
SHOPIFY_API_SECRET=your_api_secret_here
SHOPIFY_SCOPES=write_products,read_products
SHOPIFY_REDIRECT_URI=http://localhost:8000/auth/callback
SHOPIFY_SHOP=your-store.myshopify.com
SHOPIFY_ACCESS_TOKEN=your_access_token_here
NGROK_AUTH_TOKEN=your_ngrok_token_here
```

## Getting Shopify Credentials

See [Shopify OAuth Setup](SHOPIFY_OAUTH_SETUP.md) for detailed instructions.

## Running the Application

### Option 1: OAuth Server Only

```bash
python -m src.shopify.oauth
```

Navigate to: `http://localhost:8000/install?shop=your-store.myshopify.com`

### Option 2: Run Scraper

First, ensure Brave browser is running with CDP enabled:

```bash
python scripts/run_scraper.py
```

### Option 3: Setup ngrok Tunnel

```bash
python scripts/run_tunnel.py
```

## Troubleshooting

### Import Errors

Make sure you're in the virtual environment and the project root is in your Python path.

```bash
# Add project root to PYTHONPATH
set PYTHONPATH=%PYTHONPATH%;%cd%  # Windows
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # macOS/Linux
```

### Playwright Browser Not Found

```bash
playwright install
```

### ngrok Connection Issues

- Verify ngrok auth token in `.env`
- Check ngrok account at https://dashboard.ngrok.com

## Next Steps

- Read [Shopify OAuth Setup](SHOPIFY_OAUTH_SETUP.md) for detailed OAuth configuration
- Check [Project Structure](PROJECT_STRUCTURE.md) to understand the codebase
- Review individual module documentation for specific features
