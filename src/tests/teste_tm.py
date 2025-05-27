
import flet as ft
from components.resources import AZUL_ESCURO, AZUL_CLARO
from connections.database import get_any_user, delete_all_users
from controls.controls import BottomMenu

class HomeView(ft.View):
    """
    Página inicial após o login.
    """

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = '/home'
        self.padding = ft.padding.all(0)

        user = get_any_user()
        user_photo = user['photo_url'] if user and 'photo_url' in user else None
        print(f'[DEBUG] user_photo: {user_photo}')
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
                        ft.Text(
                            'Bem-vindo!',
                            color=ft.Colors.WHITE,
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Container(height=60),  # Espaço para o menu não sobrepor conteúdo
                    ]
                )
            ),
            BottomMenu(
                user_photo=user_photo,
                on_logout_click=on_logout_click,
                bg_color=AZUL_ESCURO,
            ),
        ]