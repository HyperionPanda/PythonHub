import os
import sys
import importlib
import importlib.util
import shutil

# for importing at runtime

#https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
#https://docs.python.org/3/library/importlib.html#importlib.import_module


#print("Welcome to the PythonHub, where all your python code can be run. In the input below, please include a file you want to be able to be imported and a description Otherwise, use the use section to use some code\n")






#Allow to select a file








fortest = False
pythonDataFile = ""
CLEAN = set()
reloader = set()

#connect all the python files
def Interface():
    global pythonDataFile
    currentline = 0
    print("\nThis is PythonHub, which allows you to import and use all your python files\n")
    print("Please put input if you would like to save new files for import\n")
    print("Please put use if you would like to use any saved files\n")
    print("Please put exit if you would like to quit\n")

    
    
    destination = str(input())
    if destination == "input":
        CreatePythonData()
        AppendPythonData(pythonDataFile)

        newfile = open(pythonDataFile,'r')
    
        for line in newfile:
            print(line+"\n")
            if line.startswith("Name: "):
                    currentline +=1
                

        print("There are currently "+str(currentline)+" files saved")
        newfile.close()

        #go back after creating file
        Interface()
        
    elif destination == "use":
        UsePythonData(pythonDataFile)

        #go back after using files
        Interface()

    
    elif destination == "exit":
        quit
    else:
        Interface()
        

#create the file meant to remember the python files

def CreatePythonData():
    global pythonDataFile
    global fortest
    
    directorypath = os.getcwd()
    
    filepath = os.path.join(str(directorypath), 'PythonFiles.txt')

    #if directory does not exist
    '''
        if not os.path.exists(str(directorypath)):
            os.makedirs('c:/your/full/path')
        f = open(filepath, "a")
    '''
    newfile = open(filepath,'a')
    newfile.close()

    
    

    
    pythonDataFile = filepath
    fortest = True


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
                    newfile.write(description)
                    newfile.write("\n")
                #if exit typed
                else:
                    break
            #if exit typed
            else:
                break
            
        newfile.close()

def UsePythonData(codeName):
    global fortest
    global CLEAN

    cleanup = "__pycache__"


    if fortest == True:
        #might not be necessary
        data = codeName
        
        file = open(data,'r')
        if codeName != "":
            for line in file:

                try:
                    
                    #import sys 
                    #import os
                    #sys.path.append(os.path.abspath("/home/el/foo4/stuff"))
                    #from riaa import *
                    #watchout()
                    

                #line would be "/Users/aidan/Desktop/file.py"
                   
                    '''
                    importline = os.path.dirname(line)

                    modulename = os.path.basename(line)

                    CLEAN.add(importline+"/"+cleanup)
                    
                   
                    sys.path.append(importline)
                    module = importlib.import_module(modulename)
                    '''
                    print("Works1")
                    importline = os.path.dirname(line)
                    modulename = os.path.basename(line)
                    print("Works2")
                    #sys.path.append(importline)
                    spec = importlib.util.spec_from_file_location('GameRandomizer','/Users/aidan/Desktop/GameRandomizer.py')
                    print("Works2.5")
                    print(spec)
                    foo = importlib.util.module_from_spec(spec)
                    print("Works3")
                    sys.modules[modulename] = foo
                    spec.loader.exec_module(foo)
                    foo.GameRandomizer()
                    print(foo)
                    print("Works4")
                    
                except Exception as e:
                    importlib.invalidate_caches()
                    print(e)
                    print("\n"+line+" failure")
                    quit

    #clean up the __pycache__ file
    if CLEAN:
        for paths in CLEAN:
            
            try:
                print("\nBeginning Cleaning\n")
                sys.path.append(os.path.abspath(paths))
                shutil.rmtree(paths)
            except:
                print("For "+paths+" "+cleanup+" does not exist")
            

                
def TESTING():
    path = "/Users/aidan/Desktop/__pycache__"
    try:
        print("\nBeginning Cleaning\n")
        sys.path.append(os.path.abspath(path))
        shutil.rmtree(path)
        print("\Finished Cleaning\n")
    except:
        print("For "+path+" __pycache__ does not exist")
    '''
    line = "/Users/aidan/Desktop/file.py"
    importline = os.path.dirname(os.path.abspath(line))
    print(importline)
    '''
'''
CreatePythonData()
AppendPythonData(pythonDataFile)
#UsePythonData("GameRandomizer.py")
    
UsePythonData(pythonDataFile)

#AppendPythonData(pythonDataFile)

#TESTING()
'''
Interface()
