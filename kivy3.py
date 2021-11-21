from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout class LoginsScreen (GridLayout): 
	def __init__(self, **kwargs): 
		super (LoginScreen, self).__init__(**kwargs):  
		self.add widget (Label (text="Username")) 
class MyApp (App) :
	 def build (self): 
	 	return LoginScreen ()
MyApp () .run ()