"""Módulo da tela de login do DivideAI."""

import flet as ft
from components.resources import *

class LoginView(ft.View):
    """
    Componente de visualização para autenticação de usuários.

    Esta classe representa a tela de login do aplicativo, fornecendo
    interface para autenticação de usuários.

    Attributes:
        Nenhum atributo público.
    """

    def __init__(self, page: ft.Page):
        """
        Inicializa uma nova instância da tela de login.

        Args:
            route: Rota associada à view.
        """
        super().__init__()
        self.page = page
        self.route = '/'
        self.padding = ft.padding.all(0)
        
        self.controls = [
            ft.Container(
                width=self.page.width,
                height=self.page.height,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[AZUL_ESCURO, AZUL_CLARO],
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    #spacing=40,
                    controls=[
                        ft.Image(
                            src=LOGO,
                            width=270,
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                width=page.width * 0.5,
                                bgcolor='#f6f6f6',
                                color='#010a18',
                                style=ft.ButtonStyle(
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                ),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(
                                            src='https://img.icons8.com/color/48/google-logo.png',
                                            width=20,
                                            height=20,
                                        ),
                                        ft.Text('Entrar com o Google', weight=ft.FontWeight.BOLD),
                                    ],
                                ),
                                on_click=lambda e: print('Login com Google clicado')
                            ),
                        ),
                        # Rodapé com direitos autorais
                        ft.Container(
                            #padding=ft.padding.only(bottom=20),
                            content=ft.Text(
                                "© 2026 DivideAI. Made with ❤ by TM.",
                                size=10,
                                color=BRANCO,
                            )
                        )
                    ]
                )
            )
        ]