#программа исполняет команды из файла с адресом PATH
import serial
from serial.tools import list_ports
import time 
import sys
PATH = "C:/Study/Programming/Python/Own works/StepMotorControl/StepMotorControl/source/commands.gcode"


#проверка расширения файла
def checkFile(PATH):
    fileExtension = ""
    for i in range(len(PATH)):
        if PATH[i] == '.':
            break
    for j in range(i + 1, len(PATH)):
        fileExtension += PATH[j]

    if fileExtension == "gcode":
        return 1
    return 0


#подготовка записи из файла для сохранения в очередь команд
def prepareLine(line):
    newline = ""
    for i in range(len(line)):
        if line[i] == '(':
            break
        newline += line[i]
     
    for j in range(i, len(line)):
        if line[j] == ')':
            break

    for i in range(j + 1, len(line)):
        newline += line[i]

    newline = newline.strip()
    return newline


#формирование очереди команд
def getCommandQueueFromFile():
    if not checkFile(PATH):
        print("Not a gcode file")
        exit() 
    commandQueue = []
    file = open(PATH, 'r')
    for line in file:
        newline = prepareLine(line)
        commandQueue.append(newline)
    file.close()

    if len(commandQueue) > 0:
        commandQueue = [x for x in commandQueue if x]
        for i in range(len(commandQueue)):
            if not commandQueue[i].isupper():
                print("Gcode file may contain mistakes, verify it and start application again")
                exit()
            commandQueue[i] += "\r\n"
            commandQueue[i] = commandQueue[i].encode()
        return commandQueue
    print("File doesn't has valid gcode commands")
    exit() 


def delay(timeout = 0.1):
    ts = time.process_time()
    while 1:
            if time.process_time() - ts > timeout:
                break
            

#отправка команд из очереди микроконтроллеру
def sendCommands(serialPort, commandQueue):
    if serial.tools.list_ports.comports() != []: 
        for i in range(len(commandQueue)):
            serialPort.write(commandQueue[i])
            waitingAnswer(serialPort)

                
#ожидание ответа от контроллера
def waitingAnswer(serialPort, timeout = 0.1):
        ts = time.process_time() 
        while 1:
            if time.process_time() - ts > timeout:
                break
            if serialPort.in_waiting > 0:
                serialString = serialPort.readline()
                

#инициализация порта
def init(mode = "relative"):
    serialPort = serial.Serial('COM5', 250000)
    delay(1)
    if mode == "relative":
        serialPort.write(str.encode("G91\r\n"))
        waitingAnswer(serialPort)

    return serialPort


#сравнение ответа пользоваеля
def checkAnswer(answer):
    if answer == 'Y':
        return 1
    if answer == 'N':
        exit()
    else:
        print("Invalid option")


if __name__ == "__main__":
    commandQueue = getCommandQueueFromFile()
    print("Mode set to load\n")
    print("Current command queue:\n")
    for i in range(len(commandQueue)):
        print(i, commandQueue[i], '\n')
    serialPort = init()
    print("Continue? Y/N")

    while 1:
        answer = str(input())
        answer = answer.upper()
        if checkAnswer(answer) == 1:
            sendCommands(serialPort, commandQueue)

    serialPort.close()

