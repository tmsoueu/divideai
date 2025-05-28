from connections.database import delete_all_users
from components.resources import *
import flet as ft

class MyBottomAppBar(ft.BottomAppBar):
    """
    Menu inferior customizado multiplataforma.
    """

    def __init__(self, page: ft.Page, user_photo='https://i.imgur.com/G7r1OVF.png', on_logout_click=None):
        """
        Inicializa o menu inferior.
        Args:
            user_photo (str): URL da foto do usuário.
            on_logout_click (callable): Função a ser chamada ao clicar no avatar do usuário.
        """
        super().__init__()
        self.page = page
        
        self.bgcolor = AZUL_ESCURO
        self.shape = ft.NotchShape.CIRCULAR

        self.content = ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                
                # Substituindo o último botão por imagem clicável
                ft.GestureDetector(
                    on_tap=lambda e: self.on_logout_click(),
                    content=ft.Container(
                        content=ft.Image(
                            src=user_photo,
                            width=30,
                            height=30,
                            border_radius=50,
                            fit=ft.ImageFit.COVER,
                        ),
                        border_radius=ft.border_radius.all(15),
                        clip_behavior=ft.ClipBehavior.HARD_EDGE
                    )
                )
            ]
        )
        
    def on_logout_click(self):
        """
        Função chamada ao clicar no avatar do usuário.
        Limpa o banco de dados e redireciona para a página inicial.
        """
        delete_all_users()
        self.page.go('/')

class MyFloatingActionButton(ft.FloatingActionButton):
    """
    Botão flutuante customizado.
    """

    def __init__(self, page: ft.Page, on_click=None):
        """
        Inicializa o botão flutuante.
        Args:
            on_click (callable): Função a ser chamada ao clicar no botão.
        """
        super().__init__()
        self.page = page
        self.icon = ft.Icons.ADD
        self.shape = ft.CircleBorder()
        self.on_click = on_click
        