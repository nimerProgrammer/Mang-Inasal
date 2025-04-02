from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.label import MDLabel, MDIcon
from kivy.metrics import dp, sp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard


c_Name = None
c_user = None
c_pass = None

KV = '''

ScreenManager:
    LoginScreen:
    SignupScreen:
    HomeScreen:

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        md_bg_color: 1.0, 0.84, 0.0, 1

        ScrollView:
            do_scroll_x: False  # Disable horizontal scrolling
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(20)
                size_hint_y: None  # Allow scrolling
                height: self.minimum_height  # Expand based on content
                md_bg_color: 1.0, 0.84, 0.0, 1

                Image:
                    source: 'mang.png'
                    size_hint: None, None
                    size: dp(200), dp(150)
                    pos_hint: {"center_x": 0.5}

                MDCard:
                    elevation: 0
                    radius: dp(15)
                    padding: dp(20)
                    size_hint: None, None
                    size: dp(280), dp(300)
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 1, 1, 1, 0.2

                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: dp(10)
                        adaptive_height: True  # Expand based on children

                        MDTextField:
                            id: username
                            hint_text: "Username"
                            icon_right: "email"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDTextField:
                            id: password
                            hint_text: "Password"
                            password: True
                            icon_right: "eye-off"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        

                        MDLabel:
                            text: "Forgot Password?"
                            theme_text_color: "Custom"
                            text_color: 0.05, 0.43, 0.99, 1
                            halign: "center"
                            size_hint_y: None
                            height: dp(30)

                        MDRaisedButton:
                            text: "Login"
                            md_bg_color: 0, 0.6, 0, 1
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1
                            on_release: app.login()

                        MDRaisedButton:
                            text: "Sign Up"
                            md_bg_color: 0.05, 0.43, 0.99, 1
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1
                            on_release: app.go_to_signup()

                        

<SignupScreen>:
    name: 'signup'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        md_bg_color: 1.0, 0.84, 0.0, 1

        ScrollView:
            do_scroll_x: False
            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(20)
                size_hint_y: None
                height: self.minimum_height
                md_bg_color: 1.0, 0.84, 0.0, 1

                Image:
                    source: 'mang.png'
                    size_hint: None, None
                    size: dp(200), dp(150)
                    pos_hint: {"center_x": 0.5}

                MDCard:
                    elevation: 0
                    radius: dp(15)
                    padding: dp(20)
                    size_hint: None, None
                    size: dp(280), dp(330)
                    pos_hint: {"center_x": 0.5}
                    md_bg_color: 1, 1, 1, 0.2

                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: dp(10)
                        adaptive_height: True

                        MDTextField:
                            id: fullname
                            hint_text: "Full Name"
                            icon_right: "account"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDTextField:
                            id: username
                            hint_text: "Username"
                            icon_right: "account"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}
                            
                        MDTextField:
                            id: password
                            hint_text: "Password"
                            password: True
                            icon_right: "eye-off"
                            size_hint_x: 1
                            pos_hint: {'center_x': 0.5}

                        MDRaisedButton:
                            text: "Submit"
                            md_bg_color: 0, 0.6, 0, 1
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: 1
                            on_release: app.signup()

                        MDLabel:
                            text: "Already have an account? [ref=login]Login[/ref]"
                            markup: True  
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "center"
                            size_hint_y: None
                            height: dp(30)
                            on_ref_press: app.go_to_login()

                            
<HomeScreen>:
    name: 'home'
    md_bg_color: (0.0, 0.58, 0.29, 1)
    BoxLayout:
        orientation: 'horizontal'

        MDNavigationRail:
            id: nav_rail
            size_hint_x: None
            opacity: 1
            theme_text_color: "Custom"

            MDNavigationRailFabButton:
                id: rail_fab_button  
                icon: "home"
                
            MDNavigationRailItem:
                icon: "home"
                text: "Home"
                on_release: app.switch_content("home")

            MDNavigationRailItem:
                icon: "view-dashboard"
                text: "Dashboard"
                on_release: app.switch_content("dashboard")

            MDNavigationRailItem:
                icon: "account"
                text: "Profile"
                on_release: app.switch_content("profile")

            MDNavigationRailItem:
                icon: "cog"
                text: "Settings"
                on_release: app.switch_content("settings")

            MDNavigationRailItem:
                icon: "logout"
                text: "Logout"
                on_release: app.logout()

        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 1

            MDTopAppBar:
                title: "Mang Inasal"
                left_action_items: [["menu", lambda x: app.toggle_sidebar()]]
                
            BoxLayout:
                id: page_name
                orientation: 'vertical'
                spacing: dp(10)
                padding: (dp(20), dp(30), dp(20), dp(20))
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Mang Inasal"
                    font_style: "H5"
                    halign: "center"
                    theme_text_color: "Primary"

            ScrollView:
                BoxLayout:
                    id: content_area
                    orientation: 'vertical'
                    spacing: dp(10)
                    padding: (dp(20), dp(20), dp(20), dp(60))
                    size_hint_y: None
                    height: self.minimum_height
'''

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class Application(MDApp):
   
    def build(self):
         # ✅ Set Theme (Light or Dark)
        self.theme_cls.theme_style = "Light"

        # ✅ Set a valid primary_palette
        self.theme_cls.primary_palette = "Green"  # Only use predefined palettes
        self.theme_cls.primary_hue = "800"  # Make it darker
        
        return Builder.load_string(KV)
    
    def go_to_signup(self):
        self.root.current = 'signup'
        
    def go_to_login(self):
        self.root.current = 'login'
        
    def signup(self):
        global c_Name 
        global c_user 
        global c_pass 

        c_Name = self.root.get_screen('signup').ids.fullname.text
        c_user = self.root.get_screen('signup').ids.username.text
        c_pass = self.root.get_screen('signup').ids.password.text

        self.root.current = 'login'

    def login(self):
        username = self.root.get_screen('login').ids.username.text
        password = self.root.get_screen('login').ids.password.text

        if username == c_user and password == c_pass:
            self.root.current = 'home'
            
            page_name = self.root.get_screen('home').ids.page_name
            fab_button = self.root.get_screen('home').ids.rail_fab_button
            page_name.clear_widgets()

            content_area = self.root.get_screen('home').ids.content_area
            content_area.clear_widgets()
            
            page_name.add_widget(MDLabel(text="Home", halign="left"))
            fab_button.icon = "home"

            home = MDLabel(
                text = f"Welcome to Mang Inasal!\nMr/Ms. {c_Name}",
                halign="center",
                theme_text_color="Custom",
                font_style="H5",
                size_hint_y=None,
                height=dp(50),
            )
            content_area.add_widget(home)
        else:
            self.show_login_failed_dialog()
    dialog = None  # Declare this to avoid re-creating dialogs

    def show_login_failed_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Login Failed",
                text="Invalid username or password.",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()

    def toggle_sidebar(self):
        nav_rail = self.root.get_screen('home').ids.nav_rail
        if nav_rail.width > 0:
            nav_rail.width = 0
            nav_rail.opacity = 0
            nav_rail.disabled = True
        else:
            nav_rail.width = dp(80)
            nav_rail.opacity = 1
            nav_rail.disabled = False

    def switch_content(self, section):
        
        page_name = self.root.get_screen('home').ids.page_name
        fab_button = self.root.get_screen('home').ids.rail_fab_button
        page_name.clear_widgets()

        content_area = self.root.get_screen('home').ids.content_area
        content_area.clear_widgets()

        if section == "dashboard":
            page_name.add_widget(MDLabel(text="Home/dashboard", halign="left"))
            fab_button.icon = "view-dashboard"

            card_colors = {
                "Primary": [0.0, 0.47, 0.75, 1],   # Bootstrap primary
                "Warning": [1.0, 0.84, 0.0, 1],    # Bootstrap warning
                "Success": [0.0, 0.58, 0.29, 1],   # Bootstrap success
            }


            for name, color in card_colors.items():
                card = MDCard(
                    pos_hint = {"center_x": 0.5},
                    size_hint=(1, None),
                    height=150,
                    radius=[12],
                    md_bg_color=color,
                    elevation=4
                )

                card.add_widget(MDLabel(
                    text = "Orders\nTotal: 20" if name == "Primary" else "Order's Pending\nTotal: 5" if name == "Warning" else "Order Received\nTotal: 15",
                    halign="center",
                    valign="center",
                    theme_text_color="Custom",
                    text_color = [0, 0, 0, 1] if name == "Warning" else [1, 1, 1, 1]
                ))

                content_area.add_widget(card)

        elif section == "profile":
            page_name.add_widget(MDLabel(text="Home/profile", halign="left"))
            fab_button.icon = "account"
            
            profile_card = MDCard(
                size_hint=(1, None),
                size=("300dp", "300dp"),
                pos_hint={"center_x": 0.5},
                elevation=4,
                padding=dp(20),
                radius=[12],
            )

            profile_layout = MDBoxLayout(
                orientation="vertical",
                spacing=dp(10)
            )

            profile_layout.add_widget(MDLabel(
                text='Pasquito, Precilia M.',
                halign='center',
                theme_text_color="Custom",
                font_size=sp(57),
                text_color=(0, 0, 0, 1)
            ))

            profile_layout.add_widget(MDLabel(
                text='BSIT - 3A',
                halign='center',
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1)
            ))

            profile_card.add_widget(profile_layout)
            content_area.add_widget(profile_card)

        elif section == "settings":
            page_name.add_widget(MDLabel(text="Home/settings", halign="left"))
            fab_button.icon = "cog"

        elif section == "home":
            page_name.add_widget(MDLabel(text="Home", halign="left"))
            fab_button.icon = "home"

            home = MDLabel(
                text = f"Welcome to Mang Inasal!\nMr/Ms. {c_Name}",
                halign="center",
                theme_text_color="Custom",
                font_style="H5",
                size_hint_y=None,
                height=dp(50),
            )
            content_area.add_widget(home)
        



    def logout(self):
        if not hasattr(self, 'logout_dialog'):
            self.logout_dialog = MDDialog(
                title="Confirm Logout",
                text="Are you sure you want to logout?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=lambda x: self.logout_dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="LOGOUT",
                        on_release=self.confirm_logout
                    ),
                ],
            )
        self.logout_dialog.open()

    def confirm_logout(self, *args):
        self.logout_dialog.dismiss()
        self.root.current = 'login'

Application().run()