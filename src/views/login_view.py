import flet as ft
from components.resources import *
from connections.google_auth import google_login  # ou google_login, conforme seu método

class LoginView(ft.View):
    """
    Login screen view for DivideAI.
    """

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = '/'
        self.padding = ft.padding.all(0)

        def on_google_login_click(e):
            user_info = google_login()
            print('Usuário autenticado:', user_info)
            # No próximo passo, vamos salvar no banco e redirecionar

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
                                on_click=on_google_login_click  # <-- callback atualizado
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
