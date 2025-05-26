"""Módulo principal da aplicação DivideAI."""
from connections.database import initialize_database
from controls.controls import ft
from views.login_view import LoginView
from views.home_view import HomeView


def main(page: ft.Page):
    """
    Inicializa a página principal da aplicação.

    Args:
        page (ft.Page): Página principal do Flet.
    """
    initialize_database()
    
    page.title = 'DivideAI'
    page.padding = 0
    
    page.route = '/'
    login = LoginView(page=page)
    
    def route_change(route):
        """
        Gerencia a mudança de rotas da aplicação.

        Args:
            route: Rota acessada.
        """
        page.views.clear()
        
        if page.route == '/':
            page.views.append(login)
            
        elif page.route == '/home':
            page.views.append(HomeView(page=page))
            
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    """
    Ponto de entrada da aplicação.

    Inicia a aplicação Flet.
    """
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='src/assets')
