#описание окна "меню"
import ctypes
import win32gui, win32con
import os
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import *
iconPATH = "C:/Study/Programming/Python/Own works/StepMotorControl/StepMotorControl/source/icon.png"


class Ui_MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.Manual = QtWidgets.QPushButton(self.centralwidget)
        self.Manual.setGeometry(QtCore.QRect(150, 310, 191, 61))
        self.Manual.setObjectName("Manual")

        self.LoadGCode = QtWidgets.QPushButton(self.centralwidget)
        self.LoadGCode.setGeometry(QtCore.QRect(450, 310, 191, 61))
        self.LoadGCode.setObjectName("LoadGCode")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(225, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")

        self.SelectOneText = QtWidgets.QLabel(self.centralwidget)
        self.SelectOneText.setGeometry(QtCore.QRect(265, 190, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SelectOneText.setFont(font)
        self.SelectOneText.setObjectName("SelectOneText")

        self.Version = QtWidgets.QLabel(self.centralwidget)
        self.Version.setGeometry(QtCore.QRect(730, 560, 70, 20))
        self.Version.setObjectName("Version")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.Manual.clicked.connect(self.clickedManual)
        self.LoadGCode.clicked.connect(self.clickedLoad)


    #функция для кнопки Manual
    def clickedManual(self):
        print("Mode set to manual")
        self.manualWindow = QtWidgets.QMainWindow()
        self.manualUi = Ui_MainWindow()
        self.manualUi.setupUi(self.manualWindow)
        self.manualWindow.show()
        self.close()
        

    #функция для кнопки LoadFromFile   
    def clickedLoad(self):
        self.close()
        os.startfile("C:/Study/Programming/Python/Own works/StepMotorControl/StepMotorControl/dist/LoadGCodeFromFile.exe")
        
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Stepper Motor Control"))
        self.Manual.setText(_translate("MainWindow", "Manual control mode"))
        self.LoadGCode.setText(_translate("MainWindow", "Load gcode from file"))
        self.Title.setText(_translate("MainWindow", "Stepper Motor Control"))
        self.SelectOneText.setText(_translate("MainWindow", "Select one of the following"))
        self.Version.setText(_translate("MainWindow", "Version 1.1"))


def menu():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(iconPATH))

    ui = Ui_MenuWindow()
    ui.setupUi()
    ui.show()

    sys.exit(app.exec_())
    

    
