import os
import sys
import importlib
import importlib.util
import shutil

# for importing at runtime

#https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string
#https://docs.python.org/3/library/importlib.html#importlib.import_module

#connect all the python files

def import_Program(old_file,selected_Module):
    python_file = ""
    CLEAN = set()
    cleanup = "__pycache__"

    file = open(old_file,'r')
    if file != "":
        for line in file:
            module = os.path.basename(line)

            module = "".join(module.split())
            if module == selected_Module:

                try:


                    #line would be "/Users/aidan/Desktop/file.py"

                    #put together the path and add to the clean set so that the file is cleaned of __pycache__

                    import_path = os.path.dirname(line)
                    #module.py
                    module_name = str(os.path.basename(line))
                    full_path = str(import_path+'/'+module_name)
                    CLEAN.add(import_path + "/" + cleanup)

                    #name should be file name without .py, location should be full path with the selected file.py at the end
                    spec = importlib.util.spec_from_file_location(module_name, full_path.strip())
                    foo = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = foo
                    spec.loader.exec_module(foo)


                except Exception as e:
                    importlib.invalidate_caches()
                    print(e)
                    print("\n"+line+" failure")

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
            

