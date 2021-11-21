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
y=["","","","","","","","","","","","","","","","","","","","",""]
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                x[id]=str(cx)
                y[id]=str(cy)
                #print(type(cx)

                #print("id = : ",id, "cx = : ",cx, "cy = : ",cy)
                # if id == 4:
                #cv2.circle(img, (cx, cy), 10, (0, 255, 0), 1)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            print( int(x[0])-int(x[7]))
            #if(  int(x[0])-int(x[7]) <50):
                #print("1")
            #   cv2.putText(img,"1", (10, 300), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
            #    ser.write(bytes("N",'utf-8'))
            #else:
                #print("0")
            #    cv2.putText(img, "0", (10, 300), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
            #    ser.write(bytes("F",'utf-8'))

           



    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Stop")
        break
cv2.destroyAllWindows()