from components.resources import *
from controls.controls import ft, MyBottomAppBar, MyFloatingActionButton


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

        self.controls = [
            ft.Container(
                expand=True,
                margin=ft.margin.all(50),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src=LOGO_HORIZONTAL,
                            # width=200,
                            # height=200,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Text(
                            f'Bem-vindo {user_infos.get('name').split()[0]}!',
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.WHITE
                        ),
                        ft.Icon(
                            name=ft.Icons.ARROW_DOWNWARD,
                            size=40,
                            color=ft.Colors.WHITE
                        )
                    ]
                )
            )
        ]

