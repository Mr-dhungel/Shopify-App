from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
from config.settings import (
    SHOPIFY_API_KEY,
    SHOPIFY_API_SECRET,
    SHOPIFY_SCOPES,
    SHOPIFY_REDIRECT_URI,
)

app = FastAPI(title="Shopify App")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    """Render the OAuth install page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/install")
def install(shop: str):
    """Initiate OAuth flow - redirect to Shopify authorization"""
    install_url = (
        f"https://{shop}/admin/oauth/authorize"
        f"?client_id={SHOPIFY_API_KEY}"
        f"&scope={SHOPIFY_SCOPES}"
        f"&redirect_uri={SHOPIFY_REDIRECT_URI}"
        f"&state=random_string"
    )
    return {"install_url": install_url}


@app.get("/auth/callback")
def callback(request: Request):
    """OAuth callback - exchange code for access token"""
    params = request.query_params

    code = params.get("code")
    shop = params.get("shop")

    token_url = f"https://{shop}/admin/oauth/access_token"

    payload = {
        "client_id": SHOPIFY_API_KEY,
        "client_secret": SHOPIFY_API_SECRET,
        "code": code,
    }

    response = requests.post(token_url, data=payload)
    data = response.json()

    access_token = data.get("access_token")

    # Return success page with credentials
    return templates.TemplateResponse(
        "success.html",
        {
            "request": request,
            "shop": shop,
            "access_token": access_token,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
