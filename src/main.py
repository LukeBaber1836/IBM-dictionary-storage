import flet as ft
from elements import Elements

class Dictionary_App(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        Dictionary_App.build(self)


    def build(self):
        self.page.appbar = Elements.app_bar
        self.controls = [
            Elements.main_left_container,
            Elements.main_right_container
        ]


def main(page: ft.Page):
    page.title = "IBM Terms"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE_900)
    page.window_min_height = 350
    page.window_min_width = 655
    page.window_height = 615
    page.window_width = 700

    app = Dictionary_App(page)
    page.add(app)
    
ft.app(target=main)