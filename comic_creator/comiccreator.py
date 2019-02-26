 # File name: comiccreator.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

# There is no need to explicitely load comiccreator.kv because Kivy automatically loads it by extracting the first part of the ComicCreatorApp name.
Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('comicwidgets.kv')

class ComicCreator(AnchorLayout):
	pass

class ComicCreatorApp(App):
	def build(self):
		return ComicCreator()

if __name__ == "__main__":
	ComicCreatorApp().run()