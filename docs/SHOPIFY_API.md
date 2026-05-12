# Shopify API Module

The `src/shopify/api.py` module provides a Python client for the Shopify Admin REST API.

## Usage

### Import

```python
from src.shopify.api import ShopifyAPI
```

### Initialize Client

```python
# Using credentials from .env
api = ShopifyAPI()

# Or with explicit credentials
api = ShopifyAPI(
    shop="my-store.myshopify.com",
    access_token="shpua_xxxxxxxxxxxxx"
)
```

## Methods

### Get Products

```python
# Get all products
products = api.get_products()

# Get with limit
products = api.get_products(limit=10)
```

**Returns:** Dict with `products` list containing product objects

### Get Single Product

```python
product = api.get_product(product_id=123456789)
```

**Returns:** Dict with `product` containing the product object

### Create Product

```python
new_product = api.create_product({
    "title": "My Product",
    "product_type": "Category",
    "vendor": "My Vendor",
    "variants": [
        {
            "title": "Default Title",
            "price": "9.99"
        }
    ]
})
```

**Returns:** Dict with newly created `product` object

## Error Handling

```python
try:
    products = api.get_products()
except requests.exceptions.HTTPError as e:
    print(f"API Error: {e}")
```

## Configuration

Settings are loaded from `config/settings.py`:

```python
SHOPIFY_SHOP = os.getenv("SHOPIFY_SHOP")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_API_VERSION = "2026-04"
```

## API Reference

- [Shopify Admin REST API Docs](https://shopify.dev/api/admin-rest/2026-04)
- [Products Endpoint](https://shopify.dev/api/admin-rest/2026-04/resources/product)

## Rate Limits

Shopify API has rate limits:
- **Standard plans**: 2 requests/second
- **Plus/Advanced**: Variable

Implement rate limiting if making many requests:

```python
import time

def rate_limited_get_products(api, limit_per_second=2):
    delay = 1.0 / limit_per_second
    products = api.get_products()
    time.sleep(delay)
    return products
```
