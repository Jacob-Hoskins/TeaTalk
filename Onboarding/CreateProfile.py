from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (300, 500)

class FirstStep(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class SignUp(MDApp):
    def build(self):
        self.root_widget = Builder.load_file("createProfile.kv")
        return self.root_widget
        return self.root_widget

app = SignUp()
app.run()