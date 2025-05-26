"""
Módulo responsável pela conexão e operações básicas do banco de dados SQLite.
"""

import sqlite3
from pathlib import Path
from datetime import datetime, UTC

DB_DIR = Path(__file__).parent.parent / 'storage' / 'data'
DB_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / 'divideai.db'


def get_connection():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.

    Returns:
        sqlite3.Connection: Conexão com o banco de dados.
    """
    return sqlite3.connect(DB_PATH)


def initialize_database():
    """
    Cria a tabela de usuários caso ela não exista.
    """
    try:
        print(f'Inicializando banco em: {DB_PATH}')
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    google_id TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    photo_url TEXT,
                    created_at TEXT NOT NULL
                )
                '''
            )
            conn.commit()
        print('Tabela users criada/verificada com sucesso.')
    except Exception as e:
        print(f'Erro ao inicializar banco: {e}')


def insert_user(google_id: str, name: str, email: str, photo_url: str = None) -> int:
    """
    Insere um novo usuário na tabela users.

    Args:
        google_id (str): ID do usuário no Google.
        name (str): Nome do usuário.
        email (str): E-mail do usuário.
        photo_url (str, opcional): URL da foto do usuário.

    Returns:
        int: ID do usuário inserido.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO users (google_id, name, email, photo_url, created_at)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (google_id, name, email, photo_url, datetime.now(UTC).isoformat())
        )
        conn.commit()
        return cursor.lastrowid


def get_user_by_google_id(google_id: str) -> dict | None:
    """
    Busca um usuário pelo google_id.

    Args:
        google_id (str): ID do usuário no Google.

    Returns:
        dict | None: Dicionário com os dados do usuário ou None se não encontrado.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT id, google_id, name, email, photo_url, created_at
            FROM users
            WHERE google_id = ?
            ''',
            (google_id,)
        )
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'google_id': row[1],
                'name': row[2],
                'email': row[3],
                'photo_url': row[4],
                'created_at': row[5],
            }
        return None