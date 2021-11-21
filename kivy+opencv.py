from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import time

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):

        
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)
    

    def update(self, dt):
        l=0
        
        p=0
        t = time.localtime()
        f = time.localtime()
        Time = time.strftime("%S",t)
        Ti = time.strftime("%H:%M:%S",f)   

  
        ret, frame = self.capture.read(0)                                                       
        if(Time ==1):
            fps=0
        cv2.putText(frame,"Time "+Ti+" FPS "+str(fps),(0,50),0,1,(0,0,255),cv2.LINE_4)

        
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture


class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=60)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()


if __name__ == '__main__':
    CamApp().run()