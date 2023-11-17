import Interface as home
import control_File as controls


command = 1

while command != 0:
    command = home.Interface()
    if command == 2:
        controls.view_File()
