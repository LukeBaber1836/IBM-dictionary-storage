import flet as ft
import backend_supabase as db

class Functions(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page


    def find_word(self):
        definition = db.get_definition(self.control.value)
        other_definitions = db.other_definitions(self.control.value)

        word_searched_text = self.page._controls[0]._Row__controls[1]._Container__content._Column__controls[0]
        results = self.page._controls[0]._Row__controls[1]._Container__content._Column__controls[1]
        other_words = self.page._controls[0]._Row__controls[1]._Container__content._Column__controls[2]

        # Update word_searched_text, results, other_words variables respectively
        word_searched_text.value = str(self.control.value).capitalize()
        results.value = definition
        other_words.value = other_definitions
        


        # Add searched word to history variable
        history = self.control._Control__page._controls[0]._Row__controls[0]._Container__content._Column__controls[1].controls
        history.append(ft.Text(
                str(self.control.value),
                style=ft.TextThemeStyle.BODY_MEDIUM
            )
        )
        self.page.update()


    def clear_history(self):
        history = self.control._Control__page._controls[0]._Row__controls[0]._Container__content._Column__controls[1]

        # Clear history
        while True:
            try:
                history.controls.pop(0)
            except IndexError:
                break        

        # Reset seach and results to default values
        word_searched_text = self.page._controls[0]._Row__controls[1]._Container__content._Column__controls[0]
        search = self.page._controls[0]._Row__controls[0]._Container__content._Column__controls[0]
        results = self.page._controls[0]._Row__controls[1]._Container__content._Column__controls[1]
        other_words = self.page._controls[0]._Row__controls[1]._Container__content._Column__controls[2]

        word_searched_text.value = 'Definitions'
        search.value = ''
        results.value = ''
        other_words.value = ''
        self.page.update()
    

    def swap_theme_color(self):
        color_options = {
                        "RED": ft.colors.RED_800,
                        "ORANGE": ft.colors.ORANGE_800,
                        "YELLOW": ft.colors.YELLOW_700,
                        "GREEN": ft.colors.GREEN_800,
                        "BLUE": ft.colors.BLUE_900,
                        "PURPLE": ft.colors.PURPLE_900,
                        }
        self.page.theme = ft.Theme(color_scheme_seed=color_options[self.control.text])  # Change theme color
        self.page.appbar.bgcolor = color_options[self.control.text]  # Change banner color to match theme
        self.page.update()


    def swap_dark_mode(self):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()


    def add_word(self):
        db.add_definition(
            word=self.page.appbar._AppBar__actions[0]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].value,
            definition=self.page.appbar._AppBar__actions[0]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].value
            )
        self.page.update()


    def login_or_logout(self):
        username = self.page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].value
        pw = self.page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].value
        login_status_text = self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[3]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0]

        # Handles login
        if db.login_state == False:
            login_success = db.login(username, pw)

            if login_success == True:
                login_status_text.color = ft.colors.GREEN
                login_status_text.value = "You are logged in!"
                self.control.text = "Sign Out"
                username=''
                pw=''
                # Hide credential inputs
                self.page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0].height=0
                self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0].visible=False
                self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].visible=False

                self.page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0].height=0
                self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0].visible=False
                self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].visible=False

            else:
                login_status_text.value = "Incorrect username or password!"
        
        # Handles log out
        else:
            self.control.text = "Log In"
            login_status_text.color = ft.colors.RED
            login_status_text.value = "You are logged out!"
            
            # Unhide credential inputs
            self.page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0].height=86
            self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0].visible=True
            self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].visible=True

            self.page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0].height=86
            self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0].visible=True
            self.control._Control__page.appbar._AppBar__actions[3]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].visible=True

            db.sign_out()

        self.page.update()


    def sign_up(self):
        email = self.page.appbar._AppBar__actions[4]._PopupMenuButton__items[0]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].value
        pw = self.page.appbar._AppBar__actions[4]._PopupMenuButton__items[1]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0].value
        signup_status_text = self.control._Control__page.appbar._AppBar__actions[4]._PopupMenuButton__items[3]._PopupMenuItem__content._Row__controls[0]._Container__content._Column__controls[0]

        # Handles login
        signup_success = db.sign_up(email, pw)

        if signup_success == True:
            signup_status_text.color = ft.colors.GREEN
            signup_status_text.value = f"{email} is registered\nCheck your email!"
            username=' '
            pw=' '
        else:
            signup_status_text.value = "Could not sign up with that email"

        self.page.update()


    def login_status(self):
        return db.login_state


if __name__ == "__main__":
    # Functions.find_word("hello")
    pass