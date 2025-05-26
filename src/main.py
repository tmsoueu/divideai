"""Módulo principal da aplicação DivideAI."""
from controls.controls import ft
from controls.toggle import Toggle
from views.login_view import LoginView


def main(page: ft.Page):
    """
    Inicializa a página principal da aplicação.

    Args:
        page (ft.Page): Página principal do Flet.
    """
    page.title = 'DivideAI'
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    
    page.route = '/'
    login = LoginView(page=page)
    toggle = Toggle(page=page)
    
    page.overlay.append(toggle)
    
    
    def route_change(route):
        """
        Gerencia a mudança de rotas da aplicação.

        Args:
            route: Rota acessada.
        """
        page.views.clear()
        
        if page.route == '/':
            page.views.append(login)
            
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    """
    Ponto de entrada da aplicação.

    Inicia a aplicação Flet.
    """
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
