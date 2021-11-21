import cv2
import mediapipe as mp
import time
import serial
ser = serial.Serial("COM6")
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
x=["","","","","","","","","","","","","","","","","","","","",""]
m=0
while 1:

    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                x[id]=str(cy)
                

                #print("id = : ",id, "cx = : ",cx, "cy = : ",cy)
                # if id == 4:
                #cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            #print(id)
           
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            print(x)
            

           



    cv2.imshow("Image", img)
    m+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stop")
        break
cv2.destroyAllWindows()