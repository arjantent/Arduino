import serial
import time


try:
    arduino = serial.Serial("COM3", 9600)
except:
    print("failed to connect")

ingerold = True
uitgerold = False


def onOffFunction():
    global ingerold
    global uitgerold

    command = input('Type something..:(uitrollen/ inrollen / bye)')
    if command == 'uitrollen' and uitgerold == False:
            print('led ON')
            time.sleep(1)
            arduino.write('H'.encode())
            ingerold = False
            uitgerold = True
            onOffFunction()
    elif command =='inrollen' and ingerold == False:
        print("off")
        time.sleep(1)
        arduino.write('L'.encode())
        ingerold = True
        uitgerold = False
        onOffFunction()
    elif command == 'bye':
        print("see you")
        time.sleep(1)
        arduino.close()
    else:
        print("sorry type something else")
        onOffFunction()

onOffFunction()
