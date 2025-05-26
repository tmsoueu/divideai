import os
import pytest
from connections.database import (
    get_connection,
    initialize_database,
    insert_user,
    get_user_by_google_id,
    DB_PATH,
)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Remove o banco antes de cada teste para garantir ambiente limpo
    if DB_PATH.exists():
        os.remove(DB_PATH)
    initialize_database()
    yield
    # Aguarda o garbage collector fechar conexões
    import gc, time
    gc.collect()
    time.sleep(0.1)
    if DB_PATH.exists():
        try:
            os.remove(DB_PATH)
        except PermissionError:
            pass  # Em último caso, ignore o erro no teardown

def test_insert_and_get_user():
    google_id = 'test_google_id'
    name = 'Test User'
    email = 'test@example.com'
    photo_url = 'http://example.com/photo.png'

    user_id = insert_user(google_id, name, email, photo_url)
    assert user_id > 0

    user = get_user_by_google_id(google_id)
    assert user is not None
    assert user['google_id'] == google_id
    assert user['name'] == name
    assert user['email'] == email
    assert user['photo_url'] == photo_url
    assert 'created_at' in user

def test_get_user_not_found():
    user = get_user_by_google_id('nonexistent_id')
    assert user is None