import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label

# The name of the class should be written as 'kv_file_name + App' in orther to work.
class e4App(App):
	def build(self):
		self.title = 'My first application'
		return Label()

if __name__ == '__main__':
	e4App().run()
