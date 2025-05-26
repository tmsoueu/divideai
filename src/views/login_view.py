import flet as ft
from components.resources import *
from connections.google_auth import google_login
from connections.database import insert_user, get_user_by_google_id
from pathlib import Path

SESSION_FILE = Path(__file__).parent.parent / 'storage' / 'data' / 'session.txt'


class LoginView(ft.View):
    """
    Login screen view for DivideAI.
    """

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = '/'
        self.padding = ft.padding.all(0)

        # Verifica se já existe sessão salva e usuário no banco
        google_id = self.get_logged_user_id()
        if google_id and get_user_by_google_id(google_id):
            self.page.go('/home')

        def on_google_login_click(e):
            user_info = google_login()
            insert_user(
                google_id=user_info['sub'],
                name=user_info.get('name', ''),
                email=user_info.get('email', ''),
                photo_url=user_info.get('picture', None)
            )
            self.set_logged_user_id(user_info['sub'])
            self.page.go('/home')

        self.controls = [
            ft.Container(
                expand=True,
                width=page.width,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[AZUL_ESCURO, AZUL_CLARO],
                ),
                content=ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            expand=True,
                            content=ft.Image(
                                src=LOGO,
                                width=page.width * 0.8,
                            ),
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                width=page.width * 0.6,
                                bgcolor=BRANCO,
                                color=AZUL_ESCURO,
                                style=ft.ButtonStyle(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text('Entrar com o Google', weight=ft.FontWeight.BOLD),
                                    ],
                                ),
                                on_click=on_google_login_click
                            ),
                        ),
                        ft.Container(
                            padding=ft.padding.only(bottom=20),
                            content=ft.Text(
                                '© 2026 DivideAI. Made with ❤ by TM.',
                                size=10,
                                color=AMARELO,
                            )
                        )
                    ]
                )
            )
        ]

    def get_logged_user_id(self):
        if SESSION_FILE.exists():
            google_id = SESSION_FILE.read_text().strip()
            print(f'[DEBUG] Lendo google_id do arquivo de sessão: {google_id}')
            return google_id
        print('[DEBUG] Arquivo de sessão não existe.')
        return None

    def set_logged_user_id(self, google_id):
        print(f'[DEBUG] Salvando google_id na sessão: {google_id}')
        SESSION_FILE.write_text(google_id)
