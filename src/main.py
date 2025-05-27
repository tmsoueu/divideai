"""Módulo principal da aplicação DivideAI."""
from connections.database import initialize_database, get_any_user, delete_all_users
from views.login_view import LoginView
from views.home_view import HomeView
from controls.controls import ft


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

        user = get_any_user()
        if user:
            home_view = HomeView(page=page, user_infos=user)
            page.views.append(home_view)
        
        else:
            login_view = LoginView(page=page)
            page.views.append(login_view)

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='src/assets')
