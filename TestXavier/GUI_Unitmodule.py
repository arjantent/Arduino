# Begin of Imports #
from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

plt.matplotlib.use("TkAgg")
# End of Imports #





class Unit:
    def __init__(self, master):         # constructor

        self.frame1 = Frame(master)
        self.frame1.pack(side=LEFT)


        print("test frame")

        # Checkbutton #

        # self.var1 = IntVar()   --- variable=self.var1      (back-up code)
        self.checkbutton = Checkbutton(self.frame1, text="Automatisch", onvalue=1, pady=20, padx=0).grid(row=0, column=0, columnspan=1,  sticky=E)
        print("test checkbutton")

        # Labels #
        self.Extend_Label = Label(self.frame1, text="Uitrol afstand", pady=20, padx=10).grid(row=2, column=0, sticky=E)
        self.Retract_Label = Label(self.frame1, text="Inrol afstand", pady=20, padx=10).grid(row=3, column=0, sticky=E)
        self.Temperture_Label = Label(self.frame1, text="Temperatuur Trigger", pady=20, padx=10).grid(row=5, column=0, sticky=E)
        self.LightIntensity_Label = Label(self.frame1, text="Lichtintensiteit Trigger", pady=20, padx=10).grid(row=6, column=0, sticky=E)

        print("test label")
        # Entry #
        self.Extend_Entry = Entry(self.frame1).grid(row=2, column=1, sticky=W)
        self.Retract_Entry = Entry(self.frame1).grid(row=3, column=1, sticky=W)
        self.Temperture_Entry = Entry(self.frame1).grid(row=5, column=1, sticky=W)
        self.LightIntensity_Entry = Entry(self.frame1).grid(row=6, column=1, sticky=W)
        print("test entry")

        # Buttons #
        self.A = Button(self.frame1, text="Inrollen", padx=10, pady=20).grid(row=7, column=0, sticky=E)   # inrol knop
        self.B = Button(self.frame1, text="Uitrollen", padx=10, pady=20).grid(row=7, column=1, sticky=W)  # uitrol knop
        self.C = Button(self.frame1, text="Submit", padx=10, pady=5).grid(row=4, column=0, sticky=E)      # submit knop
        print("test button")

        # test graph code #
        self.f = plt.Figure(figsize=(4,5), dpi=90)
#Todo : pas de waardes op de assen aan afhankelijk van de data die gelezen wordt
        self.a = self.f.add_subplot(211)
        self.a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 7, 4, 2, 5, 0])
        self.a.set_title('Tempertuur')
        self.a.set_xlabel('Uren')
        self.a.set_ylabel('Celsius')

        self.b = self.f.add_subplot(212)
        self.b.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 6, 1, 0, 2, 1, 0])
        self.b.set_title('Lux')
        self.b.set_xlabel('Uren')
        self.b.set_ylabel('Lichtintensiteit')

        self.f.tight_layout(pad=0.8, w_pad=0.5, h_pad=1.0)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame1)
        self.canvas.get_tk_widget().grid(row=8, column=0, columnspan=2)

        # status bar #
#Todo : zorg dat de status txt wordt geupdate afhankelijk van de status van de lampjes (groen/bewegend/rood)
        self.status = Label(self.frame1, text="status text", bd=2, relief=SUNKEN, pady=15, padx=50).grid(row=9, column=0, columnspan=2)

