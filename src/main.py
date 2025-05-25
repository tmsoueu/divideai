"""Main module for the DivideAI application."""
import flet as ft
from views.login_view import LoginView


def main(page: ft.Page):
    """Initialize the main application page."""
    page.title = "DivideAI"
    page.bgcolor = ft.Colors.BLUE_GREY_900  # Corrigido: colors -> Colors
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = False

    # Configuração das rotas
    def route_change(route):
        page.views.clear()
        page.views.append(LoginView("/login"))
        
    page.on_route_change = route_change
    page.go("/login")


ft.app(target=main)
