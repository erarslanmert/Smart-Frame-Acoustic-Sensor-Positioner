import serial
import time
import cv2
import numpy as np
from tkinter import*
import threading
import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import math
from tkinter import filedialog
import os
import sys


    
root = Tk()
root.title('Mission File Creator')
root.geometry('1600x900')
root.bind('<Escape>', lambda e: root.quit())

background_image=ImageTk.PhotoImage(Image.open("Breeze.png"))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

settingsButtonImage = ImageTk.PhotoImage(file='settingsicon.png')
refreshButtonImage = ImageTk.PhotoImage(file='refreshicon.png')

settingsFrame = Label(root,borderwidth=5,width=40, height=30,relief="groove")
settingsFrame.place(x=1200,y=70)

settingsLabel= Label(settingsFrame, text="SETTINGS")
settingsLabel.place(x=120,y=15)

settingsIcon= Label(settingsFrame, image=settingsButtonImage )
settingsIcon.place(x=70,y=0)

settingsLabel0= Label(settingsFrame,text="COM # of Lidar :    ")
settingsLabel0.place(x=30,y=53)

settingsEntry0 = Entry(settingsFrame, borderwidth=5, width=10, bg="white")
settingsEntry0.place(x=150,y=50)
settingsEntry0.insert(END, '6')

settingsLabel1= Label(settingsFrame,text="COM # of Servo1 :   ")
settingsLabel1.place(x=30, y=93)

settingsEntry1 = Entry(settingsFrame, borderwidth=5, width=10, bg="white")
settingsEntry1.place(x=150,y=90)
settingsEntry1.insert(END, '9')

settingsLabel2= Label(settingsFrame,text="COM # of Servo2 :   ")
settingsLabel2.place( x=30, y=133)

settingsEntry2 = Entry(settingsFrame, borderwidth=5, width=10, bg="white")
settingsEntry2.place(x=150,y=130)
settingsEntry2.insert(END, '7')

settingsLabel3= Label(settingsFrame,text="1. VideoCapture(#):")
settingsLabel3.place(x=30, y=173)

settingsEntry3 = Entry(settingsFrame, borderwidth=5, width=10, bg="white")
settingsEntry3.place(x=150,y=170)
settingsEntry3.insert(END, '0')

settingsLabel4= Label(settingsFrame,text="2. VideoCapture(#):")
settingsLabel4.place(x=30, y=213)

settingsEntry4 = Entry(settingsFrame, borderwidth=5, width=10, bg="white")
settingsEntry4.place(x=150,y=210)
settingsEntry4.insert(END, '1')

settingsLabel5= Label(settingsFrame,text="Device ID1(AMMSHP-01-00xxx):")
settingsLabel5.place(x=30, y=253)


settingsEntry5 = Entry(settingsFrame, borderwidth=5, width=5, bg="white")
settingsEntry5.place(x=210,y=250)
settingsEntry5.insert(END, '001')
ammsnumber1=str(settingsEntry5.get())

settingsLabel6= Label(settingsFrame,text="Device ID2(AMMSHP-01-00xxx):")
settingsLabel6.place(x=30, y=293)


settingsEntry6 = Entry(settingsFrame, borderwidth=5, width=5, bg="white")
settingsEntry6.place(x=210,y=290)
settingsEntry6.insert(END, '002')
ammsnumber2=str(settingsEntry6.get())

settingsLabel7= Label(settingsFrame,text="Device ID3(AMMSHP-01-00xxx):")
settingsLabel7.place(x=30, y=333)


settingsEntry7 = Entry(settingsFrame, borderwidth=5, width=5, bg="white")
settingsEntry7.place(x=210,y=330)
settingsEntry7.insert(END, '003')
ammsnumber3=str(settingsEntry7.get())

settingsLabel8= Label(settingsFrame,text="Device ID4(AMMSHP-01-00xxx):")
settingsLabel8.place(x=30, y=373)

settingsEntry8 = Entry(settingsFrame, borderwidth=5, width=5, bg="white")
settingsEntry8.place(x=210,y=370)
settingsEntry8.insert(END, '004')
ammsnumber4=str(settingsEntry8.get())

comnumber0="COM7"
comnumber1="COM10"
comnumber2="COM9"

videocapnumber1=0
videocapnumber2=1
cap = cv2.VideoCapture(0)
cap_2 = cv2.VideoCapture(1)
arduinoSerialData = serial.Serial() 
ser = serial.Serial()
ser_2 = serial.Serial()

if cap is None or not cap.isOpened():
    cap=cv2.VideoCapture('aclogus.mp4')
if cap_2 is None or not cap_2.isOpened():
    cap_2=cv2.VideoCapture('aclogus.mp4')
    
def saveSettings():
    global comnumber0, comnumber1, comnumber2, videocapnumber1, videocapnumber2,settingscount,cap,cap_2,ser,ser_2,arduinoSerialData

    ser.close()
    ser_2.close()
    arduinoSerialData.close()
    
    
    comnumber0="COM"+str(settingsEntry0.get())
    comnumber1="COM"+str(settingsEntry1.get())
    comnumber2="COM"+str(settingsEntry2.get())
    videocapnumber1=settingsEntry3.get()
    videocapnumber2=settingsEntry4.get()
    cap = cv2.VideoCapture(int(videocapnumber1))
    cap_2 = cv2.VideoCapture(int(videocapnumber2))
    

    if cap is None or not cap.isOpened():
        cap=cv2.VideoCapture('aclogus.mp4')
    if cap_2 is None or not cap_2.isOpened():
        cap_2=cv2.VideoCapture('aclogus.mp4') 
    
    try:
        arduinoSerialData = serial.Serial(comnumber0, '9600', timeout=2) 
        ser = serial.Serial(comnumber1, '9600', timeout=2)
        ser_2 = serial.Serial(comnumber2, '9600', timeout=2)
    except serial.SerialException as e:
        pass
    except TypeError as e:
        pass
    except PortNotOpenError:
        pass

    
    if(ser.isOpen() == False):
        messagebox.showwarning(title="COM ERROR", message="Servo1 COM# is not correct!")
        
    elif(arduinoSerialData.isOpen() == False):
        messagebox.showwarning(title="COM ERROR", message="Lidar COM# is not correct!")
        
    elif(ser_2.isOpen() == False):
        messagebox.showwarning(title="COM ERROR", message="Servo2 COM# is not correct!")
        
    else:
        pass
        
    threading.Thread(target = readPrimerAngle).start()
    threading.Thread(target = readSeconderAngle).start()
    threading.Thread(target = readDistance).start()

    
    settingsEntry0.config(state='disabled')
    settingsEntry1.config(state='disabled')
    settingsEntry2.config(state='disabled')
    settingsEntry3.config(state='disabled')
    settingsEntry4.config(state='disabled')
    settingsEntry5.config(state='disabled')
    settingsEntry6.config(state='disabled')
    settingsEntry7.config(state='disabled')
    settingsEntry8.config(state='disabled')
    saveSettingsButton.config(state='disabled')
    mycombo.config(state='normal')
    manualButton.config(state='normal')

def refreshSettings():
    settingsEntry0.config(state='normal')
    settingsEntry1.config(state='normal')
    settingsEntry2.config(state='normal')
    settingsEntry3.config(state='normal')
    settingsEntry4.config(state='normal')
    settingsEntry5.config(state='normal')
    settingsEntry6.config(state='normal')
    settingsEntry7.config(state='normal')
    settingsEntry8.config(state='normal')
    saveSettingsButton.config(state='normal')
    mycombo.config(state='disabled')
    manualButton.config(state='disabled')
    disableButtons()

        

saveSettingsButton = Button(settingsFrame, text = "Save Settings",command=saveSettings)
saveSettingsButton.place(x=70,y=410)

refreshButton = Button(settingsFrame,image=refreshButtonImage, command=refreshSettings)
refreshButton.place(x=175,y=410)




count = 0
listB = [1]
listA = []
listAngle1=[]
countagnle1=0
countangle2=0
listAngle2=[]
listDistance=[]
position = 180
position1 = 180
ang1=0
i = 1
flt = 0
ang2 = 0
distance = 0
targeticon1=0
targeticon2=0
angle1=0
angle2=0
showndistance=0



measuredangle1_2=-1
measuredangle1_3=-1
measuredangle1_4=-1
measuredangle2_1=-1
measuredangle3_1=-1
measuredangle4_1=-1


respectiveangle1=0
respectiveangle2=0
respectiveangle3=0
respectiveangle4=0

rotation1_1=0
rotation1_2=0
rotation1_3=0
rotation1_4=0


measureddistance12=0
measureddistance13=0
measureddistance14=0


respectivedist1=0
respectivedist2=0
respectivedist3=0
respectivedist4=0

tempseconderx=0
tempsecondery=0
tempx1=0
tempy1=0
tempx2=0
tempy2=0
tempx3=0
tempy3=0
tempx4=0
tempy4=0



realx1=0
realy1=0
realx2=0
realy2=0
realx3=0
realy3=0
realx4=0
realy4=0
realprimerx=0
realprimery=0
realseconderx=0
realsecondery=0

yaw1=0
yaw2=0
yaw3=0
yaw4=0

coordinaterotation=0





options = ['                ' ,' AMMS 1 - AMMS 2 ', ' AMMS 1 - AMMS 3 ', ' AMMS 1 - AMMS 4 ']

clicked = StringVar()
clicked.set(options[0])


combotext=Label(root,text = "Choose # AMMS", bg="#263037", fg="white")
combotext.place(x=450,y=165)

mycombo = ttk.Combobox(root, value = options)
mycombo.current(0)
mycombo.place(x=450,y=190)
mycombo.config(state='disabled')

consoleframe1= Frame(root,width=400,height=200,borderwidth=5,relief="groove",bg="white")
consoleframe1.place(x=650,y=70)

text0 = Text(consoleframe1,height = 1, width = 52)
text0.insert(END, "Console >>>...")
text0.pack()


text1 = Text(consoleframe1,height = 2, width = 52)
text1.pack()

text2 = Text(consoleframe1,height = 2, width = 52)
text2.pack()


text3 = Text(consoleframe1,height = 2, width = 52)
text3.pack()

consoleframe2= Frame(root,width=400,height=200,borderwidth=5,relief="groove",bg="white")
consoleframe2.place(x=650,y=435)

text4 = Text(consoleframe2,height = 1, width = 52)
text4.insert(END, "Console >>>...")
text4.pack()


text5 = Text(consoleframe2,height = 2, width = 52)
text5.pack()

text6 = Text(consoleframe2,height = 2, width = 52)
text6.pack()

text7 = Text(consoleframe2,height = 2, width = 52)
text7.pack()
   

pageimage = ImageTk.PhotoImage(file="Cartop.png")
pageLabel = Label(root, image=pageimage)
pageLabel.place(x=1250, y = 680)

frame1=Frame(root)
frame1.place(x=185,y=315)
frame2=Frame(root)
frame2.place(x=450,y=70)
frame11=Frame(root)
frame11.place(x=450,y=220)

frame3=Frame(root)
frame3.place(x=185,y=680)
frame4=Frame(root)
frame4.place(x=450,y=435)
frame33=Frame(root)
frame33.place(x=450,y=555)

lmain = Label(root, borderwidth=5, relief="sunken")
lmain.place(x=100,y=50)
lmain2 = Label(root, borderwidth=5, relief="sunken")
lmain2.place(x=100,y=415)
label1 = Label(root, text = "Primer Camera",bg="#263037",fg="white")
label1.place(x=222,y=20)
label2 = Label(root, text = "Seconder Camera",bg="#1F4265",fg="white")
label2.place(x=215,y=385)


Pammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\FirstAMMS (2).png")
Pammsimageopen=Pammsimageopen.rotate(rotation1_1)
Pammsimage= ImageTk.PhotoImage(Pammsimageopen)
Sammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\SecondAMMS (2).png")
Sammsimageopen=Sammsimageopen.rotate(rotation1_2)
Sammsimage= ImageTk.PhotoImage(Sammsimageopen)
Tammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\ThirdAMMS (2).png")
Tammsimageopen=Tammsimageopen.rotate(rotation1_3)
Tammsimage= ImageTk.PhotoImage(Tammsimageopen)
Fammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\ThirdAMMS (2).png")
Fammsimageopen=Fammsimageopen.rotate(rotation1_4)
Fammsimage= ImageTk.PhotoImage(Fammsimageopen)



gridFrame = Frame(root,borderwidth=5,relief = "solid")
canvas1 = Canvas(gridFrame, width = 700, height=600, bg="LightCyan2")
canvas1.pack()

x1,x2,x3,x4 = 400, 300, 100, 600
y1,y2,y3,y4 = 450, 100, 250, 250
x11=x1-50*(math.cos(rotation1_1*math.pi/180))
y11=y1+50*(math.sin(rotation1_1*math.pi/180))
x22=x2+50*(math.cos(rotation1_2*math.pi/180))
y22=y2-50*(math.sin(rotation1_2*math.pi/180))
x33=x11+200*math.cos(math.atan((x11-x22)/(y22-y11)))
y33=y11+200*math.sin(math.atan((x11-x22)/(y22-y11)))


im1=canvas1.create_image(x1,y1,image=Pammsimage)
im2=canvas1.create_image(x2,y2,image=Sammsimage)
im3=canvas1.create_image(x3,y3,image=Tammsimage)
im4=canvas1.create_image(x4,y4,image=Fammsimage)
lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))
linTN=canvas1.create_line(x11, y11, x22, y22,arrow=LAST, fill="blue", width=3)
linTE=canvas1.create_line(x11, y11, x33, y33, arrow=LAST, fill="blue", width=3)
linTN1=canvas1.create_line(x11, y11, x2, y2, fill="red")
linTN2=canvas1.create_line(x11, y11, x3, y3, fill="red")
linTN3=canvas1.create_line(x11, y11, x4, y4, fill="red")
gridFrame.pack()    
gridFrame.pack_forget()



def manualCalculation():
    global manualguideimage
    global measuredangle1_2
    global measuredangle1_3
    global measuredangle1_4
    global measuredangle2_1
    global measuredangle3_1
    global measuredangle4_1
    global measureddistance12
    global measureddistance13
    global measureddistance14
    
    manualWindow = Toplevel(root)
    manualWindow.title('MANUAL CALCULATION WINDOW')

    manualFrame=Label(manualWindow,width=150,height=35)
    manualFrame.pack()


    titleFrame=Label(manualWindow,text="MANUAL CALCULATION TOOL")
    titleFrame.place(x=450,y=10)
    
    angleLabel1_2= Label(manualFrame,text="Angle Between AMMS1 to AMMS2:                               degrees (1)")
    angleLabel1_2.place(x=15,y=53)

    manualEntry0 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry0.place(x=210,y=50)
    
    
    angleLabel2_1= Label(manualFrame,text="Angle Between AMMS2 to AMMS1:                               degrees (2)")
    angleLabel2_1.place(x=15,y=93)

    manualEntry1 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry1.place(x=210,y=90)
    

    distanceLabel2_1= Label(manualFrame,text="Distance Between AMMS2-AMMS1:                              cm (3)")
    distanceLabel2_1.place(x=15,y=133)

    manualEntry2 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry2.place(x=210,y=130)
    

    angleLabel1_3= Label(manualFrame,text="Angle Between AMMS1 to AMMS3:                               degrees (4)")
    angleLabel1_3.place(x=15,y=173)

    manualEntry3 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry3.place(x=210,y=170)
   

    angleLabel3_1= Label(manualFrame,text="Angle Between AMMS3 to AMMS1:                               degrees (5)")
    angleLabel3_1.place(x=15,y=213)

    manualEntry4 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry4.place(x=210,y=210)
    

    distanceLabel3_1= Label(manualFrame,text="Distance Between AMMS3-AMMS1:                              cm (6)")
    distanceLabel3_1.place(x=15,y=253)

    manualEntry5 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry5.place(x=210,y=250)
    

    angleLabel1_4= Label(manualFrame,text="Angle Between AMMS1 to AMMS4:                               degrees (7)")
    angleLabel1_4.place(x=15,y=293)

    manualEntry6 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry6.place(x=210,y=290)
    

    angleLabel4_1= Label(manualFrame,text="Angle Between AMMS4 to AMMS1:                               degrees (8)")
    angleLabel4_1.place(x=15,y=333)

    manualEntry7 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry7.place(x=210,y=330)
    

    distanceLabel4_1= Label(manualFrame,text="Distance Between AMMS4-AMMS1:                              cm (9)")
    distanceLabel4_1.place(x=15,y=373)

    manualEntry8 = Entry(manualFrame, borderwidth=5, width=10, bg="white")
    manualEntry8.place(x=210,y=370)

    
   
    
    def setValues():
        global measuredangle1_2
        global measuredangle1_3
        global measuredangle1_4
        global measuredangle2_1
        global measuredangle3_1
        global measuredangle4_1
        global measureddistance12
        global measureddistance13
        global measureddistance14
        measuredangle1_2 = int(manualEntry0.get())
        measuredangle2_1 = int(manualEntry1.get())
        measureddistance12= int(manualEntry2.get())
        measuredangle1_3 = int(manualEntry3.get())
        measuredangle3_1 = int(manualEntry4.get())
        measureddistance13 = int(manualEntry5.get())
        measuredangle1_4 = int(manualEntry6.get())
        measuredangle4_1 = int(manualEntry7.get())
        measureddistance14 = int(manualEntry8.get())
        
    missionfilegenerator = Button(manualFrame, text = "Generate Mission File",command= lambda:[setValues(),createMissionFile(),bar()],width=30,height=2)
    missionfilegenerator.place(x=70,y=420)

    manualguideimage=Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\manualguidence.png")
    manualguideimage= ImageTk.PhotoImage(manualguideimage)

    canvas2Label=Label(manualWindow,image=manualguideimage,borderwidth=5,relief="groove")
    canvas2Label.place(x=450,y=40)

    mycombo.config(state='disabled')
    disableButtons()




def disableButtons():
    rhButton.config(state='disabled')
    rlButton.config(state='disabled')
    rmButton.config(state='disabled')
    lhButton.config(state='disabled')
    llButton.config(state='disabled')
    lmButton.config(state='disabled')
    zeroButton.config(state='disabled')
    refButton.config(state='disabled')
    targetButton.config(state='disabled')
    rhButton2.config(state='disabled')
    rlButton2.config(state='disabled')
    rmButton2.config(state='disabled')
    lhButton2.config(state='disabled')
    llButton2.config(state='disabled')
    lmButton2.config(state='disabled')
    zeroButton2.config(state='disabled')
    refButton2.config(state='disabled')
    targetButton2.config(state='disabled')
    zoomButton1.config(state='disabled')
    zoomButton2.config(state='disabled')
    targeticonButton1.config(state='disabled')
    targeticonButton2.config(state='disabled')
    setsystemButton.config(state='disabled')
    missonfileButton.config(state='disabled')
    manualButton.config(state='disabled')

def enableButtons():
    rhButton.config(state='normal')
    rlButton.config(state='normal')
    rmButton.config(state='normal')
    lhButton.config(state='normal')
    llButton.config(state='normal')
    lmButton.config(state='normal')
    zeroButton.config(state='normal')
    refButton.config(state='normal')
    targetButton.config(state='normal')
    rhButton2.config(state='normal')
    rlButton2.config(state='normal')
    rmButton2.config(state='normal')
    lhButton2.config(state='normal')
    llButton2.config(state='normal')
    lmButton2.config(state='normal')
    zeroButton2.config(state='normal')
    refButton2.config(state='normal')
    targetButton2.config(state='normal')
    zoomButton1.config(state='normal')
    zoomButton2.config(state='normal')
    targeticonButton1.config(state='normal')
    targeticonButton2.config(state='normal')
    setsystemButton.config(state='normal')



def comboclick(event):
    global measuredangle1_2
    global measuredangle1_3
    global measuredangle1_4
    global measuredangle2_1
    global measuredangle3_1
    global measuredangle4_1
    global measureddistance12
    global measureddistance13
    global measureddistance14
    if mycombo.get() == options[1]:
        enableButtons()
        manualButton.config(state='disabled')
    elif mycombo.get() == options[2] and measuredangle1_2>=0 and measuredangle2_1>=0 and measureddistance12 > 0:
        enableButtons()
    elif mycombo.get() == options[3] and measuredangle1_3>=0 and measuredangle3_1>=0 and measureddistance13 > 0:
        enableButtons()
    else:
        disableButtons()

mycombo.bind("<<ComboboxSelected>>",comboclick)




  
def openAmms(e):

    global im1, im2, im3, im4, lin1, lin2, lin3, linTN, linTE, linTN1, linTN2, linTN3, labelNorth
    global Pammsimageopen
    global Pammsimage,Sammsimage,Tammsimage,Fammsimage 
    global respectiveangle1
    global realx1,realy1,realx2,realy2,realx3,realy3,realx4,realy4,rotation1_1,rotation1_2,rotation1_3,rotation1_4
    global measuredangle1_2,measuredangle2_1,measuredangle1_3,measuredangle3_1,measuredangle1_4,measuredangle4_1
    global tempx1,tempy1,tempx2,tempy2,tempx3,tempy3,tempx4,tempy4

    
    if measuredangle1_2>=0 and measuredangle2_1>=0:
        
        canvas1.delete(im1)
        canvas1.delete(im2)
        canvas1.delete(im3)
        canvas1.delete(im4)
        canvas1.delete(lin1)
        canvas1.delete(lin2)
        canvas1.delete(lin3)
        canvas1.delete(linTN)
        canvas1.delete(linTE)
        canvas1.delete(linTN1)
        canvas1.delete(linTN2)
        canvas1.delete(linTN3)
        
        if rotation1_1==180:
            shift=45
        else:
            shift=-45
        
        if 90<=measuredangle1_2<100 or 270<measuredangle1_2<=280:
            x1=500
        elif 80<=measuredangle1_2<90 or 260<measuredangle1_2<=270:
            x1=200
        else:
            x1=350   
        y1=450
        x2=x1+tempx2*3+shift
        y2=y1-tempy2*3
        x3=x1+tempx3*3+shift
        y3=y1-tempy3*3
        x4=x1+tempx4*3+shift
        y4=y1-tempy4*3
        x11=x1-50*(math.cos(rotation1_1*math.pi/180))
        y11=y1+50*(math.sin(rotation1_1*math.pi/180))
        x22=x2+50*(math.cos(rotation1_2*math.pi/180))
        y22=y2-50*(math.sin(rotation1_2*math.pi/180))
        if y3>y1 or y4>y1:
            y1=300
            x2=x1+tempx2*3+shift
            y2=y1-tempy2*3
            x3=x1+tempx3*3+shift
            y3=y1-tempy3*3
            x4=x1+tempx4*3+shift
            y4=y1-tempy4*3
            x11=x1-50*(math.cos(rotation1_1*math.pi/180))
            y11=y1+50*(math.sin(rotation1_1*math.pi/180))
            x22=x2+50*(math.cos(rotation1_2*math.pi/180))
            y22=y2-50*(math.sin(rotation1_2*math.pi/180))
    
        if (y22-y11)==0 and (x11-x22)>0:
            x33=x11
            y33=y11+200

        elif (y22-y11)==0 and (x11-x22)<0:
            x33=x11
            y33=y11-200

        else:
            x33=x11+200*math.cos(math.atan((x11-x22)/(y22-y11)))
            y33=y11+200*math.sin(math.atan((x11-x22)/(y22-y11)))

        Pammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\FirstAMMS (2).png")
        Pammsimageopen=Pammsimageopen.rotate(rotation1_1)
        Pammsimage= ImageTk.PhotoImage(Pammsimageopen)
        Sammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\SecondAMMS (2).png")
        Sammsimageopen=Sammsimageopen.rotate(rotation1_2)
        Sammsimage= ImageTk.PhotoImage(Sammsimageopen)
        im1=canvas1.create_image(x1,y1,image=Pammsimage)
        im2=canvas1.create_image(x2,y2,image=Sammsimage)
        lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
        lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
        linTN=canvas1.create_line(x11, y11, x22, y22,arrow=LAST, fill="blue", width=3)
        linTE=canvas1.create_line(x11, y11, x33, y33, arrow=LAST, fill="blue", width=3)
        linTN1=canvas1.create_line(x11, y11, x2, y2, fill="red")

        gridFrame.update()

        gridFrame.place(x=450,y=50)

    if measuredangle1_2>=0 and measuredangle2_1>=0 and measuredangle1_3>=0 and measuredangle3_1>=0:
        
        canvas1.delete(im1)
        canvas1.delete(im2)
        canvas1.delete(im3)
        canvas1.delete(im4)
        canvas1.delete(lin1)
        canvas1.delete(lin2)
        canvas1.delete(lin3)
        canvas1.delete(linTN)
        canvas1.delete(linTE)
        canvas1.delete(linTN1)
        canvas1.delete(linTN2)
        canvas1.delete(linTN3)

        if rotation1_1==180:
            shift=45
        else:
            shift=-45
        if 90<=measuredangle1_2<100 or 270<measuredangle1_2<=280:
            x1=500
        elif 80<=measuredangle1_2<90 or 260<measuredangle1_2<=270:
            x1=200
        else:
            x1=350   
        y1=450
        x2=x1+tempx2*3+shift
        y2=y1-tempy2*3
        x3=x1+tempx3*3+shift
        y3=y1-tempy3*3
        x4=x1+tempx4*3+shift
        y4=y1-tempy4*3
        x11=x1-50*(math.cos(rotation1_1*math.pi/180))
        y11=y1+50*(math.sin(rotation1_1*math.pi/180))
        x22=x2+50*(math.cos(rotation1_2*math.pi/180))
        y22=y2-50*(math.sin(rotation1_2*math.pi/180))
        if y3>y1 or y4>y1:
            y1=300
            x2=x1+tempx2*3+shift
            y2=y1-tempy2*3
            x3=x1+tempx3*3+shift
            y3=y1-tempy3*3
            x4=x1+tempx4*3+shift
            y4=y1-tempy4*3
            x11=x1-50*(math.cos(rotation1_1*math.pi/180))
            y11=y1+50*(math.sin(rotation1_1*math.pi/180))
            x22=x2+50*(math.cos(rotation1_2*math.pi/180))
            y22=y2-50*(math.sin(rotation1_2*math.pi/180))
    
        if (y22-y11)==0 and (x11-x22)>0:
            x33=x11
            y33=y11+200

        elif (y22-y11)==0 and (x11-x22)<0:
            x33=x11
            y33=y11-200

        else:
            x33=x11+200*math.cos(math.atan((x11-x22)/(y22-y11)))
            y33=y11+200*math.sin(math.atan((x11-x22)/(y22-y11)))


        Pammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\FirstAMMS (2).png")
        Pammsimageopen=Pammsimageopen.rotate(rotation1_1)
        Pammsimage= ImageTk.PhotoImage(Pammsimageopen)
        Sammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\SecondAMMS (2).png")
        Sammsimageopen=Sammsimageopen.rotate(rotation1_2)
        Sammsimage= ImageTk.PhotoImage(Sammsimageopen)
        Tammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\ThirdAMMS (2).png")
        Tammsimageopen=Tammsimageopen.rotate(rotation1_3)
        Tammsimage= ImageTk.PhotoImage(Tammsimageopen)
        im1=canvas1.create_image(x1,y1,image=Pammsimage)
        im2=canvas1.create_image(x2,y2,image=Sammsimage)
        im3=canvas1.create_image(x3,y3,image=Tammsimage)
        lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
        lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
        linTN=canvas1.create_line(x11, y11, x22, y22,arrow=LAST, fill="blue", width=3)
        linTE=canvas1.create_line(x11, y11, x33, y33, arrow=LAST, fill="blue", width=3)
        linTN1=canvas1.create_line(x11, y11, x2, y2, fill="red")
        linTN2=canvas1.create_line(x11, y11, x3, y3, fill="red")

        gridFrame.update()

        gridFrame.place(x=450,y=50)

    if measuredangle1_2>=0 and measuredangle2_1>=0 and measuredangle1_3>=0 and measuredangle3_1>=0 and measuredangle1_4>=0 and measuredangle4_1>=0:
        
        canvas1.delete(im1)
        canvas1.delete(im2)
        canvas1.delete(im3)
        canvas1.delete(im4)
        canvas1.delete(lin1)
        canvas1.delete(lin2)
        canvas1.delete(lin3)
        canvas1.delete(linTN)
        canvas1.delete(linTE)
        canvas1.delete(linTN1)
        canvas1.delete(linTN2)
        canvas1.delete(linTN3)
        if rotation1_1==180:
            shift=45
        else:
            shift=-45
        if 90<=measuredangle1_2<100 or 270<measuredangle1_2<=280:
            x1=500
        elif 80<=measuredangle1_2<90 or 260<measuredangle1_2<=270:
            x1=200
        else:
            x1=350   
        y1=450
        x2=x1+tempx2*3+shift
        y2=y1-tempy2*3
        x3=x1+tempx3*3+shift
        y3=y1-tempy3*3
        x4=x1+tempx4*3+shift
        y4=y1-tempy4*3
        x11=x1-50*(math.cos(rotation1_1*math.pi/180))
        y11=y1+50*(math.sin(rotation1_1*math.pi/180))
        x22=x2+50*(math.cos(rotation1_2*math.pi/180))
        y22=y2-50*(math.sin(rotation1_2*math.pi/180))
        if y3>y1 or y4>y1:
            y1=300
            x2=x1+tempx2*3+shift
            y2=y1-tempy2*3
            x3=x1+tempx3*3+shift
            y3=y1-tempy3*3
            x4=x1+tempx4*3+shift
            y4=y1-tempy4*3
            x11=x1-50*(math.cos(rotation1_1*math.pi/180))
            y11=y1+50*(math.sin(rotation1_1*math.pi/180))
            x22=x2+50*(math.cos(rotation1_2*math.pi/180))
            y22=y2-50*(math.sin(rotation1_2*math.pi/180))
    
        if (y22-y11)==0 and (x11-x22)>0:
            x33=x11
            y33=y11+200

        elif (y22-y11)==0 and (x11-x22)<0:
            x33=x11
            y33=y11-200

        else:
            x33=x11+200*math.cos(math.atan((x11-x22)/(y22-y11)))
            y33=y11+200*math.sin(math.atan((x11-x22)/(y22-y11)))



        Pammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\FirstAMMS (2).png")
        Pammsimageopen=Pammsimageopen.rotate(rotation1_1)
        Pammsimage= ImageTk.PhotoImage(Pammsimageopen)
        Sammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\SecondAMMS (2).png")
        Sammsimageopen=Sammsimageopen.rotate(rotation1_2)
        Sammsimage= ImageTk.PhotoImage(Sammsimageopen)
        Tammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\ThirdAMMS (2).png")
        Tammsimageopen=Tammsimageopen.rotate(rotation1_3)
        Tammsimage= ImageTk.PhotoImage(Tammsimageopen)
        Fammsimageopen= Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\ThirdAMMS (2).png")
        Fammsimageopen=Fammsimageopen.rotate(rotation1_4)
        Fammsimage= ImageTk.PhotoImage(Fammsimageopen)

        im1=canvas1.create_image(x1,y1,image=Pammsimage)
        im2=canvas1.create_image(x2,y2,image=Sammsimage)
        im3=canvas1.create_image(x3,y3,image=Tammsimage)
        im4=canvas1.create_image(x4,y4,image=Fammsimage)
        lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
        lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
        lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))
        linTN=canvas1.create_line(x11, y11, x22, y22,arrow=LAST, fill="blue", width=3)
        linTE=canvas1.create_line(x11, y11, x33, y33, arrow=LAST, fill="blue", width=3)
        linTN1=canvas1.create_line(x11, y11, x2, y2, fill="red")
        linTN2=canvas1.create_line(x11, y11, x3, y3, fill="red")
        linTN3=canvas1.create_line(x11, y11, x4, y4, fill="red")

        gridFrame.update()

        gridFrame.place(x=450,y=50)
    else:
    
        gridFrame.update()

        gridFrame.place(x=450,y=50)
  
  
    
def closeAmms(e):

    global x1,x2,x3,x4
    global y1,y2,y3,y4
    global im1, im2, im3, im4, lin1, lin2, lin3
    global Pammsimageopen
    global realx1,realy1,realx2,realy2,realx3,realy3,realx4,realy4,rotation1_1,rotation1_2,rotation1_3,rotation1_4


    gridFrame.place_forget()

pageLabel.bind("<Enter>",openAmms)
pageLabel.bind("<Leave>",closeAmms)




def bar():


    import time
    
    newWindow = Toplevel(root, bg='gray')
    newWindow.title("Mission File In Progress")
    newWindow.geometry("600x100")
    progress = Progressbar(newWindow, orient = HORIZONTAL, length = 500, mode = 'determinate')
    progress.place(x=50,y=40)
    var = StringVar()
    var.set('Progress %0')
    tempLabel = Label (newWindow, textvariable = var, bg="white")
    tempLabel.place(x=50,y=10)
    
    var2 = StringVar()
    var2.set('Initializing...')
    tempLabe2 = Label (newWindow, textvariable = var2,width=70,bg="white")
    tempLabe2.place(x=50,y=70)
    time.sleep(0.50)
    var2.set('Connecting')
    time.sleep(0.50)
    
    for i in range(0,21):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.01)
        
        
    var2.set('Getting Primer Servo Angle')
    root.update_idletasks()
    time.sleep(0.01)
    
    var2.set('Getting Seconder Servo Angle')
    root.update_idletasks()
    time.sleep(0.01)
    
    for i in range(20,41):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.01)
    
    var2.set('Getting Distance Data')
    root.update_idletasks()
    time.sleep(0.01) 

    var2.set('Waiting for Lidar Measurement')
    root.update_idletasks()
    time.sleep(0.01)

    for i in range(40,51):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.01)
    
    var2.set('Checking Sensor Data')
    root.update_idletasks()
    time.sleep(0.01)

    var2.set('Sensor Data Validated')
    root.update_idletasks()
    time.sleep(0.01)

    for i in range(50,61):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.01)
    

    var2.set('Generating Mission File')
    root.update_idletasks()
    time.sleep(0.01)

    var2.set('Writing Points and Angles')
    root.update_idletasks()
    time.sleep(0.01)
  
    for i in range(60,81):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.01)

        
    var2.set('Mission File Is Ready')
    root.update_idletasks()
    time.sleep(0.1) 
    for i in range(80,101):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.01)
        
    messagebox.showinfo("Info!", "Completed. Mission file is saved to dekstop!")
    progress.destroy()
    newWindow.destroy()


def readDistance():
    global distance
    global showndistance
    global listDistance
    while True:
        a = arduinoSerialData.readline()        
        string_k = a.decode('utf-8')   
        stringk = string_k.rstrip() 
        distance = int(stringk)+10
        text1.delete("1.0","end")
        text1.insert(END, "DISTANCE : " + str(distance))
        text5.delete("1.0","end")
        text5.insert(END, "DISTANCE : " + str(distance))
        listDistance.append(distance)
        if len(listDistance)>100:
            del listDistance[0:11]
        
        showndistance=sum(listDistance)/len(listDistance)
        

    
    

def readPrimerAngle():
    global ang1
    global listAngle1
    global angle1
    while True:
        b = ser.readline()        
        string_n = b.decode()   
        string = string_n.rstrip() 
        ang1 = int(string)
        text2.delete("1.0","end")
        text2.insert(END, "1st ANGLE : "+ string)
        listAngle1.append(ang1)
        if len(listAngle1)>100:
            del listAngle1[0:11]
        
        angle1=sum(listAngle1)/len(listAngle1)
        




def readSeconderAngle():
    
    global ang2
    global listAngle2
    global angle2
    while True:
        b = ser_2.readline()        
        string_n = b.decode()   
        string = string_n.rstrip() 
        ang2 = int(string)
        text6.delete("1.0","end")
        text6.insert(END, "2nd ANGLE : "+ string)
        listAngle2.append(ang2)
        if len(listAngle2)>100:
            del listAngle2[0:11]
        
        angle2=sum(listAngle2)/len(listAngle2)
        

    

def saveMeasurements():
    global listAngle1
    global listAngle2   
    global angle1
    global angle2
    global showndistance
    global listDistance
    global measuredangle1_2
    global measuredangle1_3
    global measuredangle1_4
    global measuredangle2_1
    global measuredangle3_1
    global measuredangle4_1
    global measureddistance12
    global measureddistance13
    global measureddistance14
    
    response1 = messagebox.askyesno("Alert", "Please check number of sensor relations. \n    Do you want to countinue saving?")
    if response1 == False:
        return ()

 
    if mycombo.get() == options[1]:
        measuredangle1_2=round(angle1)
        measuredangle2_1=round(angle2)
        measureddistance12=round(showndistance)
        calculatePositions1_2()
        disableButtons()

         
    if mycombo.get() == options[2]:
        measuredangle1_3=round(angle1)
        measuredangle3_1=round(angle2)
        measureddistance13=round(showndistance)
        calculatePositions1_3()
        disableButtons()


    if mycombo.get() == options[3]:
        measuredangle1_4=round(angle1)
        measuredangle4_1=round(angle2)
        measureddistance14=round(showndistance)
        calculatePositions1_4()
        disableButtons()
        missonfileButton.config(state='normal')
        

        

    listAngle1.clear()
    listAngle2.clear()
    listDistance.clear()
    
def calculatePositions1_2():
    global measuredangle1_2
    global measuredangle1_3
    global measuredangle1_4
    global measuredangle2_1
    global measuredangle3_1
    global measuredangle4_1
    global respectiveangle1
    global respectiveangle2
    global respectiveangle3
    global respectiveangle4
    global measureddistance12
    global measureddistance13
    global measureddistance14
    global respectivedist1
    global respectivedist2
    global respectivedist3
    global respectivedist4
    global tempx1
    global tempy1
    global tempx2
    global tempy2
    global tempx3
    global tempy3
    global tempx4
    global tempy4
    global tempseconderx
    global tempsecondery
    global realx1
    global realy1
    global realx2
    global realy2
    global realx3
    global realy3
    global realx4
    global realy4
    global realprimerx
    global realprimery
    global realseconderx
    global realsecondery
    global rotation1_1
    global rotation1_2
    global rotation1_3
    global rotation1_4
    global coordinaterotation
    global yaw1
    global yaw2
    global yaw3
    global yaw4

    if 90 <= measuredangle1_2 <= 270:

    
        rotation1_1= 180
        rotation1_2 = measuredangle2_1 - measuredangle1_2
        realprimerx=0
        realprimery=0
        realseconderx=0
        tempx1= realprimerx +15*(math.cos(rotation1_1*math.pi/180))
        tempy1= realprimery +15*(math.sin(rotation1_1*math.pi/180))
        tempx2= tempx1 - measureddistance12*(math.cos((90-measuredangle1_2)*math.pi/180))
        tempy2= tempy1 - measureddistance12*(math.sin((90-measuredangle1_2)*math.pi/180))
        tempseconderx = tempx2+15*(math.cos(rotation1_2*math.pi/180))
        tempsecondery = tempy2+15*(math.sin(rotation1_2*math.pi/180))
        realsecondery = ((tempsecondery**2+tempseconderx**2)**0.5)
        coordinaterotation = (math.atan(tempseconderx/tempsecondery))*(-1)
        realx1 = tempx1*math.cos(coordinaterotation) + tempy1*math.sin(coordinaterotation)
        realy1 = (-1)*tempx1*math.sin(coordinaterotation) + tempy1*math.cos(coordinaterotation)
        realx2 = tempx2*math.cos(coordinaterotation) + tempy2*math.sin(coordinaterotation)
        realy2 = (-1)*tempx2*math.sin(coordinaterotation) + tempy2*math.cos(coordinaterotation)
        yaw1 = (coordinaterotation*180/math.pi) - rotation1_1
        if round(yaw1) < -180:
            yaw1 = yaw1 + 360
        yaw2 = yaw1 - (rotation1_2 + rotation1_1)
        if round(yaw2) < -180:
            yaw2 = yaw2 + 360



    else:

        rotation1_1=0
        rotation1_2 =180 + measuredangle2_1 - measuredangle1_2
        realprimerx=0
        realprimery=0
        realseconderx=0
        tempx1= realprimerx +15*(math.cos(rotation1_1*math.pi/180))
        tempy1= realprimery +15*(math.sin(rotation1_1*math.pi/180))
        tempx2= tempx1 + measureddistance12*(math.cos((90-measuredangle1_2)*math.pi/180))
        tempy2= tempy1 + measureddistance12*(math.sin((90-measuredangle1_2)*math.pi/180))
        tempseconderx = tempx2+15*(math.cos(rotation1_2*math.pi/180))
        tempsecondery = tempy2+15*(math.sin(rotation1_2*math.pi/180))
        realsecondery = ((tempsecondery**2+tempseconderx**2)**0.5)
        coordinaterotation = (math.atan(tempseconderx/tempsecondery))
        realx1 = tempx1*math.cos(coordinaterotation) + tempy1*math.sin(coordinaterotation)
        realy1 = (-1)*tempx1*math.sin(coordinaterotation) + tempy1*math.cos(coordinaterotation)
        realx2 = tempx2*math.cos(coordinaterotation) + tempy2*math.sin(coordinaterotation)
        realy2 = (-1)*tempx2*math.sin(coordinaterotation) + tempy2*math.cos(coordinaterotation)
        yaw1 = (coordinaterotation*180/math.pi) - rotation1_1
        if round(yaw1) < -180:
            yaw1 = yaw1 + 360
        yaw2 = yaw1 - (rotation1_2 + rotation1_1)
        if round(yaw2) < -180:
            yaw2 = yaw2 + 360


def calculatePositions1_3():
    global measuredangle1_2
    global measuredangle1_3
    global measuredangle1_4
    global measuredangle2_1
    global measuredangle3_1
    global measuredangle4_1
    global respectiveangle1
    global respectiveangle2
    global respectiveangle3
    global respectiveangle4
    global measureddistance12
    global measureddistance13
    global measureddistance14
    global respectivedist1
    global respectivedist2
    global respectivedist3
    global respectivedist4
    global tempx1
    global tempy1
    global tempx2
    global tempy2
    global tempx3
    global tempy3
    global tempx4
    global tempy4
    global tempseconderx
    global tempsecondery
    global realx1
    global realy1
    global realx2
    global realy2
    global realx3
    global realy3
    global realx4
    global realy4
    global realprimerx
    global realprimery
    global realseconderx
    global realsecondery
    global rotation1_1
    global rotation1_2
    global rotation1_3
    global rotation1_4
    global coordinaterotation
    global yaw1
    global yaw2
    global yaw3
    global yaw4

    if 90 <= measuredangle1_3 <= 270:

        if rotation1_1==180:
    
            rotation1_13= 180
            rotation1_3 = measuredangle3_1 - measuredangle1_3
            tempx3= tempx1 - measureddistance13*(math.cos((90-measuredangle1_3)*math.pi/180))
            tempy3= tempy1 - measureddistance13*(math.sin((90-measuredangle1_3)*math.pi/180))
            realx3 = tempx3*math.cos(coordinaterotation) + tempy3*math.sin(coordinaterotation)
            realy3 = (-1)*tempx3*math.sin(coordinaterotation) + tempy3*math.cos(coordinaterotation)
            yaw3 = yaw1 - (rotation1_3 + rotation1_13)
            if round(yaw3) < -180:
                yaw3 = yaw3 + 360
        else:

            rotation1_13=0
            rotation1_3 =180 + measuredangle3_1 - measuredangle1_3
            tempx3= tempx1 + measureddistance13*(math.cos((90-measuredangle1_3)*math.pi/180))
            tempy3= tempy1 + measureddistance13*(math.sin((90-measuredangle1_3)*math.pi/180))
            realx3 = tempx3*math.cos(coordinaterotation) + tempy3*math.sin(coordinaterotation)
            realy3 = (-1)*tempx3*math.sin(coordinaterotation) + tempy3*math.cos(coordinaterotation)
            yaw3 = yaw1 - (rotation1_3 + rotation1_13)
            if round(yaw3) < -180:
                yaw3 = yaw3 + 360


    else:
         if rotation1_1==180:
    
            rotation1_13= 180
            rotation1_3 = measuredangle3_1 - measuredangle1_3
            tempx3= tempx1 - measureddistance13*(math.cos((90-measuredangle1_3)*math.pi/180))
            tempy3= tempy1 - measureddistance13*(math.sin((90-measuredangle1_3)*math.pi/180))
            realx3 = tempx3*math.cos(coordinaterotation) + tempy3*math.sin(coordinaterotation)
            realy3 = (-1)*tempx3*math.sin(coordinaterotation) + tempy3*math.cos(coordinaterotation)
            yaw3 = yaw1 - (rotation1_3 + rotation1_13)
            if round(yaw3) < -180:
                yaw3 = yaw3 + 360
         else:

            rotation1_13=0
            rotation1_3 =180 + measuredangle3_1 - measuredangle1_3
            tempx3= tempx1 + measureddistance13*(math.cos((90-measuredangle1_3)*math.pi/180))
            tempy3= tempy1 + measureddistance13*(math.sin((90-measuredangle1_3)*math.pi/180))
            realx3 = tempx3*math.cos(coordinaterotation) + tempy3*math.sin(coordinaterotation)
            realy3 = (-1)*tempx3*math.sin(coordinaterotation) + tempy3*math.cos(coordinaterotation)
            yaw3 = yaw1 - (rotation1_3 + rotation1_13)
            if round(yaw3) < -180:
                yaw3 = yaw3 + 360
        
    

def calculatePositions1_4():
    global measuredangle1_2
    global measuredangle1_3
    global measuredangle1_4
    global measuredangle2_1
    global measuredangle3_1
    global measuredangle4_1
    global respectiveangle1
    global respectiveangle2
    global respectiveangle3
    global respectiveangle4
    global measureddistance12
    global measureddistance13
    global measureddistance14
    global respectivedist1
    global respectivedist2
    global respectivedist3
    global respectivedist4
    global tempx1
    global tempy1
    global tempx2
    global tempy2
    global tempx3
    global tempy3
    global tempx4
    global tempy4
    global tempseconderx
    global tempsecondery
    global realx1
    global realy1
    global realx2
    global realy2
    global realx3
    global realy3
    global realx4
    global realy4
    global realprimerx
    global realprimery
    global realseconderx
    global realsecondery
    global rotation1_1
    global rotation1_2
    global rotation1_3
    global rotation1_4
    global coordinaterotation
    global yaw1
    global yaw2
    global yaw3
    global yaw4
  

    if 90 <= measuredangle1_4 <= 270:
        
        if rotation1_1==180:
            rotation1_14= 180
            rotation1_4 = measuredangle4_1 - measuredangle1_4
            tempx4= tempx1 - measureddistance14*(math.cos((90-measuredangle1_4)*math.pi/180))
            tempy4= tempy1 - measureddistance14*(math.sin((90-measuredangle1_4)*math.pi/180))
            realx4 = tempx4*math.cos(coordinaterotation) + tempy4*math.sin(coordinaterotation)
            realy4 = (-1)*tempx4*math.sin(coordinaterotation) + tempy4*math.cos(coordinaterotation)
            yaw4 = yaw1 - (rotation1_4 + rotation1_14)
            if round(yaw4) < -180:
                yaw4 = yaw4 + 360
        else:
            
            rotation1_14= 0
            rotation1_4 = 180 +measuredangle4_1 - measuredangle1_4
            tempx4= tempx1 + measureddistance14*(math.cos((90-measuredangle1_4)*math.pi/180))
            tempy4= tempy1 + measureddistance14*(math.sin((90-measuredangle1_4)*math.pi/180))
            realx4 = tempx4*math.cos(coordinaterotation) + tempy4*math.sin(coordinaterotation)
            realy4 = (-1)*tempx4*math.sin(coordinaterotation) + tempy4*math.cos(coordinaterotation)
            yaw4 = yaw1 - (rotation1_4 + rotation1_14)
            if round(yaw4) < -180:
                yaw4 = yaw4 + 360



    else:
         if rotation1_1==180:
            rotation1_14= 180
            rotation1_4 = measuredangle4_1 - measuredangle1_4
            tempx4= tempx1 - measureddistance14*(math.cos((90-measuredangle1_4)*math.pi/180))
            tempy4= tempy1 - measureddistance14*(math.sin((90-measuredangle1_4)*math.pi/180))
            realx4 = tempx4*math.cos(coordinaterotation) + tempy4*math.sin(coordinaterotation)
            realy4 = (-1)*tempx4*math.sin(coordinaterotation) + tempy4*math.cos(coordinaterotation)
            yaw4 = yaw1 - (rotation1_4 + rotation1_14)
            if round(yaw4) < -180:
                yaw4 = yaw4 + 360
         else:
            
            rotation1_14= 0
            rotation1_4 = 180 +measuredangle4_1 - measuredangle1_4
            tempx4= tempx1 + measureddistance14*(math.cos((90-measuredangle1_4)*math.pi/180))
            tempy4= tempy1 + measureddistance14*(math.sin((90-measuredangle1_4)*math.pi/180))
            realx4 = tempx4*math.cos(coordinaterotation) + tempy4*math.sin(coordinaterotation)
            realy4 = (-1)*tempx4*math.sin(coordinaterotation) + tempy4*math.cos(coordinaterotation)
            yaw4 = yaw1 - (rotation1_4 + rotation1_14)
            if round(yaw4) < -180:
                yaw4 = yaw4 + 360
        


       

def createMissionFile():
    global ammsnumber1,ammsnumber2,ammsnumber3,ammsnumber4
    global realx1
    global realy1
    global realx2
    global realy2
    global realx3
    global realy3
    global realx4
    global realy4
    global realprimerx
    global realprimery
    global realseconderx
    global realsecondery
    global rotation1_1
    global rotation1_2
    global rotation1_3
    global rotation1_4
    global coordinaterotation
    global yaw1
    global yaw2
    global yaw3
    global yaw4
    calculatePositions1_2()
    calculatePositions1_3()
    calculatePositions1_4()
    print("X1= "+str(round(realx1))+" Y1= "+str(round(realy1))+" Yaw1= "+str(round(yaw1)))
    print("X2= "+str(round(realx2))+" Y2= "+str(round(realy2))+" Yaw2= "+str(round(yaw2)))
    print("X3= "+str(round(realx3))+" Y3= "+str(round(realy3))+" Yaw3= "+str(round(yaw3)))
    print("X4= "+str(round(realx4))+" Y4= "+str(round(realy4))+" Yaw4= "+str(round(yaw4)))
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        sys.exit
    filetext = str("1.  [DEVICE] id=AMMSHP-01-00%s; role=none; source=gps; location=(lat,lon,alt); orientation(yaw,pitch,roll); rotation=(%d,0,0); translation=(%.2f,%.2f,0);\n2.  [DEVICE] id=AMMSHP-01-00%s; role=none; source=gps; location=(lat,lon,alt); orientation(yaw,pitch,roll); rotation=(%d,0,0); translation=(%.2f,%.2f,0);\n3.  [DEVICE] id=AMMSHP-01-00%s; role=none; source=gps; location=(lat,lon,alt); orientation(yaw,pitch,roll); rotation=(%d,0,0); translation=(%.2f,%.2f,0);\n4.  [DEVICE] id=AMMSHP-01-00%s; role=none; source=gps; location=(lat,lon,alt); orientation(yaw,pitch,roll); rotation=(%d,0,0); translation=(%.2f,%.2f,0);"
                   % (ammsnumber1,round(yaw1),round(realx1)/100,round(realy1)/100,ammsnumber2,round(yaw2),round(realx2)/100,round(realy2)/100,ammsnumber3,round(yaw3),round(realx3)/100,round(realy3)/100,ammsnumber4,round(yaw4),round(realx4)/100,round(realy4)/100))
    file.write(filetext)
    file.close()
     
        

def cameraPrimerAlign():


    global targeticon1 
    _, frame = cap.read()
    
    frame = cv2.resize(frame, (320, 240), interpolation = cv2.INTER_LINEAR)
    rows, cols, _ = frame.shape
    xmedium = int(cols / 2)
    ymedium = int(rows / 2)

    
        
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

    if targeticon1 % 2 == 0:
        if targeticon1 > 0:
            setsystemButton.config(state='normal')
        pass
         
    else:
        cv2.line(frame, (xmedium, 0), (xmedium, 240), (0, 255, 0),2)
        for cnt in contours:

                
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center0 = (int(x),int(y))
            x_medium = int(x)
            radius = int(radius)
                
            if radius >=5:
                cv2.circle(frame,center0,radius,(0,255,0),2)
                cv2.line(frame, (x_medium,0), (x_medium, 480), (255, 0, 0),2)
                    
                    
            if  x_medium < xmedium+10 and x_medium > xmedium-10:       
                cv2.circle(frame, (300, 25), 7, (0, 255, 0),-1)
                cv2.putText(frame, 'READY', (237,47), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,255,0), 1)
                text3.delete("1.0","end")
                text3.insert(END, "READY FOR MEASUREMENT")
                setsystemButton.config(state='normal')
                    
            else:

                cv2.circle(frame, (300, 25), 7, (0, 0, 255),-1)
                cv2.putText(frame, 'NOT ALIGNED', (220,47), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                setsystemButton.config(state='disabled')
                    
                if x_medium >= xmedium+5:
            
                    cv2.putText(frame, '>', (15,128), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                    text3.delete("1.0","end")
                    text3.insert(END, "CLICK RIGHT BUTTONS")

                else :
                        
                    cv2.putText(frame, '<', (287,128), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                    text3.delete("1.0","end")
                    text3.insert(END, "CLICK LEFT BUTTONS")
                
    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100,cameraPrimerAlign)

    
threading.Thread(target = cameraPrimerAlign).start()


def zoom1():
    zoomWindow1 = Toplevel(root)
    zoomWindow1.geometry("650x490")
    zoomWindow1.title('Zoom x 2 - Primer Camera')
    
    def cameraPrimerZoom():
        
        zoom1 = Label(zoomWindow1, borderwidth=5, relief="sunken")
        zoom1.place(x=0,y=0)

        _, frame = cap.read()
        rows, cols, _ = frame.shape
        xmedium = int(cols / 2)
        ymedium = int(rows / 2)

        cv2.line(frame, (xmedium, 0), (xmedium, 480), (0, 255, 0),2)
            
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

                
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center0 = (int(x),int(y))
            x_medium = int(x)
            radius = int(radius)
                
            if radius >=5:
                cv2.circle(frame,center0,radius,(0,255,0),2)
                cv2.line(frame, (x_medium,0), (x_medium, 480), (255, 0, 0),2)
                    
                    
            if  x_medium < xmedium+10 and x_medium > xmedium-10:       
                cv2.circle(frame, (600, 50), 15, (0, 255, 0),-1)
                cv2.putText(frame, 'READY', (570,95), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,255,0), 1)
                text3.delete("1.0","end")
                text3.insert(END, "READY FOR MEASUREMENT")
                    
            else:

                cv2.circle(frame, (600, 50), 15, (0, 0, 255),-1)
                cv2.putText(frame, 'NOT ALIGNED', (540,95), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
               
                    
                if x_medium >= xmedium+5:
            
                    cv2.putText(frame, '>', (30,255), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                    text3.delete("1.0","end")
                    text3.insert(END, "CLICK RIGHT BUTTONS")

                else :
                        
                    cv2.putText(frame, '<', (595,255), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                    text3.delete("1.0","end")
                    text3.insert(END, "CLICK LEFT BUTTONS")
                    
        
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        zoom1.imgtk = imgtk
        zoom1.configure(image=imgtk)
        zoom1.after(100,cameraPrimerZoom)

    threading.Thread(target = cameraPrimerZoom).start()

def zoom2():
    zoomWindow2 = Toplevel(root)
    zoomWindow2.geometry("650x490")
    zoomWindow2.title('Zoom x 2 - Seconder Camera')
    
    def cameraSeconderZoom():
        
        zoom2 = Label(zoomWindow2, borderwidth=5, relief="sunken")
        zoom2.place(x=0,y=0)

        _, frame = cap_2.read()
        rows, cols, _ = frame.shape
        xmedium = int(cols / 2)
        ymedium = int(rows / 2)

        cv2.line(frame, (xmedium, 0), (xmedium, 480), (0, 255, 0),2)
            
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

                
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center0 = (int(x),int(y))
            x_medium = int(x)
            radius = int(radius)
                
            if radius >=5:
                cv2.circle(frame,center0,radius,(0,255,0),2)
                cv2.line(frame, (x_medium,0), (x_medium, 480), (255, 0, 0),2)
                    
                    
            if  x_medium < xmedium+10 and x_medium > xmedium-10:       
                cv2.circle(frame, (600, 50), 15, (0, 255, 0),-1)
                cv2.putText(frame, 'READY', (570,95), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,255,0), 1)
                text3.delete("1.0","end")
                text3.insert(END, "READY FOR MEASUREMENT")
                    
            else:

                cv2.circle(frame, (600, 50), 15, (0, 0, 255),-1)
                cv2.putText(frame, 'NOT ALIGNED', (540,95), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                
                    
                if x_medium >= xmedium+5:
            
                    cv2.putText(frame, '>', (30,255), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                    text3.delete("1.0","end")
                    text3.insert(END, "CLICK RIGHT BUTTONS")

                else :
                        
                    cv2.putText(frame, '<', (595,255), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                    text3.delete("1.0","end")
                    text3.insert(END, "CLICK LEFT BUTTONS")
                    
        
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        zoom2.imgtk = imgtk
        zoom2.configure(image=imgtk)
        zoom2.after(100,cameraSeconderZoom)

    threading.Thread(target = cameraSeconderZoom).start()
   

def cameraSeconderAlign():

    global targeticon2
    _, frame = cap_2.read()
    
    frame = cv2.resize(frame, (320, 240), interpolation = cv2.INTER_LINEAR)
    rows, cols, _ = frame.shape
    xmedium = int(cols / 2)
    ymedium = int(rows / 2)

        
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


    if targeticon2 % 2 == 0:
        if targeticon2 > 0:
            setsystemButton.config(state='normal')
        pass

    else:

        cv2.line(frame, (xmedium, 0), (xmedium, 240), (0, 255, 0),2)
        for cnt in contours:

                
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center0 = (int(x),int(y))
            x_medium = int(x)
            radius = int(radius)

            if radius >=5:
                    cv2.circle(frame,center0,radius,(0,255,0),2)
                    cv2.line(frame, (x_medium,0), (x_medium, 480), (255, 0, 0),2)

                            
            if  x_medium < xmedium+10 and x_medium > xmedium-10:       
                    cv2.circle(frame, (300, 25), 7, (0, 255, 0),-1)
                    cv2.putText(frame, 'READY', (237,47), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,255,0), 1)
                    text7.delete("1.0","end")
                    text7.insert(END, "READY FOR MEASUREMENT")
                    setsystemButton.config(state='normal')  
            else:

                    cv2.circle(frame, (300, 25), 7, (0, 0, 255),-1)
                    cv2.putText(frame, 'NOT ALIGNED', (220,47), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                    setsystemButton.config(state='disabled')
                        
                    if x_medium >= xmedium+5:
                
                        cv2.putText(frame, '>', (15,128), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                        text7.delete("1.0","end")
                        text7.insert(END, "CLICK RIGHT BUTTONS")

                    else :
                            
                        cv2.putText(frame, '<', (287,128), cv2.FONT_HERSHEY_TRIPLEX, 1, (100,255,0), 2)
                        text7.delete("1.0","end")
                        text7.insert(END, "CLICK LEFT BUTTONS")

                
    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain2.imgtk = imgtk
    lmain2.configure(image=imgtk)
    lmain2.after(100,cameraSeconderAlign)

    
threading.Thread(target = cameraSeconderAlign).start()

         

def rightHighMovement():
               
        global position
        position = position + 30
        if position < 0:
            position = 360 - position
        elif position > 360:
            position = position - 360
        ser.write(str(position).encode())
        

def leftHighMovement():
               
        global position
        position = position - 30
        if position < 0:
            position = 360 - position
        elif position > 360:
            position = position - 360
        ser.write(str(position).encode())
        

def rightMidMovement():
               
        global position
        position = position + 10
        if position < 0:
            position = 360 - position
        elif position > 360:
            position = position - 360
        ser.write(str(position).encode())
        

def leftMidMovement():
               
        global position
        position = position - 10
        if position < 0:
            position = 360 - position
        elif position > 360:
            position = position - 360
        ser.write(str(position).encode())
        

def rightLowMovement():
               
        global position
        position = position + 1
        if position <= 0:
            position = 360 - position
        elif position > 360:
            position = position - 360
        ser.write(str(position).encode())
        

def leftLowMovement():
               
        global position
        position = position - 1
        if position < 0:
            position = 360 - position
        elif position > 360:
            position = position - 360
        ser.write(str(position).encode())
        

def goRef():
               
        global position
        position = 180
        ser.write(str(position).encode())

def goZero():
               
        global position
        position = 0
        ser.write(str(position).encode())

def targetAlign():

        global position
        ser.write(str(position).encode())


def rightHighMovement1():
               
        global position1
        position1 = position1 + 30
        if position1 < 0:
            position1 = 360 - position1
        elif position1 > 360:
            position1 = position1 - 360
        ser_2.write(str(position1).encode())
        

def leftHighMovement1():
               
        global position1
        position1 = position1 - 30
        if position1 < 0:
            position1 = 360 - position1
        elif position1 > 360:
            positio1n = position1 - 360
        ser_2.write(str(position1).encode())
        

def rightMidMovement1():
               
        global position1
        position1 = position1 + 10
        if position1 < 0:
            position1 = 360 - position1
        elif position1 > 360:
            position1 = position1 - 360
        ser_2.write(str(position1).encode())
        

def leftMidMovement1():
               
        global position1
        position1 = position1 - 10
        if position1 < 0:
            position1 = 360 - position1
        elif position1 > 360:
            position1 = position1 - 360
        ser_2.write(str(position1).encode())
        

def rightLowMovement1():
               
        global position1
        position1 = position1 + 1
        if position1 <= 0:
            position1 = 360 - position1
        elif position1 > 360:
            position1 = position1 - 360
        ser_2.write(str(position1).encode())
        

def leftLowMovement1():
               
        global position1
        position1 = position1 - 1
        if position1 < 0:
            position1 = 360 - position1
        elif position1 > 360:
            position1 = position1 - 360
        ser_2.write(str(position1).encode())
        

def goRef1():
               
        global position1
        position1 = 180
        ser_2.write(str(position1).encode())

def goZero1():
               
        global position1
        position1 = 0
        ser_2.write(str(position1).encode())

def targetAlign1():

        global position1
        ser_2.write(str(position1).encode())

def targeting1():

    global targeticon1
    targeticon1 = targeticon1 + 1

def targeting2():

    global targeticon2
    targeticon2 = targeticon2 + 1


rhButton = Button(frame1, text = ">>>", command = rightHighMovement)
rhButton.pack(side=RIGHT)

lhButton = Button(frame1, text = "<<<", command = leftHighMovement)
lhButton.pack(side=LEFT)

rmButton = Button(frame1, text = ">>", command = rightMidMovement)
rmButton.pack(side=RIGHT)

lmButton = Button(frame1, text = "<<", command = leftMidMovement)
lmButton.pack(side=LEFT)

rlButton = Button(frame1, text = ">", command = rightLowMovement)
rlButton.pack(side=RIGHT)

llButton = Button(frame1, text = "<", command = leftLowMovement)
llButton.pack(side=LEFT)

zeroButton = Button(frame2, text = "Go to Zero", command = goZero, width = 20)
zeroButton.pack()

refButton = Button(frame2, text = "Go Reference", command = goRef, width = 20)
refButton.pack()

targetButton = Button(frame2, text = "Small Target Alignment", command = targetAlign, width = 20)
targetButton.pack()

rhButton2 = Button(frame3, text = ">>>", command = rightHighMovement1)
rhButton2.pack(side=RIGHT)

lhButton2 = Button(frame3, text = "<<<", command = leftHighMovement1)
lhButton2.pack(side=LEFT)

rmButton2 = Button(frame3, text = ">>", command = rightMidMovement1)
rmButton2.pack(side=RIGHT)

lmButton2 = Button(frame3, text = "<<", command = leftMidMovement1)
lmButton2.pack(side=LEFT)

rlButton2 = Button(frame3, text = ">", command = rightLowMovement1)
rlButton2.pack(side=RIGHT)

llButton2 = Button(frame3, text = "<", command = leftLowMovement1)
llButton2.pack(side=LEFT)

zeroButton2 = Button(frame4, text = "Go to Zero", command = goZero1, width = 20)
zeroButton2.pack()

refButton2 = Button(frame4, text = "Go Reference", command = goRef1, width = 20)
refButton2.pack()

targetButton2 = Button(frame4, text = "Small Target Alignment", command = targetAlign1, width = 20)
targetButton2.pack()

zoomButtonimage = ImageTk.PhotoImage(file='zoom.png')
zoombtnLabel=Label(image=zoomButtonimage)

targetButtonimage = ImageTk.PhotoImage(file='targeticon.png')
targetbtnLabel = Label(image=targetButtonimage)

frame111=Frame(root)
frame111.place(x=380,y=310)

frame333=Frame(root)
frame333.place(x=380,y=675)

frame122=Frame(root)
frame122.place(x=120,y=310)

frame322=Frame(root)
frame322.place(x=120,y=675)

zoomButton1 = Button(frame111,image=zoomButtonimage , command = zoom1,borderwidth=0,bg="#263037")
zoomButton1.pack()

zoomButton2 = Button(frame333, image=zoomButtonimage, command = zoom2,borderwidth=0,bg="#1C558E")
zoomButton2.pack()

targeticonButton1 = Button(frame122,image=targetButtonimage , command = targeting1,borderwidth=0,bg="#1F4265")
targeticonButton1.pack()

targeticonButton2 = Button(frame322,image=targetButtonimage , command = targeting2,borderwidth=0,bg="#1C558E")
targeticonButton2.pack()


missonfileButton = Button(frame33, text = "CREATE MISSION FILE",width = 20, height = 5, command = lambda:[createMissionFile(),bar()])
missonfileButton.pack()

setsystemButton = Button(frame11, text = "SAVE MEASUREMENT",width = 20,height = 5, command = saveMeasurements)
setsystemButton.pack()

manualButton = Button(root,text="MANUAL CALCULATION", command=manualCalculation,width=40,height=5, relief="groove", borderwidth=5)
manualButton.place(x=1200,y=550)
manualButton.config(state='disabled')


disableButtons()



time.sleep(1)

root.mainloop()
        
    




