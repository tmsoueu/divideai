import os
from dotenv import load_dotenv
from pathlib import Path
import webbrowser
import requests
from urllib.parse import urlencode, urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

# Carrega variáveis do .env
env_path = Path(__file__).parent.parent / 'storage' / 'data' / '.env'
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
SCOPES = "openid email profile"

def get_auth_code():
    # Gera a URL de autorização
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPES,
        "access_type": "offline",
        "prompt": "consent"
    }
    auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
    webbrowser.open(auth_url)

    # Inicia servidor local para capturar o código
    class OAuthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            self.server.auth_code = query.get("code", [None])[0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Login realizado. Pode fechar esta aba.")

    parsed = urlparse(REDIRECT_URI)
    server = HTTPServer((parsed.hostname, parsed.port), OAuthHandler)
    server.handle_request()
    return server.auth_code

def exchange_code_for_token(auth_code):
    token_response = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "code": auth_code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code"
        }
    )
    token_response.raise_for_status()
    return token_response.json()

def get_user_info(access_token):
    resp = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    resp.raise_for_status()
    return resp.json()

def google_login_manual():
    code = get_auth_code()
    tokens = exchange_code_for_token(code)
    user_info = get_user_info(tokens["access_token"])
    return user_info

if __name__ == "__main__":
    user = google_login_manual()
    print("Usuário autenticado:", user)
