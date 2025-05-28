from components.resources import AZUL_CLARO, BRANCO, AMARELO, LOGO_HORIZONTAL
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

        # Instancia o menu inferior e o botão flutuante
        self.bottom_appbar = MyBottomAppBar(page=self.page, user_photo=user_infos.get('photo_url'))
        self.floating_action_button = MyFloatingActionButton(page=self.page)
        self.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

        # Estado da animação
        self.arrow_icon = ft.Container(
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            content=ft.Icon(name=ft.Icons.ARROW_DOWNWARD, size=40, color=BRANCO),
        )

        self.arrow_stack = ft.Stack(
            width=40,
            height=60,
            controls=[self.arrow_icon]
        )


        # Layout principal
        self.controls = [
            ft.Container(
                expand=True,
                margin=ft.margin.all(40),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Image(
                                    src=LOGO_HORIZONTAL,
                                    height=300,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Text(
                                    f"{user_infos.get('name').split()[0]}, você sabe! 🍻\nBoteco não é bagunça,\ne sua conta também não!",
                                    width=self.page.width * 0.8,
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                    color=BRANCO
                                )
                            ]
                        ),
                        ft.Text(
                            'Chega de confusão na hora de dividir a conta do bar.',
                            size=14,
                            width=self.page.width * 0.5,
                            text_align=ft.TextAlign.CENTER,
                            color=BRANCO
                        ),
                        ft.Container(expand=True),  # Espaço para o menu não sobrepor conteúdo
                        ft.Text(
                            'Clica no botão aí embaixo e deixa que a gente resolve',
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
        threading.Thread(target=self.animate_arrow, daemon=True).start()

    def animate_arrow(self):
        while True:
            for offset in [0, 100]:  # movimento suavizado
                self.arrow_icon.height = offset
                self.page.update()
                time.sleep(0.6)



