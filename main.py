from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
import mysql.connector
import mysql

Window.size = (300, 500)

db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='Thepassword59..',
    database="teatalk"
)

mycursor = db.cursor()



class ResetConfirm(Screen):
    pass

class ResetPassword(Screen):
    def resetPassword(self):
        userEmail = self.ids.email.text
        print(userEmail)
        print("Clicked")
        self.manager.current = 'resetConfirm'



class Register(Screen):

    def createAccount(self):
        print("Clicked")
        fullName = self.ids.fullName.text
        print(fullName)
        email = self.ids.newEmail.text
        print(email)
        mycursor.execute("INSERT INTO userinfo(fullname, email) VALUES (%s,%s)", (fullName, email))
        db.commit()



    def logIn(self):
        self.manager.current = "loginPage"


class LoginLayout(Screen):

    def login(self, **kwargs):
        userGrab = self.ids.username.text
        passGrab = self.ids.password.text
        print(userGrab + '\n' + passGrab)

    def signUp(self):
        #once user clicks sign up bring them to a page to create an account
        print('clicked')
        self.manager.current = 'signUpPage'

    def forgotPassword(self):
        #load page for users to reset their profile information
        print("clicked")


class WindowManager(ScreenManager):
    pass


class TeaTalkApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.root_widget = Builder.load_file("TeaTalkKv.kv")
        return self.root_widget

    def set_toolbar_title_halign(self, *args):
        self.ids.toolbar.ids.label_title.halign = "center"


TeaTalkApp().run()