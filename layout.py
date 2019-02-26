import kivy
kivy.require('1.10.0') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class MyW(Widget):
	# Root class. In the init constructor we add the FloatLayout widget as follows:
	def __init__(self, **kwargs):
		super(MyW, self).__init__(**kwargs)
		self.MyW1_name=MyW1()
		self.add_widget(self.MyW1_name)

class MyW1(FloatLayout):
	def __init__(self, **kwargs):
		super(MyW1, self).__init__(**kwargs)
		# Set size to the FloatLayout method
		self.size=(300,300)

class e5App(App):
	def build(self):
		return MyW()

if __name__ == '__main__':
	e5App().run()