from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout

# See https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html

            
class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        
            s = Screen()
            s.add_widget(Label(text=l))
            self.ids.sm.add_widget(s)
            self.ids.buttons.add_widget()

class AnotherScreen(ScreenManagement):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("window.kv")

class MainApp(App):
    
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()
        
    