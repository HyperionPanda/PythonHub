import Interface as home
import control_File as controls
import HomePage as home

#command should be 1 unless testing GUI, then 10
#command = 1
command = 10

home

while command != 0 and command != 10:
    command = home.Interface()
    if command == 2:
        controls.view_File()

#with open('PythonFiles.txt') as file:
    #gui.fillGUI(file)