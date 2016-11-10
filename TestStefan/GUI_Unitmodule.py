# Begin of Imports #
from tkinter import *
from drawnow import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import serial
import time
plt.matplotlib.use("TkAgg")
# End of Imports #

# todo: implementeer code van stefan voor inlezen temp en lux waardes -> temp_val & lux_val

class Unit:
    def __init__(self, master, port, baudrate=9600):         # constructor

        self.frame1 = Frame(master)
        self.frame1.pack(side=LEFT, fill=BOTH, expand=1)
        self.port = serial.Serial(port=port, baudrate=baudrate)

        self.rollin_bool = True
        self.automatic_bool = False
        self.master = master
        self.uitrollen=int(0)
        #self.uitrollen.set(0)
        self.inrollen=int(0)
        #self.inrollen.set(0)

        self.temperatuur=int(0)      # standaard temperatuur waarde
        #self.temperatuur.set(25)
        self.lichtint=int(0)         # standaard lux waarde
        #self.lichtint.set(800)




        self.var = StringVar()
        self.var.set('Ingerold')

        self.lux_list = []
        self.temp_list = []

        self.plt = plt.ion()
        self.cnt = 0


        for i in range(0, 30):
            self.lux_list.append(0)

        for a in range(0, 30):
            self.temp_list.append(0)

        # Begin Uit- en Inrolafstanden input #
        def uitrolafstand():
            try:
                self.uitrolwaarde = int(self.uitrollen)
                print(self.uitrolwaarde)
                return
            except ValueError:
                print("Ongeldige waarde.")

        def inrolafstand():
            try:
                self.inrolwaarde = int(self.inrollen)
                print(self.inrolwaarde)
                return self.inrolwaarde
            except ValueError:
                print("Ongeldige waarde.")

        def submitten():
            uitrolafstand()
            inrolafstand()
            # einde afstand submit

            # begin temp/ lux submit
        def temperatuur():
            try:
                self.temperatuurwaarde = int(self.temperatuur)
                print(self.temperatuurwaarde)
                return
            except ValueError:
                print("Ongeldige waarde.")

        def lichtint():
            try:
                self.lichtwaarde = int(self.lichtint)
                print(self.lichtwaarde)
                return
            except ValueError:
                print("Ongeldige waarde.")

        def submitten2():
            temperatuur()
            lichtint()
        # Einde Uit- en Inrolafstanden input #

        # Checkbutton #
        self.checkbutton = Checkbutton(self.frame1, text="Automatisch", onvalue=1, pady=20, padx=0, command=self.set_automatic_bool).grid(row=0, column=0, columnspan=1,  sticky=E)
        print("test checkbutton")

        # Labels #

        print("test label")
        # Entry #
        print("test label")
        self.Extend_Label = Label(self.frame1, text="Temperatuur regelaar: ", pady=20, padx=10).grid(row=1, column=0, sticky=E)
        self.temp_plus5 = Button(self.frame1, text="Plus 5", padx=10, pady=20, command=self.postemp5).grid(row=1, column=2,sticky=N)
        self.temp_plus1 = Button(self.frame1, text="Plus 1", padx=10, pady=20, command=self.postemp1).grid(row=1, column=3,sticky=W)
        self.temp_min5 = Button(self.frame1, text="Min 5", padx=10, pady=20, command=self.negtemp5).grid(row=1, column=4,sticky=W)
        self.temp_min1 = Button(self.frame1, text="Min 1", padx=10, pady=20, command=self.negtemp1).grid(row=1, column=5, sticky=W)
        self.Extend_Label = Label(self.frame1, text="Uitrol temperatuur: 10" , pady=20, padx=10).grid(row=2, column=1,sticky=E)

        self.Extend_Label = Label(self.frame1, text="Licht regelaar", pady=20, padx=10).grid(row=3, column=0, sticky=E)
        self.neger = Button(self.frame1, text="Neger", padx=10, pady=20, command=self.setneger).grid(row=3, column=2,sticky=W)
        self.bruin = Button(self.frame1, text="Bruin ", padx=10, pady=20, command=self.setbruin).grid(row=3, column=3,sticky=W)
        self.blank = Button(self.frame1, text="Blank", padx=10, pady=20, command=self.setblank).grid(row=3, column=4,sticky=W)
        self.ginger = Button(self.frame1, text="Ginger", padx=10, pady=20, command=self.setginger).grid(row=3, column=5,sticky=W)
        self.Extend_Label = Label(self.frame1, text="Uitrol Lux: 800", pady=20, padx=10).grid(row=4, column=1, sticky=E)

        self.Extend_Label = Label(self.frame1, text="Afstand regelaar", pady=20, padx=10).grid(row=5, column=0, sticky=E)
        self.neger = Button(self.frame1, text="Omlaag", padx=10, pady=20, command=self.rolluit).grid(row=5, column=1,sticky=E)
        self.bruin = Button(self.frame1, text="Omhoog", padx=10, pady=20, command=self.rolluit).grid(row=5, column=2,sticky=W)
        self.blank = Button(self.frame1, text="10CM Omlaag", padx=10, pady=20, command=self.rolluit).grid(row=5, column=3, sticky=E)
        self.ginger = Button(self.frame1, text="10CM Omhoog", padx=10, pady=20, command=self.rolluit).grid(row=5, column=4, sticky=W)

        # test graph code #
        self.updategraph()

        #while True:
    def updategraph(self):

        self.write("V")
        self.data = self.port.readline().decode('utf-8')  # maakt connectie met arduino

        self.lux_read, self.temp_read = [int(x.encode()) for x in self.data.split(",")]

        self.lux_val = int(self.lux_read)
        self.temp_val = int(self.temp_read)
        print("lux %d" % self.lux_val)
        print("temp %d" % self.temp_val)

        self.lux_list.append(self.lux_val)
        self.lux_list.pop(0)
        self.temp_list.append(self.temp_val)
        self.temp_list.pop(0)
        drawnow(self.plotValues)
        if self.automatic_bool == True:
            print(self.temperatuur, self.lichtint, self.lux_val, self.temp_val)
            if self.lux_val >= self.lichtint and self.temp_val >= self.temperatuur:
                self.rolluit_auto()
            elif self.lux_val < self.lichtint and self.temp_val < self.temperatuur:
                self.rollin_auto()
        self.master.after(20000, self.updategraph)





    def plotValues(self):
        self.f = plt.Figure(figsize=(4, 5), dpi=90)
        self.a = self.f.add_subplot(211)
        self.a.plot(self.temp_list, 'bx-', label='TEMP')
        self.a.set_title('Tempertuur')
        self.a.set_xlabel('Uren')
        self.a.set_ylabel('Celsius')
        self.a.grid(True)


        self.b = self.f.add_subplot(212)
        self.b.plot(self.lux_list, 'rx-', label='LUX')
        self.b.set_title('Lux')
        self.b.set_xlabel('Uren')
        self.b.set_ylabel('Lichtintensiteit')
        self.b.grid(True)

        self.f.tight_layout(pad=0.8, w_pad=0.5, h_pad=1.0)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame1, )
        self.canvas.get_tk_widget().grid(row=9, column=0, columnspan=2)


        # status bar #
        self.getal = self.lux_val
        self.var2 = (str(self.getal))
        self.tp = StringVar()
        self.tp.set(self.var2)

        self.getal2 = self.temp_val
        self.var3 = (str(self.temp_val))
        self.lx = StringVar()
        self.lx.set(self.var3)

        # status bar #
        self.status = Label(self.frame1, textvariable=self.var, bd=2, width=8, relief=SUNKEN, pady=15, padx=50).grid(
            row=10, column=0, columnspan=1)
        self.status_lux = Label(self.frame1, textvariable=self.tp, bd=2, width=8, relief=SUNKEN, pady=15, padx=50).grid(
            row=10, column=1, columnspan=1)
        self.status_temp = Label(self.frame1, textvariable=self.lx, bd=2, width=8, relief=SUNKEN, pady=15,
                                 padx=50).grid(row=11, column=0, columnspan=1)

    def open(self):
        ''' Open the serial port.'''
        self.port.open()

    def close(self):
        ''' Close the serial port.'''
        self.port.close()

    def afstand(self):
        self.write("X")
        distance = int(self.port.readline().decode('utf-8'))
        print (distance)


    def write(self, msg):
        time.sleep(2)
        self.port.write(msg.encode())

    def readline(self):
        self.port.readline()

    def readlines(self):
        self.port.readlines()

    def onGroen(self):
        self.write("H")

    def offGroen(self):
        self.write("L")

    def offRood(self):
        self.write("U")

    def onRood(self):
        self.write("A")

    def onGeel(self):
        self.write("N")

    def offGeel(self):
        self.write("M")

    def blink(self):
        for i in range(5):
            self.onGeel()
            self.offGeel()

    # uitrollen
    def rolluit(self):
        if self.automatic_bool == False:
            if self.rollin_bool == True:
                self.offRood()
                self.onGroen()
                self.blink()
                self.offGroen()
                self.onRood()
                self.var.set('Uitgerold')
                self.rollin_bool = False

    # inrollen
    def rollin(self):
        if self.automatic_bool == False:
            if self.rollin_bool == False:
                self.offGroen()
                self.onRood()
                self.blink()
                self.offRood()
                self.onGroen()
                self.var.set('Ingerold')
                self.rollin_bool = True

    def rolluit_auto(self):
        if self.rollin_bool == True:
            self.offRood()
            self.onGroen()
            self.blink()
            self.offGroen()
            self.onRood()
            self.var.set('Uitgerold')
            self.rollin_bool = False

    # inrollen
    def rollin_auto(self):
        if self.rollin_bool == False:
            self.offGroen()
            self.onRood()
            self.blink()
            self.offRood()
            self.onGroen()
            self.var.set('Ingerold')
            self.rollin_bool = True

    # Automatic / Manual switch
    def set_automatic_bool(self):
        self.write("0")
        self.automatic_bool = not self.automatic_bool
        return self.set_automatic_bool

    # check lux waarde #
    def check_lux(self):
        if self.lux_val >= self.lichtint:
            print("true")
            self.rolluit()

    # check temp waarde #
    def check_temp(self):
        if self.temp_val >= self.temperatuur:
            print("ook true")
            self.rolluit()


    def postemp1(self):
        self.write("1")

    def postemp5(self):
        self.write("2")

    def negtemp1(self):
        self.write("3")

    def negtemp5(self):
        self.write("4")

    def setneger(self):
        self.write("5")

    def setbruin(self):
        self.write("6")

    def setblank(self):
        self.write("7")

    def setginger(self):
        self.write("8")