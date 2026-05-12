from pyngrok import ngrok
from config.settings import NGROK_AUTH_TOKEN

ngrok.set_auth_token(NGROK_AUTH_TOKEN)

public_url = ngrok.connect(8000)

print("🔥 Public URL:", public_url)

# keep script alive
input("Press ENTER to stop tunnel...\n")