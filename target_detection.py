import serial
import time
import cv2
import numpy as np


    

ser = serial.Serial("COM6", '9600', timeout=2)



cap = cv2.VideoCapture(0)


cap.set(3,480)
cap.set(4,320)



_, frame = cap.read()
rows, cols, _ = frame.shape



xmedium = int(cols / 2)
center = int (cols/ 2)

position = 180


while True:
    __, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (7,7), 0)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([0, 120, 70])
    high_red = np.array([10,255,255])
    red_mask0 = cv2.inRange(hsv_frame, low_red, high_red)

    low_red = np.array([170, 120, 70])
    high_red = np.array([180,255,255])
    red_mask1 = cv2.inRange(hsv_frame, low_red, high_red)

    red_mask = red_mask0 + red_mask1
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
                
    for cnt in contours:

        cv2.line(frame, (xmedium, 0), (xmedium, 480), (0, 255, 0),2)
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center0 = (int(x),int(y))
        x_medium = int(x)
        radius = int(radius)
        
        if radius >=10:
            print (radius)
            cv2.circle(frame,center0,radius,(0,255,0),2)
            cv2.line(frame, (x_medium,0), (x_medium, 480), (255, 0, 0),2)
            
            
        
            
        if x_medium < xmedium-5:

            position = position + 1
            cv2.circle(frame, (600, 50), 15, (0, 0, 255),-1)
            cv2.putText(frame, 'NOT ALLIGNED', (525,85), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 2)
            cv2.putText(frame, '>', (30,320), cv2.FONT_HERSHEY_TRIPLEX, 2, (100,255,0), 3)
            ser.write((str(position)).encode())
            
        elif x_medium > xmedium+5:
            
            position = position - 1
            cv2.circle(frame, (600, 50), 15, (0, 0, 255),-1)
            cv2.putText(frame, 'NOT ALLIGNED', (525,85), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 2)    
            cv2.putText(frame, '<', (575,320), cv2.FONT_HERSHEY_TRIPLEX, 2, (100,255,0), 3)
            ser.write((str(position)).encode())

        else:       
            cv2.circle(frame, (600, 50), 15, (0, 255, 0),-1)
            cv2.putText(frame, 'READY', (575,85), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,255,0), 2)
    
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

