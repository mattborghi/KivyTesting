import kivy
kivy.require('1.10.1') # replace with your current kivy version !

#	It’s required that the base Class of your App inherits from the App class. 
#	It’s present in the kivy_installation_dir/kivy/app.py.
from kivy.app import App
#	One important thing to note here is the way packages/classes are laid out. 
#	The uix module is the section that holds the user interface elements like layouts and widgets.
from kivy.uix.label import Label


#	sub-classing the App class
class MyApp(App):
	#	implementing its build() method so it returns a Widget instance (the root of your widget tree)	
	def build(self):
		self.title = 'My first application'
		return Label(text='Hello world')

if __name__ == '__main__':
	#	instantiating this class, and calling its run() method.
	MyApp().run()

#	Check /usr/lib/python3/dist-packages/kivy for additional info