import kivy
kivy.require('1.10.0') 
from kivy.app import App
from kivy.uix.widget import Widget

class MyW(Widget):
	def my_callback(self):
		self.ids.label1.text = 'Click ! '
	def my_callback1(self, inpt):
		self.ids.label1.text = 'Enter ! ' + str(inpt)

class e1App(App):
	def build(self):
		return MyW()
if __name__ == '__main__':
	e1App().run()