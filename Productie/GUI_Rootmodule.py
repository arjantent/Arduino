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


        try:
            Unit(rootframe, 'COM3' )

        except: print("Com3 is niet aangesloten")

        try:
            Unit(rootframe, 'COM4' )
        except:
            print("Com4 is niet aangesloten")

        try:
            Unit(rootframe, 'COM5' )
        except:
            print("Com5 is niet aangesloten")

        try:
            Unit(rootframe, 'COM6' )
        except:
            print("Com6 is niet aangesloten")

        try:
            Unit(rootframe, 'COM7' )
        except:
            print("Com7 is niet aangesloten")

        try:
            Unit(rootframe, 'COM8' )
        except:
            print("Com8 is niet aangesloten")

        window.mainloop()