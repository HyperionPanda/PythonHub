import control_File as control
import PythonHub as hub

print("\nThis is PythonHub, which allows you to import and use all your python files\n")



def Interface():

    python_file = control.create_python_Data()

    print("Please put input if you would like to save new files for import\n")
    print("Please put use if you would like to use any saved files\n")
    print("Please put view if you would like to view what files are saved\n")
    print("Please put exit if you would like to quit\n")

    command = (str(input())).split()
    #command = command.split()

    if command[0] == "input":

        fortest = True
        control.add_to_File(python_file)

        newfile = open(python_file, 'r')
        for line in newfile:
            print( "\n"+line)
            #if line.startswith("Name: "):
                #currentline += 1

        #print("There are currently " + str(currentline) + " files saved")
        newfile.close()

        # go back after creating file
        return 1

    elif command[0] == "use":
        try:
            hub.import_Program(python_file, command[1])
        except:
            print("Error, no file specified\n")
            return 1

        # go back after using files
        return 1

    elif command[0] == "view":
        return 2

    elif command[0] == "exit":
        return 0


