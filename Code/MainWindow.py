#описание окна "Manual"
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
from serial.tools import list_ports
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.initPort()

        #объявление элементов окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.CommandList = QtWidgets.QPushButton(self.centralwidget)
        self.CommandList.setGeometry(QtCore.QRect(315, 500, 150, 50))
        self.CommandList.setObjectName("CommandList")
        self.CommandList.setText("Command list")

        self.PositiveY = QtWidgets.QPushButton(self.centralwidget)
        self.PositiveY.setGeometry(QtCore.QRect(415, 290, 150, 50))
        self.PositiveY.setObjectName("PositiveY")

        self.NegativeY = QtWidgets.QPushButton(self.centralwidget)
        self.NegativeY.setGeometry(QtCore.QRect(415, 355, 150, 50))
        self.NegativeY.setObjectName("NegativeY")

        self.NegativeX = QtWidgets.QPushButton(self.centralwidget)
        self.NegativeX.setGeometry(QtCore.QRect(215, 355, 150, 50))
        self.NegativeX.setObjectName("NegativeX")

        self.PositiveX = QtWidgets.QPushButton(self.centralwidget)
        self.PositiveX.setGeometry(QtCore.QRect(215, 290, 150, 50))
        self.PositiveX.setObjectName("PositiveX")

        self.StepX = QtWidgets.QPushButton(self.centralwidget)
        self.StepX.setGeometry(QtCore.QRect(240, 200, 100, 30))
        self.StepX.setObjectName("StepX")

        self.StepY = QtWidgets.QPushButton(self.centralwidget)
        self.StepY.setGeometry(QtCore.QRect(440, 200, 100, 30))
        self.StepY.setObjectName("StepY")

        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(720, 520, 80, 20))
        self.version.setObjectName("version")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(240, 0, 321, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.instruction = QtWidgets.QLabel(self.centralwidget)
        self.instruction.setGeometry(QtCore.QRect(272, 170, 255, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instruction.setFont(font)
        self.instruction.setObjectName("instruction")

        self.comboX = QtWidgets.QComboBox(self.centralwidget)
        self.comboX.setGeometry(QtCore.QRect(252, 250, 75, 22))
        self.comboX.setObjectName("comboX")
        self.comboX.addItem("")
        self.comboX.addItem("")
        self.comboX.addItem("")

        self.comboY = QtWidgets.QComboBox(self.centralwidget)
        self.comboY.setGeometry(QtCore.QRect(453, 250, 75, 22))
        self.comboY.setObjectName("comboY")
        self.comboY.addItem("")
        self.comboY.addItem("")
        self.comboY.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        self.menuSelect_COM_port = QtWidgets.QMenu(self.menubar)
        self.menuSelect_COM_port.setGeometry(QtCore.QRect(270, 153, 171, 78))
        self.menuSelect_COM_port.setObjectName("menuSelect_COM_port")

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSelect_COM_port = QtWidgets.QAction(MainWindow)
        self.actionSelect_COM_port.setObjectName("actionSelect_COM_port")

        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.menuSelect_COM_port.addAction(self.actionSelect_COM_port)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuSelect_COM_port.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #функции, вызывающиеся по нажатию на элементы меню
        self.actionHelp.triggered.connect(self.clickedHelp)

        #функции, вызывающиеся по нажатию кнопок
        self.StepX.clicked.connect(lambda: self.updateInstructionLine("Select step for X in the list below"))
        self.StepY.clicked.connect(lambda: self.updateInstructionLine("Select step for Y in the list below"))

        self.CommandList.clicked.connect(self.getCommandQueue)

        self.PositiveX.clicked.connect(self.clickedPositiveX)
        self.NegativeX.clicked.connect(self.clickedNegativeX)
        self.PositiveY.clicked.connect(self.clickedPositiveY)
        self.NegativeY.clicked.connect(self.clickedNegativeY)

        #внутрение переменные
        self.command = "" #посылка передаваемая через порт
        self.commandCode = 0 #код посылки 
        self.counter = 0 #счетчик комманд
        self.commandQueue = [] #список комманд
        self.step = 0


    #возвращение списка команд
    def getCommandQueue(self):
        if len(self.commandQueue) > 0:
            print(self.commandQueue)
            self.updateInstructionLine("Commands are shown in console")
            return 1
        self.updateInstructionLine("There were no commands yet")
        return 0


    #обновление надписи в поле инструкций
    def updateInstructionLine(self, text):
        self.instruction.setText(text)
        self.instruction.adjustSize()


    #функция для меню help
    def clickedHelp(self):
        print("Help was clicked")


    #функции для кнопок перемещения
    def clickedPositiveX(self):
        self.step = self.comboX.currentText()
        direction = "Z"
        self.command = "G1 " + direction + str(self.step) + " F200\r\n"
        self.sendCommand()

    def clickedNegativeX(self):
        self.step = self.comboX.currentText()
        direction = "Z-"
        self.command = "G1 " + direction + str(self.step) + " F200\r\n"
        self.sendCommand()

    def clickedPositiveY(self):
        self.step = self.comboY.currentText()
        direction = "Y"
        self.command = "G0 " + direction + str(self.step) + " F150\r\n"
        self.sendCommand()

    def clickedNegativeY(self):
        step = self.comboY.currentText()
        direction = "Y-"
        self.command = "G0 " + direction + str(self.step) + " F150\r\n"
        self.sendCommand()


    #инициализация порта (здесь же установка в режим относительного перемещения)
    def initPort(self, mode = "relative"):
        self.serialPort = serial.Serial('COM5', 250000) #открытие порта COM5, с битрейтом 250000
        self.delay(1)
        if mode == "relative":
            self.serialPort.write(str.encode("G91\r\n"))
            self.waitingAnswer(self.serialPort)


    #функция, ожидающая ответа от контроллера
    def waitingAnswer(self, serialPort, timeout = 0.1):
        ts = time.process_time() 
        while 1:
            if time.process_time() - ts > timeout:
                break
            if serialPort.in_waiting > 0:
                serialString = serialPort.readline()
                print(serialString.decode("UTF-8"))


    def delay(self, timeout = 0.2):
        ts = time.process_time() 
        while 1:
            if time.process_time() - ts > timeout:
                break


    #функция, отправляющая посылку контроллеру
    def sendCommand(self, cmd = "", init = 0):
        if len(cmd) > 0:
            self.command = cmd
        if serial.tools.list_ports.comports() != []: #если есть открытые порты
                self.serialPort.write(str.encode(self.command)) #отправка посылки через порт
                self.waitingAnswer(self.serialPort) 
                if not init: #выполняется только для инициализации, чтобы G91 не вносить в список команд
                    self.commandQueue.append(str(self.counter) + ' ' + str(self.command)) #сохраняем команду в список
                    self.counter += 1
                    self.updateInstructionLine("Command was succesfully sent")
        else:
            self.updateInstructionLine("COM ports are not available!")


    #обозначения элементов окна
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stepper Motor Control Manual Mode"))
        self.PositiveY.setText(_translate("MainWindow", "Positive Y"))
        self.NegativeY.setText(_translate("MainWindow", "Negative Y"))
        self.NegativeX.setText(_translate("MainWindow", "Negative X"))
        self.PositiveX.setText(_translate("MainWindow", "Positive X"))
        self.StepX.setText(_translate("MainWindow", "Step X"))
        self.StepY.setText(_translate("MainWindow", "Step Y"))
        self.version.setText(_translate("MainWindow", "Version 1.1"))
        self.title.setText(_translate("MainWindow", "Stepper Motor Control"))
        self.instruction.setText(_translate("MainWindow", "Press buttons to control the motor"))
        self.comboX.setItemText(0, _translate("MainWindow", "1"))
        self.comboX.setItemText(1, _translate("MainWindow", "10"))
        self.comboX.setItemText(2, _translate("MainWindow", "100"))
        self.comboY.setItemText(0, _translate("MainWindow", "1"))
        self.comboY.setItemText(1, _translate("MainWindow", "10"))
        self.comboY.setItemText(2, _translate("MainWindow", "100"))
        self.menuSelect_COM_port.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSelect_COM_port.setText(_translate("MainWindow", "Select COM port"))
        self.actionSelect_COM_port.setStatusTip(_translate("MainWindow", "Select available COM port"))
        self.actionSelect_COM_port.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))


def manualMode():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uiMain = Ui_MainWindow()
    uiMain.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
