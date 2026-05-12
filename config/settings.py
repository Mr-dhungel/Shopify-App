import os
from dotenv import load_dotenv

load_dotenv()

# Shopify OAuth Configuration
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET")
SHOPIFY_SCOPES = os.getenv("SHOPIFY_SCOPES")
SHOPIFY_REDIRECT_URI = os.getenv("SHOPIFY_REDIRECT_URI")

# Shopify API Configuration
SHOPIFY_SHOP = os.getenv("SHOPIFY_SHOP")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_API_VERSION = "2026-04"

# Browser Configuration
BRAVE_PATH = os.getenv("BRAVE_PATH", r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
BRAVE_USER_DATA_DIR = os.getenv("BRAVE_USER_DATA_DIR", r"C:\Users\Mukunda\AppData\Local\BraveSoftware\Brave-Browser\User Data")

# NYWD Scraper Configuration
NYWD_DEFAULT_SKUS = ["583295", "583296", "999999"]

# ngrok Configuration
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")
NGROK_TUNNEL_PORT = 8000

# FastAPI Configuration
FASTAPI_HOST = "0.0.0.0"
FASTAPI_PORT = 8000
