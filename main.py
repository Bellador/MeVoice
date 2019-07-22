import kivy  # importing main package
from kivy.app import App  # required base class for your app.
from kivy.uix.label import Label  # uix element that will hold text
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require("1.11.1")  # make sure people running py file have right version

# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
class ConnectPage(GridLayout):
#     # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout
        super().__init__(**kwargs)

        self.cols = 1  # used for our grid

        # widgets added in order, so mind the order.
        self.add_widget(Label(text='Command'))  # widget #1, top left
        self.command = TextInput(multiline=False)  # defining self.ip...
        self.add_widget(self.command) # widget #2, top right

        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.submit_it)
        self.add_widget(self.submit_button)

    def submit_it(self, instance):
        myapp.info_page.update_info(self.command.text)
        myapp.screen_manager.current = 'Info'

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.adjust_text_width)
        self.add_widget(self.message)

    def adjust_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None) #None stands for the Y-axis/height

    def update_info(self, message):
        self.message.text = str(message)

class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    myapp = EpicApp()
    myapp.run()