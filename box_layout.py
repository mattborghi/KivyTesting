import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class MyW(FloatLayout):
	pass

class e7App(App):
	def build(self):
		return MyW()

if __name__ == '__main__':
	e7App().run()