"""
Módulo responsável pelo fluxo de autenticação com o Google OAuth2.

Este módulo realiza o login OAuth2, troca o código por token e obtém as informações do usuário.
"""

import os
from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
env_path = Path(__file__).parent.parent / 'storage' / 'data' / '.env'
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URI_LOCAL = os.getenv('GOOGLE_REDIRECT_URI_LOCAL')
REDIRECT_URI_PROD = os.getenv('GOOGLE_REDIRECT_URI_PROD')
SCOPES = 'openid email profile'


def is_running_local():
    """
    Detecta se o app está rodando localmente (desktop/web) ou em produção/mobile.
    Retorna True se local, False se produção/mobile.
    """
    # Flet define a variável de ambiente FLET_RUNTIME no ambiente mobile/cloud
    return os.getenv('FLET_RUNTIME') is None


def get_redirect_uri():
    """
    Retorna o redirect URI apropriado para o ambiente.
    """
    return REDIRECT_URI_LOCAL if is_running_local() else REDIRECT_URI_PROD


def get_auth_code():
    """
    Inicia o fluxo OAuth2, abre o navegador e captura o código de autorização.

    Returns:
        str: Código de autorização recebido do Google.
    """
    redirect_uri = get_redirect_uri()
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': SCOPES,
        'access_type': 'offline',
        'prompt': 'consent'
    }
    auth_url = f'https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}'
    webbrowser.open(auth_url)

    if is_running_local():
        class OAuthHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                query = parse_qs(urlparse(self.path).query)
                self.server.auth_code = query.get('code', [None])[0]
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Login realizado. Pode fechar esta aba.')

        parsed = urlparse(redirect_uri)
        server = HTTPServer((parsed.hostname, parsed.port), OAuthHandler)
        server.handle_request()
        return server.auth_code
    else:
        # No Flet Cloud/mobile, o código de autorização será retornado via callback do Flet
        # O fluxo pode ser adaptado conforme a documentação do Flet para OAuth2
        raise NotImplementedError('Fluxo OAuth2 para produção/mobile deve ser implementado conforme o Flet Cloud.')


def exchange_code_for_token(auth_code):
    """
    Troca o código de autorização por um token de acesso.

    Args:
        auth_code (str): Código de autorização recebido do Google.

    Returns:
        dict: Resposta do token contendo access_token, refresh_token, etc.
    """
    token_response = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'code': auth_code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': get_redirect_uri(),
            'grant_type': 'authorization_code'
        }
    )
    token_response.raise_for_status()
    return token_response.json()


def get_user_info(access_token):
    """
    Obtém informações do usuário autenticado usando o access_token.

    Args:
        access_token (str): Token de acesso válido.

    Returns:
        dict: Informações do usuário (email, nome, foto, etc).
    """
    resp = requests.get(
        'https://www.googleapis.com/oauth2/v3/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    resp.raise_for_status()
    return resp.json()


def google_login():
    """
    Executa o fluxo completo de login OAuth2 com o Google.

    Returns:
        dict: Informações do usuário autenticado.
    """
    code = get_auth_code()
    tokens = exchange_code_for_token(code)
    user_info = get_user_info(tokens['access_token'])
    return user_info


if __name__ == '__main__':
    user = google_login()
    print('Usuário autenticado:', user)
