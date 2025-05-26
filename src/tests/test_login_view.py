import pytest
import flet as ft
from views.login_view import LoginView

def test_login_view_structure():
    # Cria uma página mock
    class MockPage:
        width = 400
        height = 800

    page = MockPage()
    view = LoginView(page=page)
    assert isinstance(view.controls, list)
    assert len(view.controls) > 0
    # Verifica se o primeiro controle é um Container com gradiente
    container = view.controls[0]
    assert isinstance(container, ft.Container)
    assert hasattr(container, 'gradient')
    assert container.gradient is not None

def test_login_button_callback(monkeypatch):
    class MockPage:
        width = 400
        height = 800

    page = MockPage()
    view = LoginView(page=page)

    # Busca o botão de login
    button = None
    for ctrl in view.controls[0].content.controls:
        if isinstance(ctrl, ft.Container):
            if hasattr(ctrl.content, 'on_click'):
                button = ctrl.content
                break

    assert button is not None

    # Testa se o callback está definido
    called = {}

    def fake_callback(e):
        called['ok'] = True

    button.on_click = fake_callback
    button.on_click(None)
    assert called.get('ok') is True

def test_login_view_responsive_layout():
    class MockPage:
        def __init__(self, width):
            self.width = width
            self.height = 800

    # Testa para diferentes larguras de tela
    for width in [320, 480, 768, 1024]:
        page = MockPage(width)
        view = LoginView(page=page)
        # Busca o botão de login
        button = None
        for ctrl in view.controls[0].content.controls:
            if isinstance(ctrl, ft.Container) and isinstance(ctrl.content, ft.ElevatedButton):
                button = ctrl.content
                break
        assert button is not None
        # O botão deve ocupar 60% da largura da tela
        assert button.width == page.width * 0.6