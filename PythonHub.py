import os

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



CreatePythonData()
