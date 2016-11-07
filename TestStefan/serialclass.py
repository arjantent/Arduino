import serial
import time

class Serializer:
    last_received = ''


    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = serial.Serial(port = port, baudrate=baudrate,
                                  timeout=timeout)

    def open(self):
        ''' Open the serial port.'''
        self.port.open()

    def close(self):
        ''' Close the serial port.'''
        self.port.close()

    def write(self, msg):
        time.sleep(1.6)
        self.port.write(msg.encode())

    def readline(self):
        return self.port.readline()

    def readlines(self):
        return self.port.readlines()





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

    def rolluit(self):
        self.offRood()
        self.onGroen()
        self.blink()
        self.offGroen()
        self.onRood()

    def rollin(self):
        self.offGroen()
        self.onRood()
        self.blink()
        self.offRood()
        self.onGroen()







    def getLux(self):
        lux = int(self.getTempLight()[1])
        print(lux)

    def getTemp(self):
        temp = str(self.getTempLight())

        print(temp)

    def getTempLight(self):
        data =self.readlines()
        return data

    def seek(self, pos=0):
        return self.port.seek()



        """
        temp = float(list[3])
        lux = int(list[1])
        return temp
        print(lux)
        """

'''
    def receiver(self):
        buffer_string = ''
        global last_received
        while True:
            buffer_string = buffer_string + str(self.read())
            if '\n' in buffer_string:
                lines = buffer_string.split('\n')
                last_received = lines[-2]
                buffer_string = lines[-1]
        return buffer_string
'''


COM3 = Serializer("COM3")

def main():


    COM3.rolluit()
    COM3.rollin()





    #COM3.receiver()
    #read_data_list = COM3.getTempLight()
    #print(COM3.getTemp(data_list=read_data_list))
    #print(COM3.getLux(data_list=read_data_list))




main()

