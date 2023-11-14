import Interface as home
import control_File as control

#currentline = 1
command = 1

while command != 0:
    command = home.Interface()
    if command == 2:
        control.view_File()
