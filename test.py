from kivy.app import App
from kivy.uix.button import Button

class test(App):
    def build(self):
        return Button(text="hello")
test().run()