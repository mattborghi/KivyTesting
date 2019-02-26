# uix related

from kivy.uix.widget import Widget

from kivy.uix.label import Label

from kivy.uix.checkbox import CheckBox

from kivy.uix.gridlayout import GridLayout

 

# Graphics related

from kivy.graphics import InstructionGroup

from kivy.graphics import Color

from kivy.graphics import Rectangle

 

from kivy.app import App

 

from kivy.core.window import Window

 

 

# Container class for the app's widgets

class UserInterface(GridLayout):

 

    def __init__(self, **kwargs):

        super(UserInterface, self).__init__(**kwargs)

       

        # Add labels and checkbox

        self.cols = 2

        self.add_widget(Label(text='Rotate Mode'))

        self.cb_roateMode = CheckBox(active=True)

        self.add_widget(self.cb_roateMode)

       

        self.lbl_roateMode = Label(text='Rotate Mode is on')

        self.add_widget(self.lbl_roateMode)

       

        # Change the color of the background to grey

        blue = InstructionGroup()

        blue.add(Color(1, 1, 1, .3))

        blue.add(Rectangle(pos=self.pos, size=(Window.width, Window.height)))

        self.canvas.add(blue)

       

        # Attach a callback

        self.cb_roateMode.bind(active=self.on_roateMode_Active)

 

    # Callback for the checkbox

    def on_roateMode_Active(self, checkboxInstance, isActive):

        if isActive:

            self.lbl_roateMode.text = "Rotate mode is on"

        else:

            self.lbl_roateMode.text = "Rotate mode is off"

 

# App derived from App class

class CheckBoxApp(App):

 

    def build(self):

        ux = UserInterface()

        return ux

 

# Run the app

if __name__ == '__main__':

    CheckBoxApp().run()        