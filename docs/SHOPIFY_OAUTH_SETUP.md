# Shopify OAuth Setup

This guide walks through the process of setting up Shopify OAuth authentication for your app.

## Step 1: Create a Custom App in Shopify Partner Dashboard

1. Go to [Shopify Partner Dashboard](https://partners.shopify.com/)
2. Select your development store
3. Go to **Settings** → **Apps and integrations** → **Develop apps**
4. Click **Create an app**
5. Choose **Custom app**
6. Enter your app name (e.g., "Product Automation")

## Step 2: Configure App Settings

### API Credentials Tab

1. Navigate to the **API Credentials** tab
2. Under **Admin API access scopes**, enable:
   - `write_products`
   - `read_products`
3. Click **Save**
4. In the **API Credentials** section, you'll see:
   - **Client ID** → Copy to `SHOPIFY_API_KEY`
   - **Client secret** → Copy to `SHOPIFY_API_SECRET`

### Configuration

1. Set **App URL**: `http://localhost:8000` (or your ngrok URL)
2. Set **Allowed redirect URL**: `http://localhost:8000/auth/callback`

### Webhooks

Set API version to `2026-04` (or latest stable)

## Step 3: Get Access Token

### Method 1: Using OAuth Flow (Recommended)

1. Start the FastAPI server:
   ```bash
   python -m src.shopify.oauth
   ```

2. Navigate to:
   ```
   http://localhost:8000/install?shop=your-store.myshopify.com
   ```

3. Follow the OAuth flow
4. After authorization, you'll receive an `access_token`

### Method 2: Manual Access Token

1. In Partner Dashboard, go to **Admin API access tokens**
2. Click **Generate token**
3. Copy the token to `SHOPIFY_ACCESS_TOKEN`

## Step 4: Update .env

```env
SHOPIFY_API_KEY=<your_client_id>
SHOPIFY_API_SECRET=<your_client_secret>
SHOPIFY_SCOPES=write_products,read_products
SHOPIFY_REDIRECT_URI=http://localhost:8000/auth/callback
SHOPIFY_SHOP=<your-store>.myshopify.com
SHOPIFY_ACCESS_TOKEN=<your_access_token>
```

## Step 5: Test Connection

```bash
python -c "
from src.shopify.api import ShopifyAPI
api = ShopifyAPI()
products = api.get_products()
print(f'Connected! Found {len(products[\"products\"])} products')
"
```

## Using ngrok for Development

If you want to use ngrok for public URLs:

1. Get ngrok auth token from https://dashboard.ngrok.com/
2. Add to `.env`: `NGROK_AUTH_TOKEN=<your_token>`
3. Run tunnel:
   ```bash
   python scripts/run_tunnel.py
   ```
4. Update redirect URL in Shopify Partner Dashboard with ngrok URL

## Scopes Reference

Common scopes:
- `write_products` - Create/modify products
- `read_products` - Read product data
- `write_orders` - Create orders
- `read_orders` - Read order data
- `write_customers` - Manage customers
- `read_customers` - Read customer data

For full list, see [Shopify Scopes Documentation](https://shopify.dev/api/admin-rest/2026-04/resources/oauth#scopes)

## Troubleshooting

### "Invalid API Key"
- Verify Client ID is correct
- Check it's for a Custom app (not a public app)

### "Redirect URI mismatch"
- Ensure redirect URI in Partner Dashboard matches exactly
- Include `http://` or `https://` scheme

### Access Token Expired
- Generate a new token in Partner Dashboard
- OAuth tokens don't expire automatically, but can be revoked

## Security Notes

⚠️ **Important Security Practices:**

1. **Never commit `.env` file** - Already in `.gitignore`
2. **Use environment variables** - Don't hardcode credentials
3. **Rotate tokens regularly** - Especially if exposed
4. **Use HTTPS in production** - Never use HTTP
5. **Keep secrets out of logs** - Check your logging configuration
