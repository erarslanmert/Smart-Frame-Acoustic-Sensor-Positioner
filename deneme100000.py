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
import sys
sys.setrecursionlimit(100) # 10000 is an example, try with different values
root = Tk()
root.title('Mission File Creator')
root.geometry('1600x900')

pageimage = ImageTk.PhotoImage(file="Cartop.png")
pageLabel = Label(root, image=pageimage)
pageLabel.place(x=1300, y = 680)




Pammsimage= ImageTk.PhotoImage(file="FirstAMMS.png")
Sammsimage= ImageTk.PhotoImage(file="SecondAMMS.png")
Tammsimage= ImageTk.PhotoImage(file="ThirdAMMS.png")
Fammsimage= ImageTk.PhotoImage(file="ThirdAMMS.png")

gridFrame = Frame(root,borderwidth=5,relief = "sunken")
canvas1 = Canvas(gridFrame, width = 500, height=400)
canvas1.pack()

x1,x2,x3,x4 = 100, 400, 250, 250
y1,y2,y3,y4 = 200, 200, 50, 350

im1=canvas1.create_image(x1,y1,image=Pammsimage)
im2=canvas1.create_image(x2,y2,image=Sammsimage)
im3=canvas1.create_image(x3,y3,image=Tammsimage)
im4=canvas1.create_image(x4,y4,image=Fammsimage)
lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))
gridFrame.pack()    
gridFrame.pack_forget()
    
def openAmms(e):
    global x1,x2,x3,x4 
    global y1,y2,y3,y4
    gridFrame.place(x=775,y=260)
    time.sleep(0.1)
    canvas1.delete(im1)
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
    lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))
            
    x2=x2-2
    x3=x3-1
    x4=x4-1
    y3=y3+1
    y4=y4-1

    
        
    
        

    
def closeAmms(e):
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    global im1,im2,im3,im4,lin1,lin2,lin3
    
    """x1,x2,x3,x4 = 100, 400, 250, 250
    y1,y2,y3,y4 = 200, 200, 50, 350

    im1=canvas1.create_image(x1,y1,image=Pammsimage)
    im2=canvas1.create_image(x2,y2,image=Sammsimage)
    im3=canvas1.create_image(x3,y3,image=Tammsimage)
    im4=canvas1.create_image(x4,y4,image=Fammsimage)
    lin1=canvas1.create_line(x1, y1, x2, y2, dash=(4, 2))
    lin2=canvas1.create_line(x1, y1, x3, y3, dash=(4, 2))
    lin3=canvas1.create_line(x1, y1, x4, y4, dash=(4, 2))"""

    gridFrame.place_forget()

pageLabel.bind("<Enter>",openAmms)
pageLabel.bind("<Leave>",closeAmms)
    
