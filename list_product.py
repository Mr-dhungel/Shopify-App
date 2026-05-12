import requests

SHOP = "test-store-3volkicy.myshopify.com"
TOKEN = "shpua_a76731113c6c51eca1ecfb61ea0541e2"

url = f"https://{SHOP}/admin/api/2026-04/products.json"

headers = {
    "X-Shopify-Access-Token": TOKEN
}

response = requests.get(url, headers=headers)

print(response.json())