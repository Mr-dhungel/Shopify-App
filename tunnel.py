from pyngrok import ngrok

ngrok.set_auth_token("3DcoRUcpTtFxL7xMO35kMn6N5rM_4T5sANwTTs3LPDc84fYXU")

public_url = ngrok.connect(8000)

print("🔥 Public URL:", public_url)

# keep script alive
input("Press ENTER to stop tunnel...\n")