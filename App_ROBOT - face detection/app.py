# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QDateTime
from PyQt5.QtGui import QImage
import cv2, imutils
import keyboard as kb
import numpy as np
from pyzbar.pyzbar import Decoded, decode
from socket import *
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1901, 1026)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IP_label = QtWidgets.QLabel(self.centralwidget)
        self.IP_label.setGeometry(QtCore.QRect(40, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.IP_label.setFont(font)
        self.IP_label.setStyleSheet("")
        self.IP_label.setObjectName("IP_label")
        self.PORT_label = QtWidgets.QLabel(self.centralwidget)
        self.PORT_label.setGeometry(QtCore.QRect(418, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PORT_label.setFont(font)
        self.PORT_label.setObjectName("PORT_label")
        self.IP_input = QtWidgets.QLineEdit(self.centralwidget)
        self.IP_input.setGeometry(QtCore.QRect(102, 21, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.IP_input.setFont(font)
        self.IP_input.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.IP_input.setObjectName("IP_input")
        self.PORT_input = QtWidgets.QLineEdit(self.centralwidget)
        self.PORT_input.setGeometry(QtCore.QRect(548, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PORT_input.setFont(font)
        self.PORT_input.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.PORT_input.setObjectName("PORT_input")
        self.W_Button = QtWidgets.QPushButton(self.centralwidget)
        self.W_Button.setGeometry(QtCore.QRect(104, 766, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.W_Button.setFont(font)
        self.W_Button.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-color: rgb(0, 0, 255);")
        self.W_Button.setObjectName("W_Button")
        self.A_Button = QtWidgets.QPushButton(self.centralwidget)
        self.A_Button.setGeometry(QtCore.QRect(10, 860, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.A_Button.setFont(font)
        self.A_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.A_Button.setObjectName("A_Button")
        self.S_Button = QtWidgets.QPushButton(self.centralwidget)
        self.S_Button.setGeometry(QtCore.QRect(105, 860, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.S_Button.setFont(font)
        self.S_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.S_Button.setObjectName("S_Button")
        self.D_Button = QtWidgets.QPushButton(self.centralwidget)
        self.D_Button.setGeometry(QtCore.QRect(200, 860, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.D_Button.setFont(font)
        self.D_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.D_Button.setObjectName("W_Button_3")
        self.Connect_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_Button.setGeometry(QtCore.QRect(710, 19, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Connect_Button.setFont(font)
        self.Connect_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Connect_Button.setObjectName("Connect_Button")
        self.Video_Streaming = QtWidgets.QLabel(self.centralwidget)
        self.Video_Streaming.setGeometry(QtCore.QRect(350, 120, 1541, 841))
        self.Video_Streaming.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Video_Streaming.setText("")
        self.Video_Streaming.setPixmap(QtGui.QPixmap("../QT5_UI_Image/image-30938-800.jpg"))
        self.Video_Streaming.setObjectName("Video_Streaming")
        self.IP_cam_label = QtWidgets.QLabel(self.centralwidget)
        self.IP_cam_label.setGeometry(QtCore.QRect(940, 19, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.IP_cam_label.setFont(font)
        self.IP_cam_label.setObjectName("IP_cam_label")
        self.IP_cam_input = QtWidgets.QLineEdit(self.centralwidget)
        self.IP_cam_input.setGeometry(QtCore.QRect(1102, 17, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.IP_cam_input.setFont(font)
        self.IP_cam_input.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.IP_cam_input.setObjectName("IP_cam_input")
        self.Connect_Button_ipcam = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_Button_ipcam.setGeometry(QtCore.QRect(1600, 16, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Connect_Button_ipcam.setFont(font)
        self.Connect_Button_ipcam.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Connect_Button_ipcam.setObjectName("Connect_Button_ipcam")
        self.Temp_label = QtWidgets.QLabel(self.centralwidget)
        self.Temp_label.setGeometry(QtCore.QRect(100, 110, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Temp_label.setFont(font)
        self.Temp_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.Temp_label.setObjectName("Temp_label")
        self.DateTime_label = QtWidgets.QLabel(self.centralwidget)
        self.DateTime_label.setGeometry(QtCore.QRect(100, 330, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.DateTime_label.setFont(font)
        self.DateTime_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.DateTime_label.setObjectName("DateTime_label")
        self.Co2_label = QtWidgets.QLabel(self.centralwidget)
        self.Co2_label.setGeometry(QtCore.QRect(110, 220, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Co2_label.setFont(font)
        self.Co2_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.Co2_label.setObjectName("Co2_label")
        self.TempOut = QtWidgets.QLabel(self.centralwidget)
        self.TempOut.setGeometry(QtCore.QRect(126, 168, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TempOut.setFont(font)
        self.TempOut.setObjectName("Temp_label_2")
        self.Co2Out = QtWidgets.QLabel(self.centralwidget)
        self.Co2Out.setGeometry(QtCore.QRect(128, 270, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Co2Out.setFont(font)
        self.Co2Out.setObjectName("Temp_label_3")
        self.TimeOut= QtWidgets.QLabel(self.centralwidget)
        self.TimeOut.setGeometry(QtCore.QRect(83, 387, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TimeOut.setFont(font)
        self.TimeOut.setObjectName("Temp_label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1901, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.IP_CONNECT_STATUS = False
        self.CAM_CONNECT_STATUS = False
        self.START_STATUS_CAM = False
        self.DataIN = ""
        self.L1 = "F"
        self.L2 = "F"
        self.L3 = "F"
        self.L4 = "F"
        self.Data=["","",""]
        self.number = 0
        self.arr = 0
        self.face_cascade = "haarcascade_frontalface_default.xml"


        self.timer_cam = QTimer()
        self.timer_ip = QTimer()
        self.timer_cam.timeout.connect(self.showTime_cam)
        self.timer_ip.timeout.connect(self.showTime_ip)


        self.msg = QMessageBox()
        self.Connect_Button_ipcam.clicked.connect(self.CAM_CONNECT)
        self.Connect_Button.clicked.connect(self.IP_CONNECT)


    def loadImage(self):

        _, image_bgr = self.cap.read()
        image_bw = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        face_classifier = cv2.CascadeClassifier(self.face_cascade)
        faces = face_classifier.detectMultiScale(image_bw)
        #print(f'There are {len(faces)} faces found.')
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)
        for barcode in decode(image_bgr):
            myData = barcode.data.decode('utf-8')
            cv2.putText(image_bgr,'QR and BAR CODE = '+myData,(10,50), 2, 0.5, (0, 255, 0), 0)

        self.image = image_bgr
        self.setPhoto(self.image)

    def showTime_cam(self):
        self.loadImage()

    def showTime_ip(self):
        self.SENDDATA()
        self.KEYINPUT()
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)
        self.TimeOut.setText(time_string)

    def RUN(self):
        self.TempOut.setText(self.Data[0])
        self.Co2Out.setText(self.Data[1])
        print(self.Data)

    def START_CAM(self):
        self.START_STATUS_CAM = not self.START_STATUS_CAM
        if self.START_STATUS_CAM == True:
            self.timer_cam.start(0)
        else:
            self.timer_cam.stop()

    def CAM_CONNECT(self):
        self.CAM_CONNECT_STATUS = not self.CAM_CONNECT_STATUS
        if self.IP_cam_input.text() == "":
            self.msg.setWindowTitle("App")
            self.msg.setText("Not Connect Webcam Enter IP ro COM PORT")
            x = self.msg.exec_()
        elif self.IP_cam_input.text() != "" and self.CAM_CONNECT_STATUS == False:

            self.Connect_Button_ipcam.setText("Connect")
            self.Connect_Button_ipcam.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.START_CAM()
            self.IP_cam_input.setEnabled(True)

        elif self.IP_cam_input.text() != "" and self.CAM_CONNECT_STATUS == True:
            if len(self.IP_cam_input.text()) <2:
                self.IP_CAM = int(self.IP_cam_input.text())
                self.IP_cam_input.setEnabled(False)
                self.Connect_Button_ipcam.setText("Disconnect")
                self.Connect_Button_ipcam.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.IP_CAM = self.IP_cam_input.text()
                self.IP_cam_input.setEnabled(False)
                self.Connect_Button_ipcam.setText("Disconnect")
                self.Connect_Button_ipcam.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.START_CAM()
        #print(self.IP_CAM)
        self.cap = cv2.VideoCapture(self.IP_CAM)

    def IP_CONNECT(self):
        self.IP_CONNECT_STATUS = not self.IP_CONNECT_STATUS
        if self.IP_input.text() == "" or self.PORT_input.text() == "":
            self.msg.setWindowTitle("App")
            self.msg.setText("Not Connect Please Enter Ip And Port ")
            x = self.msg.exec_()
        elif self.IP_input.text() != "" and self.PORT_input.text() != "" and self.IP_CONNECT_STATUS == True:
            self.Connect_Button.setText("DisConnect")
            self.Connect_Button.setStyleSheet("background-color: rgb(0, 255, 0);")

            self.IP_input.setEnabled(False)
            self.PORT_input.setEnabled(False)
            self.address = (str(self.IP_input.text()),
                            int(self.PORT_input.text()))  # Defind who you are talking to (must match arduino IP and port)
            self.client_socket = socket(AF_INET, SOCK_DGRAM)  # Set Up the Socket
            self.client_socket.settimeout(0.0001)  # only wait 1 second for a resonse
            self.timer_ip.start(0)

            #print("OK")
        else:
            self.Connect_Button.setText("Connect")
            self.Connect_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.IP_input.setEnabled(True)
            self.PORT_input.setEnabled(True)
            self.timer_ip.stop()
            #print("NOT")

    def setPhoto(self, image):
        self.tmp = image
        # resize image
        image = imutils.resize(image, width=1120)
        dsize = (1540, image.shape[0])

        image = cv2.resize(image, dsize, interpolation=cv2.INTER_AREA)

        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.Video_Streaming.setPixmap(QtGui.QPixmap.fromImage(image))

    def SENDDATA(self):
        self.DataSend = self.L1 + self.L2 + self.L3 + self.L4
        #print(self.DataSend)
        data = str.encode(self.DataSend, 'utf-8')  # Set data to Blue Command
        self.client_socket.sendto(data, self.address)  # send command to arduino
        try:
            rec_data, addr = self.client_socket.recvfrom(2048)  # Read response from arduino
            self.DataIN = rec_data.decode('utf-8')
            for i in self.DataIN:
                if i == "\n":
                    self.arr += 1
                    self.number=0
                else:
                    self.number = 1

                if self.number == 1:
                    self.Data[self.arr] += i
                if self.arr > 4:
                    self.arr = 0
            self.RUN()
            self.Data = ["", "", ""]
            #print(self.Data)
            #print(self.arr)


        except:
            pass

    def KEYINPUT(self):
        if kb.is_pressed('w'):
            self.L1 = "N"
            self.W_Button.setEnabled(False)
            self.W_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.L1 = 'F'
            self.W_Button.setEnabled(True)
            self.W_Button.setStyleSheet("background-color: rgb(255, 0, 0);")

        if kb.is_pressed('a'):
            self.L2 = "N"
            self.A_Button.setEnabled(False)
            self.A_Button.setStyleSheet("background-color: rgb(0, 255, 0);")

        else:
            self.L2 = "F"
            self.A_Button.setEnabled(True)
            self.A_Button.setStyleSheet("background-color: rgb(255, 0, 0);")

        if kb.is_pressed('s'):
            self.L3 = "N"
            self.S_Button.setEnabled(False)
            self.S_Button.setStyleSheet("background-color: rgb(0, 255, 0);")

        else:
            self.L3 = "F"
            self.S_Button.setEnabled(True)
            self.S_Button.setStyleSheet("background-color: rgb(255, 0, 0);")

        if kb.is_pressed('d'):
            self.L4 = "N"
            self.D_Button.setEnabled(False)
            self.D_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.L4 = "F"
            self.D_Button.setEnabled(True)
            self.D_Button.setStyleSheet("background-color: rgb(255, 0, 0);")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MYAPP"))
        self.IP_label.setText(_translate("MainWindow", "IP"))
        self.PORT_label.setText(_translate("MainWindow", "PORT"))
        self.IP_input.setText(_translate("MainWindow", "192.168.1.243"))
        self.PORT_input.setText(_translate("MainWindow", "8888"))
        self.W_Button.setText(_translate("MainWindow", "W"))
        self.A_Button.setText(_translate("MainWindow", "A"))
        self.S_Button.setText(_translate("MainWindow", "S"))
        self.D_Button.setText(_translate("MainWindow", "D"))
        self.Connect_Button.setText(_translate("MainWindow", "Connect"))
        self.IP_cam_label.setText(_translate("MainWindow", "IP CAM"))
        self.IP_cam_input.setText(_translate("MainWindow", "0"))
        self.Connect_Button_ipcam.setText(_translate("MainWindow", "Connect"))
        self.Temp_label.setText(_translate("MainWindow", "TEMP"))
        self.DateTime_label.setText(_translate("MainWindow", "Time "))
        self.Co2_label.setText(_translate("MainWindow", "Co2"))
        self.TempOut.setText(_translate("MainWindow", "00"))
        self.Co2Out.setText(_translate("MainWindow", "00"))
        self.TimeOut.setText(_translate("MainWindow", "00:00:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())