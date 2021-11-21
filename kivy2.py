from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
class test(App):
	def build(self):
		return Button(text="hello")
		return Button(text="pust")
test().run()