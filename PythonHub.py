import os
import importlib
# for importing at runtime

#https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
#https://docs.python.org/3/library/importlib.html#importlib.import_module


pythonDataFile = ""

print("Welcome to the PythonHub, where all your python code can be run. In the input below, please include a file you want to be able to be imported and a description Otherwise, use the use section to use some code")



#create the file meant to remember the python files

def CreatePythonData():
    global pythonDataFile
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


CreatePythonData()

# add files to the data file  
def AppendPythonData(pythonDataFile):
    data = pythonDataFile

    if data != "":
        #if file exists, open it
        newfile = open(data,'a')
        print("Type exit to stop")
        while True:
            #what is path of the file (to call from)
            filename = str(input("Name of file meant to save (put whole path): "))
            if filename != "exit":
                newfile.write(filename+"\n")
                #what is description of file (for future uses)
                description = str(input("What is the description of the file? "))
                if description != "exit":
                    newfile.write(description+"\n")
                #if exit typed
                else:
                    break
            #if exit typed
            else:
                break
            
        newfile.close()

def UsePythonData(codeName):
    if codeName != "":
        try:
            module = importlib.import_module(codeName)
            print("fin")
        except:
            print("failure")
            return
    
#CreatePythonData()
#AppendPythonData(pythonDataFile)
UsePythonData("GameRandomizer.py")
#AppendPythonData(pythonDataFile)
