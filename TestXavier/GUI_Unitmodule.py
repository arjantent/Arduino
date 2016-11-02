from tkinter import *


class Unit:
    def __init__(self, master, checkbutton):
        self.frame1 = Frame(master)     #Frame voor labels, buttons, entries
        self.frame1.pack()
        print("test frame")

        # Checkbutton #

        self.var1 = IntVar()
        self.checkbutton = checkbutton(self.frame1, text="Automatisch", variable=self.var1, onvalue= 1, offvalue= 0, pady=20).grid(row=0, column=0, sticky=E)
        print("test checkbutton")

        # Labels #

        self.Extend_Label = Label(self.frame1, text="Uitrol afstand", pady=20).grid(row=2, column=0, sticky=E)
        self.Retract_Label = Label(self.frame1, text="Inrol afstand", pady=20).grid(row=3, column=0, sticky=E)
        self.Temperture_Label = Label(self.frame1, text="Temperatuur Trigger", pady=20).grid(row=4, column=0, sticky=E)
        self.LightIntensity_Label = Label(self.frame1, text="Lichtintensiteit Trigger", pady=20).grid(row=5, column=0, sticky=E)
        print("test label")

        # Entry #

        self.Extend_Entry = Entry(self.frame1).grid(row=2, column=1, sticky=E)
        self.Retract_Entry = Entry(self.frame1).grid(row=3, column=1, sticky=E)
        self.Temperture_Entry = Entry(self.frame1).grid(row=4, column=1, sticky=E)
        self.LightIntensity_Entry = Entry(self.frame1).grid(row=5, column=1, sticky=E)
        print("test entry")
        # Buttons

        self.A = Button(self.frame1, text ="Inrollen", padx=10, pady=20).grid(row=6, column=0)
        self.B = Button(self.frame1, text ="Uitrollen", padx=10, pady=20).grid(row=6, column=1)
        print("test button")