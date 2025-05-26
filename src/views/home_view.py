import flet as ft
from components.resources import AZUL_ESCURO, AZUL_CLARO
from connections.database import delete_all_users

class HomeView(ft.View):
    """
    Página inicial após o login.
    """

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = '/home'
        self.padding = ft.padding.all(0)

        def on_logout_click(e):
            delete_all_users()
            self.page.go('/')

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
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            text='Logout',
                            bgcolor=ft.Colors.WHITE,
                            color=AZUL_ESCURO,
                            width=page.width * 0.5,
                            on_click=on_logout_click,
                        )
                    ]
                )
            )
        ]