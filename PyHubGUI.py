import tkinter as tk
import PythonHub
print(1)

class Main:
    def __init__(self):

        self.window = tk.Tk()
        self.length = 1280
        self.height = 460

        self.headerScreen = tk.Frame(self.window)
        self.headerScreen.pack(side="top")
        self.buttonScreen = tk.Frame(self.window)
        self.buttonScreen.pack()

        self.header = tk.Label(self.headerScreen, text="Python Files")
        self.header.pack(side="top")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
    def run(self):
        self.window.title("PythonHub")


        #print(str(length)+"x"+str(height))
        self.window.geometry(str(self.length)+"x"+str(self.height))

        with open('PythonFiles.txt') as file:
            self.fillGUI(file)
        self.window.mainloop()
    def clicked(self):
        self.header.configure("Testing 1")

    def fillGUI(self,python_file):
            grid_column = 1
            grid_row = 1
            #change later based on size of row
            grid_max_row = 3
            line_count = 1

            for file in python_file:
                #is the current line a file or a description? if file, continue and add as button
                if line_count %2 !=0:

                    btn = tk.Button(self.buttonScreen, text=file,fg="red", command=self.clicked)
                    btn.grid(column=grid_column, row=grid_row, padx = 25, pady = 10)
                    print(btn.size)

                    grid_row +=1
                #changing number next to row determines number of file buttons allowed in each column
                if grid_row > 8 and grid_column < 6:
                    grid_column +=1
                    grid_row = 1
                line_count +=1
        #===============================================
        #runs the window
        #window.mainloop()