import cv2
import tensorflow
import keras
from PIL import Image
image = r'test_photo.jpg'
face_cascade = "haarcascade_frontalface_default.xml"
webcam= cv2.VideoCapture(1)

count = 1
while True:
    success, image_bgr = webcam.read()
    image_org = image_bgr.copy()
    image_bw = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(face_cascade)
    faces = face_classifier.detectMultiScale(image_bw)
    print(f'There are {len(faces)} faces found.')
    for face in faces:
        x, y, w, h = face
    cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(f'mask/mask_{count}.jpg', image_org[y:y + h, x:x + w])
    count += 1
    cv2.imshow("Faces found", image_bgr)
    cv2.waitKey(1)