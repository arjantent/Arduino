import serial
import time

class Serializer:
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
        time.sleep(3)
        self.port.write(msg.encode())

    def recv(self):
        return self.port.readline()

    def on(self):
        self.write("H")

    def off(self):
        self.write("L")



COM3 = Serializer("COM3")

