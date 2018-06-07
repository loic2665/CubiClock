import serial

from Constants import *

class Sensors:
    @classmethod
    def getSensorsValue(cls):
        print("Check sensors")
        try:

            arduino = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=5)
            print("Verif arduino OK")
        except:
            pass

        try:
            if arduino.inWaiting() > 0:
                retour = arduino.readlines(arduino.inWaiting())
                ok = retour[0].decode().split("|")
                return Constants.sensors_data
        except:
            Constants.sensors_data = ['SENSORS', '23', '21', '25', '0.00']
