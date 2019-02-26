from kivy.app import App
#   import a Gridlayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


#   GridLayout is used as a Base for our Root Widget (LoginScreen)
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        #   in the class LoginScreen, we override the method __init__() 
        #   so as to add widgets and to define their behavior:
        super(LoginScreen, self).__init__(**kwargs)
        #   We ask the GridLayout to manage its children in two columns 
        #   and add a Label and a TextInput for the username and password.
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()