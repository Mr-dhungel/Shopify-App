from pyngrok import ngrok
from config.settings import NGROK_AUTH_TOKEN, NGROK_TUNNEL_PORT


def setup_ngrok_tunnel(auth_token: str = None, port: int = None) -> str:
    """
    Setup ngrok tunnel for public URL access.

    Args:
        auth_token: ngrok authentication token (uses config if None)
        port: Port to tunnel (uses config if None)

    Returns:
        Public URL from ngrok
    """
    auth_token = auth_token or NGROK_AUTH_TOKEN
    port = port or NGROK_TUNNEL_PORT

    if not auth_token:
        raise ValueError("ngrok auth token not configured")

    ngrok.set_auth_token(auth_token)
    public_url = ngrok.connect(port)

    print(f"🔥 Public URL: {public_url}")

    return public_url


def keep_tunnel_alive():
    """Keep the tunnel alive until user interrupts"""
    try:
        input("Press ENTER to stop tunnel...\n")
    except KeyboardInterrupt:
        print("\n🛑 Stopping tunnel...")
    finally:
        ngrok.kill()
