from connections.google_auth import google_login

def test_google_login():
    """
    Testa o fluxo manual de login com Google OAuth2.
    """
    user_info = google_login()
    print('Usuário autenticado:', user_info)

    assert isinstance(user_info, dict), 'Retorno deve ser um dicionário'
    assert 'email' in user_info, 'Resposta deve conter o e-mail'
    assert 'sub' in user_info, 'Resposta deve conter o ID do usuário (sub)'
    assert 'given_name' in user_info, 'Resposta deve conter o primeiro nome (given_name)'
    assert 'picture' in user_info, 'Resposta deve conter a URL da imagem do perfil (picture)'
    assert isinstance(user_info['given_name'], str) and user_info['given_name'], 'given_name deve ser uma string não vazia'
    assert isinstance(user_info['picture'], str) and user_info['picture'].startswith('http'), 'picture deve ser uma URL'
