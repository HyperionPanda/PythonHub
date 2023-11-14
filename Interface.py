import control_File as control
import PythonHub as hub

print("\nThis is PythonHub, which allows you to import and use all your python files\n")



def Interface():

    python_file = control.create_python_Data()

    print("Please put input if you would like to save new files for import\n")
    print("Please put use if you would like to use any saved files\n")
    print("Please put exit if you would like to quit\n")

    command = str(input())
    command = command.split()

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

        if command[1] != "":

            hub.import_Program(python_file, command[1])

        else:
            print("Error, no file specified")
            return 1

        # go back after using files
        return 1

    elif command[0] == "exit":
        return 0
        #quit

