import backend_supabase as db
import flet as ft

def main(page: ft.Page):
    page.title = "IBM Terminology Lookup"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE_900)
    page.window_min_height = 350
    #page.window_max_height = 400
    page.window_min_width = 655
    page.window_height = 615
    page.window_width = 700
    page.scroll = ft.ScrollMode.ADAPTIVE

    def word_searched(self):
        definition = db.get_definition(str(self.control.value))
        other_definitions = db.other_definitions(str(self.control.value))
        results.value = definition
        other_words.value = other_definitions
        word_searched_text.value = str(self.control.value).capitalize()

        # Add searched word to history
        history.controls.append(ft.Text(
                str(self.control.value),
                style=ft.TextThemeStyle.BODY_MEDIUM
            )
        )
        page.update()
    
    def clear_history(self):
        self = history
        # Clear history
        while True:
            try:
                self.controls.remove(self.controls[0])
            except Exception:
                break
        
        # Reset seach and results to default values
        word_searched_text.value = 'Definitions'
        search.value = ''
        results.value = ''
        other_words.value = ''
        page.update()
    
    def swap_theme_color(self):
        c_options = {
                     "RED": ft.colors.RED_800,
                     "ORANGE": ft.colors.ORANGE_800,
                     "YELLOW": ft.colors.YELLOW_700,
                     "GREEN": ft.colors.GREEN_800,
                     "BLUE": ft.colors.BLUE_900,
                     "PURPLE": ft.colors.PURPLE_900,
                     }
        page.theme = ft.Theme(color_scheme_seed=c_options[self.control.text])  # Change theme color
        page.appbar.bgcolor = c_options[self.control.text]  # Change banner color to match theme
        page.update()
    
    def swap_dark_mode(*args):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def add_word(self):
        db.add_definition(word=new_word.value, definition=new_word_def.value)

    results = ft.Text(
        style=ft.TextThemeStyle.BODY_SMALL
    )

    other_words = ft.Text(
        style=ft.TextThemeStyle.BODY_SMALL
    )

    history = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,     
    )

    word_searched_text = ft.Text(
        value="Definitions",
        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
    )
    
    clear_button = ft.ElevatedButton(
        text="Clear", 
        tooltip="Clear search history",
        width=300,
        on_click=clear_history
    )

    search = ft.TextField(
            label="Search", 
            tooltip="Look up word definition",
            on_submit=word_searched
    )

    new_word = ft.TextField(
            label="Word",
            multiline=True,
            min_lines=1,
            max_lines=3,
            expand=True,
    )

    new_word_def = ft.TextField(
            label="Definition",
            multiline=True,
            min_lines=1,
            max_lines=3,
            expand=True,
    )

    ibm_logo = ft.Container(
        width=100,
        # alignment=ft.alignment.center,
        padding=8,
        content=ft.Image(
            src=f"assets\icon_white_200.png",
            width=100,
            height=100,
            fit=ft.ImageFit.SCALE_DOWN,
        )
    )

    page.appbar = ft.AppBar(
        leading=ibm_logo,
        leading_width=100,
        title=ft.Text("Terminology Lookup"),
        center_title=False,
        bgcolor=ft.colors.BLUE_900,
        color= ft.colors.WHITE,
        actions=[
            ft.PopupMenuButton(
                icon = ft.icons.ADD,
                tooltip="Add definition",
                items = [
                    ft.PopupMenuItem(
                        content=ft.Row([ 
                                ft.Container(
                                    height=86,
                                    width=300,
                                    alignment=ft.alignment.center,
                                    padding=10,
                                    border_radius=10,
                                    expand=True,

                                    content=ft.Column(
                                        controls=[new_word]
                                    )        
                                )
                            ]
                        )
                    ),
                    ft.PopupMenuItem(
                        content=ft.Row([ 
                                ft.Container(
                                    height=86,
                                    width=300,
                                    alignment=ft.alignment.center,
                                    padding=10,
                                    border_radius=10,
                                    expand=True,

                                    content=ft.Column(
                                        controls=[new_word_def]
                                    )        
                                )
                            ]
                        )
                    ),
                    ft.ElevatedButton(
                        content=ft.Row([ 
                                ft.Container(
                                    height=60,
                                    width=300,
                                    alignment=ft.alignment.center,
                                    padding=10,
                                    border_radius=10,
                                    expand=True,

                                    content=ft.Column(
                                        controls=[
                                            ft.ElevatedButton(
                                                text="Add word",
                                                tooltip="Add word and definition to dictionary",
                                                width=300,
                                                expand=True,
                                                on_click=add_word
                                            )
                                        ]
                                    )        
                                )
                            ]
                        )
                    )
                ]
            ),
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                tooltip="Dark mode",
                on_click=swap_dark_mode
            ),
            ft.PopupMenuButton(
                icon = ft.icons.PALETTE,
                tooltip="Theme color",
                items = [
                    ft.PopupMenuItem(
                        on_click=swap_theme_color,
                        text="RED",
                        content=ft.Row([ 
                                ft.Icon(
                                    name=ft.icons.PALETTE,
                                    color=ft.colors.RED_800
                                ),
                                ft.Text("Red")
                            ]
                        )
                    ),
                    ft.PopupMenuItem(
                        on_click=swap_theme_color,
                        text="ORANGE",
                        content=ft.Row([
                                ft.Icon(
                                    name=ft.icons.PALETTE,
                                    color=ft.colors.ORANGE_800
                                ),
                                ft.Text("Orange")
                            ]
                        )
                    ),
                    ft.PopupMenuItem(
                        on_click=swap_theme_color,
                        text="YELLOW",
                        content=ft.Row([
                                ft.Icon(
                                    name=ft.icons.PALETTE,
                                    color=ft.colors.YELLOW_800
                                ),
                                ft.Text("Yellow")
                            ]
                        )
                    ),
                    ft.PopupMenuItem(
                        on_click=swap_theme_color,
                        text="GREEN",
                        content=ft.Row([
                                ft.Icon(
                                    name=ft.icons.PALETTE,
                                    color=ft.colors.GREEN_800
                                ),
                                ft.Text("Green")
                            ]
                        )
                    ),
                    ft.PopupMenuItem(
                        on_click=swap_theme_color,
                        text="BLUE",
                        content=ft.Row([
                                ft.Icon(
                                    name=ft.icons.PALETTE,
                                    color=ft.colors.BLUE_900
                                ),
                                ft.Text("Blue")
                            ]
                        )
                    ),
                    ft.PopupMenuItem(
                        on_click=swap_theme_color,
                        text="PURPLE",
                        content=ft.Row([
                                ft.Icon(
                                    name=ft.icons.PALETTE,
                                    color=ft.colors.PURPLE_900
                                ),
                                ft.Text("Purple")
                            ]
                        )
                    )
                ]
            )
        ]
    )

    # create app control and add it to the page
    page.add(ft.Column(
            alignment=ft.alignment.center,
            controls=[
                ft.Row(
                    alignment=ft.alignment.center,
                    controls=[
                        #Left Container
                        ft.Container(
                            height=500,
                            width=300,
                            alignment=ft.alignment.center,
                            padding=10,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            border_radius=10,

                            content=ft.Column(
                                controls=[
                                    search,
                                    history,
                                    clear_button
                                ]
                            )        
                        ),

                        #Right Container
                        ft.Container(
                            height=500,
                            expand=True,
                            alignment=ft.alignment.center_left,
                            padding=10,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            border_radius=10,

                            content=ft.Column(
                                controls=[
                                    word_searched_text,
                                    results,
                                    other_words
                                ]
                            )
                        )
                    ]
                )
            ]
        )
    )
    
ft.app(target=main)