import flet as ft
from functions import Functions

class Elements(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

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
        on_click=Functions.clear_history
    )

    search = ft.TextField(
            label="Search", 
            tooltip="Look up word definition",
            on_submit=Functions.find_word
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
            src="../assets/icon_white_200.png",
            width=100,
            height=100,
            fit=ft.ImageFit.SCALE_DOWN,
        )
    )

    theme_colors = [
        ft.PopupMenuItem(
            on_click=Functions.swap_theme_color,
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
            on_click=Functions.swap_theme_color,
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
            on_click=Functions.swap_theme_color,
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
            on_click=Functions.swap_theme_color,
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
            on_click=Functions.swap_theme_color,
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
            on_click=Functions.swap_theme_color,
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

    add_word_page = [
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
                                    tooltip="Add word and definition to the dictionary",
                                    width=300,
                                    expand=True,
                                    on_click=Functions.add_word
                                )
                            ]
                        )        
                    )
                ]
            )
        )
    ]

    username = ft.TextField(
            label="Username",
            multiline=True,
            min_lines=1,
            max_lines=3,
            expand=True,
    )

    password = ft.TextField(
            label="Password",
            multiline=True,
            min_lines=1,
            max_lines=3,
            expand=True,
    )

    login_status = ft.Text(
        value="Not logged in",
        color=ft.colors.RED,
        style=ft.TextThemeStyle.BODY_SMALL,
    )

    login_page = [
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
                            controls=[username]
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
                            controls=[password]
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
                                    text="Login",
                                    tooltip="Log into your account",
                                    width=300,
                                    expand=True,
                                    on_click=Functions.login
                                )
                            ]
                        )        
                    )
                ]
            )
        ),
        login_status
    ]

    app_bar = ft.AppBar(
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
                items = add_word_page
            ),
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                tooltip="Dark mode",
                on_click=Functions.swap_dark_mode
            ),
            ft.PopupMenuButton(
                icon = ft.icons.PALETTE,
                tooltip="Theme color",
                items = theme_colors
            ),
            ft.PopupMenuButton(
                icon = ft.icons.PERSON_ROUNDED,
                tooltip="Profile",
                items = login_page
            )
        ]
    )

    main_left_container = ft.Container(
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
    )

    main_right_container = ft.Container(
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
