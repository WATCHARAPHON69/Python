from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import time
import numpy as np
import cv2
import pyshine as ps


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/H.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_2.clicked.connect(self.loadImage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Added code here
        self.filename = 'Snapshot ' + str(
            time.strftime("%Y-%b-%d at %H.%M.%S %p")) + '.png'  # Will hold the image address location

        self.started = False

    def loadImage(self):

        if self.started:
            self.started = False
            self.pushButton_2.setText('Start')
        else:
            self.started = True
            self.pushButton_2.setText('Stop')

        vid = cv2.VideoCapture(1)

        while (vid.isOpened()):

            img, self.image = vid.read()
            self.image = imutils.resize(self.image, height=480)

            self.update()
            key = cv2.waitKey(1) & 0xFF


    def setPhoto(self, image):
        self.tmp = image
        image = imutils.resize(image, width=500)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))


    def update(self):
        img = self.image

        text = str(time.strftime("%H:%M %p"))
        img = ps.putBText(img, text, text_offset_x=self.image.shape[1] - 180, text_offset_y=30, vspace=20, hspace=10,
                          font_scale=1.0, background_RGB=(228, 20, 222), text_RGB=(255, 255, 255))
        self.setPhoto(img)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyShine video process"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


