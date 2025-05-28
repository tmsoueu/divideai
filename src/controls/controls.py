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
        self.on_logout_click_callback = on_logout_click  # Salva o callback externo, se houver

        self.bgcolor = AZUL_ESCURO
        self.shape = ft.NotchShape.CIRCULAR
        self.content = ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.HOME, icon_color=BRANCO),
                ft.IconButton(icon=ft.Icons.LIST, icon_color=BRANCO),
                ft.Container(expand=True),

                # Substituindo o último botão por imagem clicável
                ft.GestureDetector(
                    on_tap=self.on_logout_click,
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

    def on_logout_click(self, e=None):
        """
        Função chamada ao clicar no avatar do usuário.
        Exibe um dialog de confirmação antes de fazer logout.
        """
        print('[DEBUG] Avatar clicado! Exibindo diálogo de confirmação.')
        def do_logout(e=None):
            print('[DEBUG] Logout confirmado.')
            delete_all_users()
            self.page.go('/login_view')

        def cancel(ev=None):
            print('[DEBUG] Logout cancelado.')

        dialog = MyAlertDialog(
            page=self.page,
            title='Confirmar logout',
            message='Deseja realmente sair da sua conta?',
            on_ok=do_logout,
            on_cancel=cancel
        )
        dialog.show()
        

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
        self.bgcolor = AZUL_MEDIO
        self.shape = ft.CircleBorder()
        self.content = ft.Icon(
            name=ft.Icons.ADD,
            size=30,
            color=BRANCO
        )
        self.on_click = on_click

class MyAlertDialog(ft.AlertDialog):
    """
    Diálogo de confirmação reutilizável com título, mensagem e botões OK/Cancelar.
    """

    def __init__(self, page: ft.Page, title: str, message: str, on_ok, on_cancel=None):
        super().__init__()
        self.page = page
        self.title = ft.Text(title, weight=ft.FontWeight.BOLD, color=BRANCO)
        self.title_padding = ft.padding.only(left=50, top=30, right=50)
        self.content_padding = ft.padding.only(left=50, top=20, right=50, bottom=20)
        self.content = ft.Text(message, color=BRANCO)
        self.actions_alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.bgcolor = AZUL_ESCURO
        self.barrier_color = ft.Colors.with_opacity(0.9, AMARELO)

        def handle_cancel(e):
            if on_cancel:
                on_cancel(e)
            self.open = False
            self.page.update()

        def handle_ok(e):
            if on_ok:
                on_ok(e)
            self.open = False
            self.page.update()

        self.actions = [
            ft.TextButton(
                'Cancelar',
                on_click=handle_cancel,
                style=ft.ButtonStyle(
                    color=BRANCO
                )
            ),
            ft.TextButton(
                'OK',
                on_click=handle_ok,
                style=ft.ButtonStyle(
                    color=BRANCO
                )
            )
        ]

    def show(self):
        """Exibe o diálogo."""
        self.page.open(self)
        self.page.update()