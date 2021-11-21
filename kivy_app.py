from kivy.app import App
from kivy.uix.label import Label
class test(App):
	def build(self):
		return Label(text="hello")
test().run()