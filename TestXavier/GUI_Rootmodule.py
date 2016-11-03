from GUI_Unitmodule import Unit
from tkinter import *




class GUI_Root:
    def __init__(self):
        print("hoi")
        window = Tk()
        window.title("Project: Embedded Systems")

        rootframe = Frame(window, width=1800, height=750)
        rootframe.pack()
        for y in range(0, 5):
            Unit(rootframe)

        window.mainloop()