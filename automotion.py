import serial
import time
import cv2
import numpy as np


#arduinoSerialData = serial.Serial("COM13", '9600', timeout=2) 
 
count = 0
count1 = 0
count_1=0
count_2=0
count_3=0
measurement_distPS = 0
listA = [1]
    

ser = serial.Serial("COM6", '9600', timeout=2)
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

xmedium = int(cols / 2)
center = int (cols/ 2)

#x2_medium = int(cols_2 / 2)
#center_2 = int (cols_2/ 2)



    
while True:     

    
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    while True:
        if count == 0:
            count = count+1
            command = input("CW için 1'e CCW için 2'ye basınız: ")
            if command == '1':
                ser.write ('89'.encode())
                
            elif command =='2':
                ser.write ('97'.encode())
                
            else:
                ser.write ('93'.encode())
        else:
            break
                
                

    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        x_medium = int((x + x + w)/2)
            
        
        if x_medium < center+10 and x_medium > center-10:
            for i in listA:
                ser.write('93'.encode())
                print("ready for measurement")
                break
            
        else:
                print("not alligned")

         

    cv2.line(frame, (xmedium, 0), (xmedium, 480), (0, 255, 0),2)
    
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()



        
    




