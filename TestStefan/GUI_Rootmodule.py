# Begin of Imports #
from GUI_Unitmodule import Unit
from tkinter import *
# End of Imports #




class GUI_Root:
    def __init__(self):
        print("hoi")
        window = Tk()
        print("test1")
        window.title("Project: Embedded Systems")
        print("test2")
        rootframe = Frame(window, width=1800, height=750)
        rootframe.pack()

        Unit(rootframe, 'COM3' )
        try:
            Unit(rootframe, 'COM4' )
        except:
            print("LUKT NIET PIK")
        window.mainloop()