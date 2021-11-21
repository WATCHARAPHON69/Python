import cv2
import mediapipe as mp
webcam = cv2.VideoCapture(0)

image = webcam.read()
mp_hands = mp.solutions.hands
