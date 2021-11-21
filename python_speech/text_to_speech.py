import pyaudio
import speech_recognition as sr
import os
import keyboard as kb
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(1)
recog = sr.Recognizer()
def run():
    with mic as source:
        print(source)
        while True:
            try:
                audio = recog.listen(source)
                text = recog.recognize_google(audio,language='th')
                print(text)
                if text == "อาดูโน่":
                    print("โปรแกรมอาดูโน่")
                    x= os.startfile("C:\\Program Files (x86)\Arduino\\arduino.exe")
                if text == "pycharm":
                    #pass
                    os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe")
                if text == "Code":
                    os.startfile("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                if text == "ปิดอาดูโน่":
                    print("close")
                    os.close(x)

            except:
                continue
def key():
    while True:
        if kb.is_pressed('o'):
            x = os.startfile("C:\\Program Files (x86)\Arduino\\arduino.exe")
            print("OPEN")
        if kb.is_pressed('c'):
            os.c(x)
            print("CLOCE")

key()