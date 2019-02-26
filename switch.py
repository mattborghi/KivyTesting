
import kivy

kivy.require('1.9.1')

 

from kivy.app import App

from kivy.uix.switch import Switch

from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label

 

# A Gridlayout with a label a switch

class SwitchContainer(GridLayout):

     def __init__(self, **kwargs):

          super(SwitchContainer, self).__init__(**kwargs)

          self.cols = 2

          self.add_widget(Label(text="Sample Settings:"))

 

          self.settings_sample = Switch(active=False)

          self.add_widget(self.settings_sample)

         

          self.settings_sample.bind(active=switch_callback)       

 

# Callback for the switch state transition

def switch_callback(switchObject, switchValue):

     print('Value of sample settings is:', switchValue)

 

# The App

class SwitchExample(App):

     def build(self):

          return SwitchContainer()

 

# Run the kivy app

if __name__ == '__main__':

     SwitchExample().run()