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

python_file = ""
CLEAN = set()
reloader = set()

#connect all the python files

def import_Program(old_file,codeName):

    cleanup = "__pycache__"

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
            

