import ctypes
import win32gui, win32con
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import serial
from Menu import menu
import time 


#pyinstaller --onefile LoadGCodeFromFile.py
#pyinstaller --onefile StepMotorControl.py
#конвертировать .py в .exe
if __name__ == "__main__":
    #скрытие консоли
    The_program_to_hide = win32gui.GetForegroundWindow() 
    win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
    menu()
    

