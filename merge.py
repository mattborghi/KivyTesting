from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

Builder.load_file("merge.kv")


class Menu(BoxLayout):
    pass
    #manager = ObjectProperty(None)

class Add(Screen):
    pass

class Help(Screen):
    pass

class Credits(Screen):
    pass

class Manager(ScreenManager):
    pass
    #addScreen = ObjectProperty(None)
    #helpScreen = ObjectProperty(None)
    #creditsScreen = ObjectProperty(None)

class AntsApp(App):

    def build(self):
        return Menu()


if __name__ == '__main__':
    AntsApp().run()