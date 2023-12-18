import tkinter as tk
import PythonHub
window = tk.Tk()

window.title("Test Window")

#sets the basic window geometry
window.geometry("300x200")

#Creates a header/label for the window
header = tk.Label(window,text="PythonHub")
header.grid()

#Code from geeksforgeeks.org ====================
# function to display text when
# button is clicked
def clicked():
    header.configure(text="I just got clicked")


# button widget with red color text
# inside
btn = tk.Button(window, text="Click me",fg="red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

#===============================================

#runs the window
window.mainloop()



