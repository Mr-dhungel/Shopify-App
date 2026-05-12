# Shopify OAuth Token Generator (FastAPI + HTML + Dev Dashboard Setup)

## 1. Shopify App Creation (Dev Dashboard)

Go to:

https://dev.shopify.com/apps

### Steps:

1.  Click **Create app**
2.  Choose **Custom app**
3.  Enter app name (e.g. `product-automation`)
4.  Select your development store or organization
5.  App will be created instantly

------------------------------------------------------------------------

## 2. Configure App Settings

### App URL

    https://your-ngrok-url.ngrok-free.dev

------------------------------------------------------------------------

### Redirect URL (IMPORTANT)

    https://your-ngrok-url.ngrok-free.dev/auth/callback

------------------------------------------------------------------------

### Admin API Scopes

Enable: - write_products - read_products

------------------------------------------------------------------------

### Webhooks API version

Use latest stable:

    2026-04

------------------------------------------------------------------------

### Distribution

-   Use: Custom distribution
-   Do NOT publish to App Store

------------------------------------------------------------------------

### Legacy install flow

-   OFF (do NOT enable)

------------------------------------------------------------------------

## 3. Install Dependencies

pip install fastapi uvicorn requests python-dotenv jinja2

------------------------------------------------------------------------

## 4. Project Structure

shopify-oauth-app/ │ ├── main.py ├── .env ├── templates/ │ ├──
index.html │ └── success.html

------------------------------------------------------------------------

## 5. .env

SHOPIFY_API_KEY=your_client_id\
SHOPIFY_API_SECRET=your_client_secret\
SHOPIFY_SCOPES=write_products,read_products\
SHOPIFY_REDIRECT_URI=https://your-ngrok-url.ngrok-free.dev/auth/callback

------------------------------------------------------------------------

## 6. main.py

``` python
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = os.getenv("SHOPIFY_API_KEY")
API_SECRET = os.getenv("SHOPIFY_API_SECRET")
SCOPES = os.getenv("SHOPIFY_SCOPES")
REDIRECT_URI = os.getenv("SHOPIFY_REDIRECT_URI")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/install")
def install(shop: str = Form(...)):
    install_url = (
        f"https://{shop}/admin/oauth/authorize"
        f"?client_id={API_KEY}"
        f"&scope={SCOPES}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&state=random_string"
    )
    return {"install_url": install_url}

@app.get("/auth/callback", response_class=HTMLResponse)
def callback(request: Request):
    params = request.query_params
    code = params.get("code")
    shop = params.get("shop")

    token_url = f"https://{shop}/admin/oauth/access_token"

    payload = {
        "client_id": API_KEY,
        "client_secret": API_SECRET,
        "code": code
    }

    response = requests.post(token_url, data=payload)
    data = response.json()

    access_token = data.get("access_token")

    return templates.TemplateResponse(
        "success.html",
        {
            "request": request,
            "shop": shop,
            "token": access_token
        }
    )
```

------------------------------------------------------------------------

## 7. templates/index.html

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Shopify Installer</title>
</head>
<body>
    <h2>Install Shopify App</h2>
    <form action="/install" method="post">
        <input type="text" name="shop" placeholder="your-store.myshopify.com" required />
        <button type="submit">Generate Install Link</button>
    </form>
</body>
</html>
```

------------------------------------------------------------------------

## 8. templates/success.html

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h2>App Installed Successfully</h2>
    <p><b>Shop:</b> {{ shop }}</p>
    <p><b>Access Token:</b></p>
    <textarea rows="6" cols="80">{{ token }}</textarea>
</body>
</html>
```

------------------------------------------------------------------------

## 9. Run Project

uvicorn main:app --reload --port 8000\
ngrok http 8000

------------------------------------------------------------------------

## 10. Flow

1.  Create app in dev.shopify.com
2.  Configure URLs + scopes
3.  Run FastAPI
4.  Start ngrok
5.  Enter shop name
6.  Install app
7.  Get access token

------------------------------------------------------------------------

## Output

You get: - Shopify app installed - OAuth completed - Access token
generated - Ready for product API automation
