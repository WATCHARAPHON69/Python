import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import serial
ser = serial.Serial("COM6")
################################
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        length = math.hypot(x2 - x1, y2 - y1)



        if length < 50:
            cv2.putText(img, "ON", (10, 300), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            ser.write(bytes("N",'utf-8'))
        elif length > 50:
            cv2.putText(img, "OFF", (10, 300), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
            ser.write(bytes("F", 'utf-8'))



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stop")
        break