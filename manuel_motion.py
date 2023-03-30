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


#arduinoSerialData = serial.Serial("COM7", '9600', timeout=2) 
#ser = serial.Serial("COM5", '9600', timeout=2)
#ser_2 = serial.Serial("COM6", '9600', timeout=2)

count = 0
listB = [1]
listA = []
position = 180
position1 = 180
ang1=0
i = 1
flt = 0
ang = 0
distance = 0
targeticon1=0
targeticon2=0

cap = cv2.VideoCapture(0)
cap_2 = cv2.VideoCapture('aclogus.mp4')
    
root = Tk()
root.title('Mission File Creator')
root.geometry('1600x900')
root.bind('<Escape>', lambda e: root.quit())




background_image=ImageTk.PhotoImage(Image.open("Breeze.png"))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


options = [ ' AMMS 1 - AMMS 2 ', ' AMMS 1 - AMMS 3 ', ' AMMS 1 - AMMS 4 ']

clicked = StringVar()
clicked.set(options[0])



combotext=Label(root,text = "Choose # AMMS", bg="#263037", fg="white")
combotext.place(x=450,y=165)

mycombo = ttk.Combobox(root, value = options)
mycombo.current(0)
mycombo.place(x=450,y=190)


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
pageLabel.place(x=1300, y = 680)

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


Pammsimage= ImageTk.PhotoImage(file="FirstAMMS (2).png")
Sammsimage= ImageTk.PhotoImage(file="SecondAMMS (2).png")
Tammsimage= ImageTk.PhotoImage(file="ThirdAMMS (2).png")
Fammsimage= ImageTk.PhotoImage(file="ThirdAMMS (2).png")


gridFrame = Frame(root,borderwidth=5,relief = "sunken")
canvas1 = Canvas(gridFrame, width = 600, height=500)
canvas1.pack()

x1,x2,x3,x4 = 300, 300, 100, 500
y1,y2,y3,y4 = 400, 100, 250, 250

im1=canvas1.create_image(x1,y1,image=Pammsimage)
im2=canvas1.create_image(x2,y2,image=Sammsimage)
im3=canvas1.create_image(x3,y3,image=Tammsimage)
im4=canvas1.create_image(x4,y4,image=Fammsimage)
lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))
linTN=canvas1.create_line(x1-50, y1, x2-50, y2,arrow=LAST, fill="blue")
linTE=canvas1.create_line(x1-50, y1, abs(y1-y2)+x1-50, abs(x1-x2)+y1, arrow=LAST, fill="blue")
linTN1=canvas1.create_line(x1-50, y1, x2, y2, fill="red")
linTN2=canvas1.create_line(x1-50, y1, x3, y3, fill="red")
linTN3=canvas1.create_line(x1-50, y1, x4, y4, fill="red")
labelNorth = Label(canvas1, text="N")
labelNorth.place(x=(x1-50+x2-50)/2-7,y=(y1+y2)/2)
gridFrame.pack()    
gridFrame.pack_forget()
    
def openAmms(e):
    global x1,x2,x3,x4
    global y1,y2,y3,y4
   

    gridFrame.place(x=675,y=160)
    """canvas1.delete(im1)
    canvas1.delete(im2)
    canvas1.delete(im3)
    canvas1.delete(im4)
    canvas1.delete(lin1)
    canvas1.delete(lin2)
    canvas1.delete(lin3)
            
    im1=canvas1.create_image(x1,y1,image=Pammsimage)
    im2=canvas1.create_image(x2,y2,image=Sammsimage)
    im3=canvas1.create_image(x3,y3,image=Tammsimage)
    im4=canvas1.create_image(x4,y4,image=Fammsimage)
    lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
    lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
    lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))"""

    def rotate (degrees):
        global img
        img = img.rotate (degrees)
        global tkimg
        tkimg = ImageTk.PhotoImage (img)
        canvas1.create_image (200,200, image = tkimg, tags = "img")
        
#img = Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\FirstAMMS (2).png")
#rotate (0)           

        

    
def closeAmms(e):

    gridFrame.place_forget()

pageLabel.bind("<Enter>",openAmms)
pageLabel.bind("<Leave>",closeAmms)




def bar():

    response = messagebox.askyesno("Alert", "Do you want to create a mission file?")
    if response == False:
        return ()
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
        time.sleep(0.1)
        
        
    var2.set('Getting Primer Servo Angle')
    root.update_idletasks()
    time.sleep(0.25)
    
    var2.set('Getting Seconder Servo Angle')
    root.update_idletasks()
    time.sleep(0.25)
    
    for i in range(20,41):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.1)
    
    var2.set('Getting Distance Data')
    root.update_idletasks()
    time.sleep(0.25) 

    var2.set('Waiting for Lidar Measurement')
    root.update_idletasks()
    time.sleep(0.25)

    for i in range(40,51):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.1)
    
    var2.set('Checking Sensor Data')
    root.update_idletasks()
    time.sleep(0.25)

    var2.set('Sensor Data Validated')
    root.update_idletasks()
    time.sleep(0.25)

    for i in range(50,61):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.1)
    

    var2.set('Generating Mission File')
    root.update_idletasks()
    time.sleep(0.25)

    var2.set('Writing Points and Angles')
    root.update_idletasks()
    time.sleep(0.25)
  
    for i in range(60,81):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.1)

        
    var2.set('Mission File Is Ready')
    root.update_idletasks()
    time.sleep(0.25) 
    for i in range(80,101):
        progress['value'] = i
        percent="Progress %"+str(i)
        i= i + 1
        root.update_idletasks()
        var.set(percent)
        time.sleep(0.1)
        
    messagebox.showinfo("Info!", "Completed. Mission file is saved to dekstop!")
    progress.destroy()
    newWindow.destroy()


def readDistance():
    global distance
    while True:
        a = arduinoSerialData.readline()        
        string_k = a.decode('utf-8')   
        stringk = string_k.rstrip() 
        distance = int(stringk)
        text1.delete("1.0","end")
        text1.insert(END, "DISTANCE : " + stringk)
        text5.delete("1.0","end")
        text5.insert(END, "DISTANCE : " + stringk)

#threading.Thread(target = readDistance).start()
    
    

def readPrimerAngle():
    global flt
    while True:
        b = ser.readline()        
        string_n = b.decode()   
        string = string_n.rstrip() 
        flt = int(string)
        text2.delete("1.0","end")
        text2.insert(END, "1st ANGLE : "+ string)

        
#threading.Thread(target = readPrimerAngle).start()
    



def readSeconderAngle():
    global ang
    while True:
        b = ser_2.readline()        
        string_n = b.decode()   
        string = string_n.rstrip() 
        ang = int(string)
        text6.delete("1.0","end")
        text6.insert(END, "2nd ANGLE : "+ string)

#threading.Thread(target = readSeconderAngle).start()
    


    
        

def cameraPrimerAllign():
   
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

    if targeticon1 % 2 == 1:

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
                    
            else:

                cv2.circle(frame, (300, 25), 7, (0, 0, 255),-1)
                cv2.putText(frame, 'NOT ALLIGNED', (220,47), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                
                    
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
    lmain.after(100,cameraPrimerAllign)

    
threading.Thread(target = cameraPrimerAllign).start()


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
                cv2.putText(frame, 'NOT ALLIGNED', (540,95), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                
                    
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
                cv2.putText(frame, 'NOT ALLIGNED', (540,95), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                
                    
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
   

def cameraSeconderAllign():

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


    if targeticon2 % 2 == 1:
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
                        
            else:

                    cv2.circle(frame, (300, 25), 7, (0, 0, 255),-1)
                    cv2.putText(frame, 'NOT ALLIGNED', (220,47), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0,0,255), 1)
                    
                        
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
    lmain2.after(10,cameraSeconderAllign)

    
threading.Thread(target = cameraSeconderAllign).start()

         

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

def targetAllign():

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

def targetAllign1():

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

targetButton = Button(frame2, text = "Small Target Allignment", command = targetAllign, width = 20)
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

targetButton2 = Button(frame4, text = "Small Target Allignment", command = targetAllign1, width = 20)
targetButton2.pack()

zoomButton = ImageTk.PhotoImage(file='zoom.png')
zoombtnLabel=Label(image=zoomButton)

targetButton = ImageTk.PhotoImage(file='targeticon.png')
targetbtnLabel=Label(image=targetButton)

frame111=Frame(root)
frame111.place(x=380,y=310)

frame333=Frame(root)
frame333.place(x=380,y=675)

frame122=Frame(root)
frame122.place(x=120,y=310)

frame322=Frame(root)
frame322.place(x=120,y=675)

zoomButton1 = Button(frame111,image=zoomButton , command = zoom1,borderwidth=0,bg="#263037")
zoomButton1.pack()

zoomButton2 = Button(frame333, image=zoomButton, command = zoom2,borderwidth=0,bg="#1C558E")
zoomButton2.pack()

targetButton1 = Button(frame122,image=targetButton , command = targeting1,borderwidth=0,bg="#1F4265")
targetButton1.pack()

targetButton2 = Button(frame322,image=targetButton , command = targeting2,borderwidth=0,bg="#1C558E")
targetButton2.pack()


angle2Button = Button(frame33, text = "CREATE MISSION FILE",width = 20, height = 5, command = bar)
angle2Button.pack()

setsystemButton = Button(frame11, text = "START",width = 20, command = bar)
setsystemButton.pack()

fixButton = Button(frame11, text = "MEASURE",width = 20, command = bar)
fixButton.pack()





time.sleep(1)

root.mainloop()
        
    




