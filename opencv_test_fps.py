from inspect import FrameInfo
import cv2
import time
#cap = cv2.VideoCapture('rtsp://192.168.43.1:8080/h264_pcm.sdp')
cap = cv2.VideoCapture(0)
l =0
fps=0
p=1
while(True):
    t = time.localtime()
    Time = time.strftime("%S",t)
    
    if(Time != l):
        p+=1
        l = Time
    elif(Time == l):
        p=0
    if(p==0):
        fps+=1
    elif(p!=0):
        #print("FPS = ",fps)
        tt = str(fps)
        fps=0
        
    _,Frame = cap.read()
    cv2.putText(Frame,"FPS "+tt,(0,50),0,1,(0,0,255),3)
    cv2.imshow('frame',Frame)
    #print(Time," : ",l," : ",p ,"FPS = ",fps)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stop")
        break
