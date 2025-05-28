from components.resources import AZUL_CLARO, AZUL_ESCURO, BRANCO, AMARELO, LOGO_HORIZONTAL, BG_PATTERN_WEB
from controls.controls import ft, MyBottomAppBar, MyFloatingActionButton
import threading
import time


class HomeView(ft.View):
    """
    View da tela inicial do DivideAI.
    Exibe mensagem de boas-vindas, logo e menu inferior.
    """

    def __init__(self, page: ft.Page, user_infos: dict = None):
        """
        Inicializa a tela inicial.

        Args:
            page (ft.Page): Página principal do Flet.
            user_infos (dict): Informações do usuário logado.
        """
        super().__init__()
        self.page = page
        self.route = '/home'
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.bgcolor = AZUL_CLARO
        self.padding = ft.padding.all(0)
        
        # Instancia o menu inferior e o botão flutuante
        self.bottom_appbar = MyBottomAppBar(page=self.page, user_photo=user_infos.get('photo_url'))
        self.floating_action_button = MyFloatingActionButton(page=self.page)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

        # Estado da animação
        self.arrow_icon = ft.Container(
            animate=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
            content=ft.Icon(name=ft.Icons.ARROW_DOWNWARD, size=40, color=BRANCO),
        )

        self.arrow_stack = ft.Stack(
            width=40,
            height=100,
            controls=[self.arrow_icon]
        )

        # Layout principal
        self.controls = [
            ft.Container(
                expand=True,
                image=ft.DecorationImage(
                    src=BG_PATTERN_WEB,
                    repeat=ft.ImageRepeat.REPEAT,
                    opacity=0.3
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            height=self.page.height * 0.5,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Image(
                                    src=LOGO_HORIZONTAL,
                                    width=self.page.width * 0.9,
                                    height=self.page.height * 0.2,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Divider(
                                    height=20,
                                    color='transparent',
                                    thickness=1
                                ),
                                ft.Text(
                                    'Boteco não é bagunça,\ne sua conta também não!',
                                    width=self.page.width * 0.8,
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                    color=AMARELO
                                ),
                                ft.Divider(
                                    height=20,
                                    color='transparent',
                                    thickness=1
                                ),
                                ft.Text(
                                    f'Salve {user_infos.get('name').split()[0]}, bora beber sem dor de cabeça?',
                                    width=self.page.width * 0.9,
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                    color=BRANCO
                                )
                            ]
                        ),
                        ft.Text(
                            'A da conta o gente resolve...\nMas a de amanhã é com você! ^^',
                            size=14,
                            width=self.page.width * 0.5,
                            text_align=ft.TextAlign.CENTER,
                            color=BRANCO
                        ),
                        ft.Container(expand=True),
                        ft.Text(
                            'Clica no botão e joga essa dor de cabeça no nosso peito!',
                            size=14,
                            width=self.page.width * 0.5,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color=AMARELO
                        ),
                        self.arrow_stack
                    ]
                )
            )
        ]
        threading.Thread(target=self.animate_arrow, daemon=True).start() # Inicia a animação da seta

    def animate_arrow(self):
        """
        Animação do ícone de seta para baixo.
        Faz o ícone subir e descer suavemente.
        """
        while True:
            for offset in [0, 90]:
                self.arrow_icon.height = offset
                self.page.update()
                time.sleep(0.5)



