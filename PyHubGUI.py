import tkinter as tk
import PythonHub

window = tk.Tk()

window.title("PythonHub")

#Creates a header/label for the window
header = tk.Label(window,text="Python Files")
header.grid()


length = 1280
height = 460
#print(str(length)+"x"+str(height))
window.geometry(str(length)+"x"+str(height))


#Code from geeksforgeeks.org ====================
# function to display text when
# button is clicked
def clicked():
    header.configure(text="I just got clicked")


# button widget with red color text
# inside
def fillGUI(python_file):
    grid_column = 1
    grid_row = 1
    #change later based on size of row
    grid_max_row = 3
    line_count = 1
    for file in python_file:
        #is the current line a file or a description? if file, continue and add as button
        if line_count %2 !=0:
            btn = tk.Button(window, text=file,fg="red", command=clicked)
            btn.grid(column=grid_column, row=grid_row)
            grid_row +=1
        if grid_row > 3:
            grid_column +=1
            grid_row = 1
        line_count +=1
    window.mainloop()
#===============================================
#runs the window
#window.mainloop()