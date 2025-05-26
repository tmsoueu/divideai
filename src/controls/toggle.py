import flet as ft

class Toggle(ft.Switch):
    """
    Componente de alternância personalizado para trocar o tema da aplicação.
    """

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.focus_color = None
        self.hover_color = None
        self.height = 30
        self.top = 30
        self.right = 10

        # Inicializa o valor do switch baseado no tema atual da página
        self.value = self.page.theme_mode == ft.ThemeMode.LIGHT

        self.on_change = self.change_theme

    def change_theme(self, e: ft.ControlEvent):
        """
        Altera o tema da página com base no estado do toggle.
        """
        if self.value:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
        print("Tema atual:", self.page.theme_mode)
        self.page.update()
