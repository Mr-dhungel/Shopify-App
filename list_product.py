import requests
from config.settings import SHOPIFY_SHOP, SHOPIFY_ACCESS_TOKEN

url = f"https://{SHOPIFY_SHOP}/admin/api/2026-04/products.json"

headers = {
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
}

response = requests.get(url, headers=headers)

print(response.json())