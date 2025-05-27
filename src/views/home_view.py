from components.resources import *
from controls.controls import ft, MyBottomAppBar, MyFloatingActionButton
import time
import threading

class HomeView(ft.View):
    """
    View da tela inicial do DivideAI.
    """
    def __init__(self, page: ft.Page, user_infos: str = None):
        super().__init__()
        self.page = page
        self.route = "/home"
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.bgcolor = AZUL_CLARO
        
        print(user_infos)
        # Instancia o menu inferior e o botão flutuante
        self.bottom_appbar = MyBottomAppBar(page=self.page, user_photo=user_infos.get('photo_url'))
        self.floating_action_button = MyFloatingActionButton(page=self.page)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

        self.arrow_icon = None
        
        self.controls = [
            ft.Container(
                expand=True,
                margin=ft.margin.all(40),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src=LOGO_HORIZONTAL,
                            # width=200,
                            height=300,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Text(
                            
                            f'{user_infos.get('name').split()[0]}, você sabe! 🍻\nBoteco não é bagunça,\ne sua conta também não!',
                            width=self.page.width * 0.8,
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color=BRANCO
                        ),
                        ft.Text(
                            f'Chega de confusão na hora de dividir a conta do bar.',
                            size=14,
                            width=self.page.width * 0.5,
                            text_align=ft.TextAlign.CENTER,
                            color=BRANCO
                        ),
                        ft.Text(
                            'Clica no botão aí embaixo e deixa que a gente resolve',
                            size=14,
                            width=self.page.width * 0.5,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color=AMARELO
                        ),
                        arrow_icon := ft.Container(
                            content=ft.Icon(name=ft.Icons.ARROW_DOWNWARD, size=40, color=BRANCO),
                        )
                    ]
                )
            )
        ]
        self.arrow_icon = arrow_icon
        