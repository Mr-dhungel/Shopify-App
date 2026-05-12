import requests
from config.settings import SHOPIFY_SHOP, SHOPIFY_ACCESS_TOKEN, SHOPIFY_API_VERSION


class ShopifyAPI:
    """Shopify REST API client"""

    def __init__(self, shop: str = None, access_token: str = None):
        self.shop = shop or SHOPIFY_SHOP
        self.access_token = access_token or SHOPIFY_ACCESS_TOKEN
        self.api_version = SHOPIFY_API_VERSION
        self.base_url = f"https://{self.shop}/admin/api/{self.api_version}"

    def _get_headers(self):
        """Get authorization headers"""
        return {"X-Shopify-Access-Token": self.access_token}

    def get_products(self, limit=50):
        """Get all products from Shopify store"""
        url = f"{self.base_url}/products.json"
        params = {"limit": limit}
        headers = self._get_headers()

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        return response.json()

    def get_product(self, product_id: int):
        """Get a specific product by ID"""
        url = f"{self.base_url}/products/{product_id}.json"
        headers = self._get_headers()

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    def create_product(self, product_data: dict):
        """Create a new product"""
        url = f"{self.base_url}/products.json"
        headers = self._get_headers()
        payload = {"product": product_data}

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()
