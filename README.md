# diploma_project
Description of stepper motor control software 

That program was designed to control the process of 2D laser ablation/polymerization needed to construct methamaterial with custom spectral characteristics in terahertz diapason.

# Manual
1. Start StepperMotorControl.exe
2. In the menu window there are two options to choose. Manual control and Load Code from file.
3. Case 1: Manual control was chosen. In the second window there are 2 select boxes and 4 buttons to interact. Boxes contains values, which represents a distance (in mm) the motor will drive. Buttons defines direction of movement. As soon as the button Positive/Negative X or Y is pressed, motor drives the selected distance in the selected direction.
4. Case 2: Load from file was chosen. Application evokes console program, which loads Code from file "/sourse/commands.gcode" in the list to be sent to microcontroller. In the console screen list of commands with question "Continue?" is shown. After positive answer ("Y") program sends all the commands to controller. Choosing "N" exits the program. 


# Files description 
The core of program is 4 files:
1. StepperMotorControl.py 
2. Menu.py
3. MainWindow.py
4. LoadGCodeFromFile.py

Brief description:
1. StepperMotorControl.py only contains function menu() from Menu.py to initialize main menu of application.
2. Menu.py contains description of the first window seen by user. Class Menu defines each element of the window and functions evoking by interacting with them. 
3. MainWindow.py contains description of the window seen by user by pressing Manual button in menu window. Class MainWindow defines each element of the window and functions evoking by interacting with them. 
4. LoadGCodeFromFile.py contains functions interacting with file in .gcode extension and communication with microcontroller.  

Information about implementation is to be seen in comments in each file (only in russian for now)
