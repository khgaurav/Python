

import math
import serial
ser=serial.Serial('/dev/ttyUSB0',9600)

while 1:
    ser.write('K')
