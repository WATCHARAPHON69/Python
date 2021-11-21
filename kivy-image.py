


# Program to explain how to add image in kivy
  
# import kivy module   
import kivy 

import cv2
# base Class of your App inherits from the App class.   
# app:always refers to the instance of your application  
from kivy.app import App
cap = cv2.VideoCapture(1)
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require('1.9.0')
  
# The Image widget is used to display an image
# this module contain all features of images
from kivy.uix.image import Image
  
# creating the App class
class MyApp(App):
  
    # defining build()
      
    def build(self):
          
        # return image
        _,fram=cap.read()
        cv2.imwrite('ggg.jpg', fram)
        return Image(source ='ggg.jpg')
  
# run the App
MyApp().run()