import serial 
import numpy as np
import matplotlib.pyplot as plt

primer_gps_position = [0,0,0,0,0,0]
seconder_gps_position = [0,0,0,0,0,0]
first_AMMS_position = [0,0,0,0,0,0]
second_AMMS_position = [0,0,0,0,0,0]
third_AMMS_position = [0,0,0,0,0,0]
fourth_AMMS_position = [0,0,0,0,0,0]

dist_first_AMMS = 0
dist_second_AMMS = 0
dist_third_AMMS = 0
dist_fourth_AMMS = 0

orient_first_AMMS = 0
orient_second_AMMS = 0
orient_third_AMMS = 0
orient_fourth_AMMS = 0

relative_orient_first_AMMS = 0
relative_orient_second_AMMS = 0
relative_orient_third_AMMS = 0
relative_orient_fourth_AMMS = 0

distance_read = 0
gyro_primer = 0
gyro_seconder = 0

north_ture = [0,0,0]


arduinoSerialData = serial.Serial('com3',9600) 
 
count = 0

measurement_distPS = 0

while (True):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline().decode('ascii')
        count = count + 1
        measurement = int(myData)
        print(measurement)
        if (count>1000):
            break
        
        
        
