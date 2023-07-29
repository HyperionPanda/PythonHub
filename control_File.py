import os

#create the file meant to remember the python files
def create_python_Data():
    pythonDataFile = ""
    fortest = False

    directory_path = os.getcwd()

    filepath = os.path.join(str(directory_path), 'PythonFiles.txt')

    # if directory does not exist
    '''
        if not os.path.exists(str(directorypath)):
            os.makedirs('c:/your/full/path')
        f = open(filepath, "a")
    '''
    newfile = open(filepath, 'a')
    newfile.close()

    pythonDataFile = filepath
    fortest = True
    return filepath


# add files to the data file
def add_to_File (existing_file):
    data = existing_file

    if data != "":
        # if file exists, open it
        append_file = open(data, 'a')
        print("Type exit to stop")
        while True:
            # what is path of the file (to call from)
            filename = str(input("Name of file meant to save (put whole path): "))
            if filename != "exit":
                append_file.write(filename + "\n")

                # what is description of file (for future uses)
                description = str(input("What is the description of the file? "))
                if description != "exit":
                    append_file.write(description)
                    append_file.write("\n")
                # if exit typed
                else:
                    break
            # if exit typed
            else:
                break
        append_file.close()

