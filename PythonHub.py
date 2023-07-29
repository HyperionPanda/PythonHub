import os
import sys
import importlib
import importlib.util
import shutil
import control_File

# for importing at runtime

#https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
#https://docs.python.org/3/library/importlib.html#importlib.import_module


#print("Welcome to the PythonHub, where all your python code can be run. In the input below, please include a file you want to be able to be imported and a description Otherwise, use the use section to use some code\n")


#Allow to select a file


fortest = False
python_file = ""
CLEAN = set()
reloader = set()

#connect all the python files
def Interface():
    global python_file
    global fortest
    currentline = 1
    print("\nThis is PythonHub, which allows you to import and use all your python files\n")
    print("Please put input if you would like to save new files for import\n")
    print("Please put use if you would like to use any saved files\n")
    print("Please put exit if you would like to quit\n")

    
    
    destination = str(input())
    destination = destination.split()

    if destination[0] == "input":
        python_file = control_File.create_python_Data()
        fortest = True
        control_File.add_to_File(python_file)

        newfile = open(python_file,'r')
        for line in newfile:
            print(line+"\n")
            if line.startswith("Name: "):
                    currentline +=1
                

        print("There are currently "+str(currentline)+" files saved")
        newfile.close()

        #go back after creating file
        Interface()

    elif destination[0] == "use":
        if destination[1] != "":
            import_Program(python_file, destination[1])
        else:
            print("Error, no file specified")

        #go back after using files
        Interface()

    
    elif destination[0] == "exit":
        quit
    else:
        Interface()


def import_Program(old_file,codeName):
    global fortest
    global CLEAN

    cleanup = "__pycache__"


    if fortest == True:
        #might not be necessary
        data = old_file
        
        file = open(data,'r')
        if file != "":
            for line in file:
                module = os.path.basename(line)

                module = "".join(module.split())
                if module == codeName:

                    try:


                        #line would be "/Users/aidan/Desktop/file.py"


                        importline = os.path.dirname(line)
                        modulename = os.path.basename(line)
                        CLEAN.add(importline + "/" + cleanup)
                        #sys.path.append(importline)
                        spec = importlib.util.spec_from_file_location('GameRandomizer','/Users/aidan/Desktop/GameRandomizer.py')
                        #print(spec)
                        foo = importlib.util.module_from_spec(spec)
                        sys.modules[modulename] = foo
                        spec.loader.exec_module(foo)
                        #foo.GameRandomizer()
                        #print(foo)


                    except Exception as e:
                        importlib.invalidate_caches()
                        print(e)
                        print("\n"+line+" failure")
                        quit
                else:
                    print("No")

    #clean up the __pycache__ file
    if CLEAN:
        for paths in CLEAN:
            
            try:
                print("\nBeginning Cleaning\n")
                sys.path.append(os.path.abspath(paths))
                shutil.rmtree(paths)
                print("\nFinished Cleaning\n")
            except:
                print("For "+paths+" "+cleanup+" does not exist")
            

Interface()
