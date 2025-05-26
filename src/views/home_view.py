import flet as ft
from components.resources import AZUL_ESCURO, AZUL_CLARO
from pathlib import Path

SESSION_FILE = Path(__file__).parent.parent / 'storage' / 'data' / 'session.txt'

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
            if SESSION_FILE.exists():
                SESSION_FILE.unlink()
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
                        ft.Text(
                            'Olá mundo',
                            color=ft.Colors.WHITE,
                            size=32,
                            weight=ft.FontWeight.BOLD,
                        ),
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