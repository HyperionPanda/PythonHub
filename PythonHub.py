import os
pythonDataFile = ""
#create the file meant to remember the python files

def CreatePythonData():

    directorypath = os.getcwd()
    
    filepath = os.path.join(str(directorypath), 'PythonFiles.txt')

    #for if directory does not exist
    '''
        if not os.path.exists(str(directorypath)):
            os.makedirs('c:/your/full/path')
        f = open(filepath, "a")
    '''
    newfile = open(filepath,'a')
    

    
    newfile.close()
    pythonDataFile = filepath
    AppendPythonData(pythonDataFile)

    
# add files to the data file  
def AppendPythonData(pythonDataFile):
    data = pythonDataFile

    if data != "":
        newfile = open(data,'a')
        print("Type exit to stop")
        while True:
            
            filename = str(input("Name of file meant to save (put whole path): "))
            if filename != "exit":
                newfile.write(filename+"\n")
                
                description = str(input("What is the description of the file? "))
                if description != "exit":
                    newfile.write(description+"\n")
                else:
                    break
            else:
                break
            
        newfile.close()
            
CreatePythonData()
#AppendPythonData(pythonDataFile)
