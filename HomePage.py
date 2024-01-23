import tkinter as tk
import PyHubGUI as gui
import Interface as hub
#from tkinter import ttk

window = tk.Tk()
#window.attributes("-fullscreen", True)
window.title("PythonHub")

length = 1280
height = 420
#print(str(length)+"x"+str(height))
window.geometry(str(length)+"x"+str(height))

#Creates a header/label for the window
header = tk.Label(window,text="Homepage")
header.pack(side = "top")

intro_text = tk.Text(window,height = 5)
intro_text.pack(side = "top")
intro_text.insert(tk.END,"This is PythonHub, which allows you to import and use all your python files")

enterScreen = tk.Frame(window)
enterScreen.pack(side = "left",padx = 50,expand = True)

exitScreen = tk.Frame(window)
exitScreen.pack(side = "right",padx = 50, expand = True)

def enterHub():
    Object = gui.Main()
    Object.run()
    window.destroy()


def exitHub():
    window.destroy()

enter = tk.Button(enterScreen, text="Enter",fg="green", command=enterHub, height = 10, width = 50)
enter.grid(column = 5, row=10)
exit = tk.Button(exitScreen, text="Exit",fg="red", command=exitHub, height = 10, width = 50)
exit.grid(column= 5, row=10)
#Code from geeksforgeeks.org ====================
# function to display text when
# button is clicked
def clicked():
    header.configure(text="I just got clicked")

#===============================================
#runs the window
window.mainloop()

#hub.Interface()