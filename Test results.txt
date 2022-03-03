# Test results 
Manual control mode was tested for each of the distances (1, 10, 100) at several speeds (10, 20, 50, 100, 150, 200, 300). All the commands worked properly with 0.1mm deviation.

Load mode was tested for a file with 2 "blured" commands and 2 empty lines:
--------commands.gcode--------------
 
 
      G1 Z-10 F150 (wrgrgegewrtwert)
G1(erterter)                Z-5 F100
------------------------------------
All blanks and "blure" text were ignored. Commands worked properly with 0.1mm deviation. 


Second test was for a file with .txt extension. 
Program returned extension error.


Third test was for a file wich contained error in GCode:
--------commands.gcode--------------
g1 Z-10 F150 
G1 Z-5 F100
------------------------------------
Program returned syntax error. 


Fourth test was for a file with with 4 "blured" different commands:
--------commands.gcode--------------
(dfsdfg)G1 Z5 F120
G0 (sdsdg) Z10 F20
G0 Z-20(sdfs) F200
G1 Z5 F20(sdsdgsd)
------------------------------------
All "blure" text was ignored. Commands worked properly with 0.1mm deviation. 


Fifth test was for a file with "blur" text not in brackets:
--------commands.gcode--------------
dfsdfggdsd
G0 (sdsdg) Z10 F20
G0 Z-20(sdfs) F200
G1 Z5 F20(sdsdgsd)
------------------------------------
Program returned syntax error. 
