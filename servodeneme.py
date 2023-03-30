import serial
import time
import cv2
import numpy as np

ser2 = serial.Serial("COM6", '9600', timeout=2)
count=0

while True:

        if count == 0:
                command = ('89').encode()
                ser2.write (command)
