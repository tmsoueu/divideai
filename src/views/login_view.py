"""Login view module.

Este módulo contém a implementação da tela de login do aplicativo DivideAI.
"""
import flet as ft


class LoginView(ft.View):
    """
    Componente de visualização para autenticação de usuários.

    Esta classe representa a tela de login do aplicativo, fornecendo
    interface para autenticação de usuários.

    Attributes:
        Nenhum atributo público.
    """

    def __init__(self, route: str):
        """
        Inicializa uma nova instância da tela de login.

        Args:
            route: Rota associada à view.
        """
        super().__init__(route=route)
        self.container = ft.Container(
            width=400,
            height=600,
            border_radius=35,
            bgcolor=ft.colors.WHITE,
            padding=20,
            alignment=ft.alignment.center
        )
        self.controls = [
            ft.Container(
                content=self.container,
                alignment=ft.alignment.center,
                expand=True
            )
        ]