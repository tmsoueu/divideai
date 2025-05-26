"""Módulo da tela de login do DivideAI."""

import flet as ft


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
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=['#010a18', '#01132e'],
                ),
            )
        ]