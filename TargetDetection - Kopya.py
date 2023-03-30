import serial
import time
import cv2
import numpy as np


#arduinoSerialData = serial.Serial("COM13", '9600', timeout=2) 
 
count = 0
count1 = 0
measurement_distPS = 0
    

ser = serial.Serial("COM5", '9600', timeout=2)
#ser_2 = serial.Serial("COM16", '9600', timeout=2)


cap = cv2.VideoCapture(0)
#cap_2 = cv2.VideoCapture(1)

cap.set(3,480)
cap.set(4,320)

#cap_2.set(3,480)
#cap_2.set(4,320)

_, frame = cap.read()
rows, cols, _ = frame.shape

#_, frame2 = cap_2.read()
#rows_2, cols_2, _ = frame2.shape

x_medium = int(cols / 2)
center = int (cols/ 2)

#x2_medium = int(cols_2 / 2)
#center_2 = int (cols_2/ 2)

position = 1500
#position_2 = 90


while True:
    
    angleData1 = ser.readline().decode('utf-8')
    count1 = count1 + 1
    anglemeasurement1 = int(angleData1)

    if (anglemeasurement1 > 180):
        position = 1450
        ser.write((str(position) + 'a').encode('utf-8'))
        print ('angle is : ', anglemeasurement1)
        print (position)
        
    elif (anglemeasurement1 < 180):
        position = 1550
        ser.write((str(position) + 'a').encode('utf-8'))
        print ('angle is : ', anglemeasurement1)
        print (position)
    
    
    elif (anglemeasurement1 == 180):
        position = 1500
        ser.write((str(position) + 'a').encode('utf-8'))
        print ('angle is : ', anglemeasurement1)
        print (position)
        
    




