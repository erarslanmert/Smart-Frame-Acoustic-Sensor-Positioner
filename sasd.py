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
from tkinter.ttk import Progressbar
from tkinter import messagebox


root = Tk()
root.title('Mission File Creator')
root.geometry('1600x900')

background_image=ImageTk.PhotoImage(Image.open("Breeze.png"))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

imgPrimer=ImageTk.PhotoImage(Image.open("Configimage.png"))
imgLabel = Label(root,image=imgPrimer,borderwidth=5,relief="groove")
imgLabel.pack(side=BOTTOM)


imgamms=ImageTk.PhotoImage(Image.open("PAMMS.png"))
ammsLabel = Label(root,image=imgamms)
ammsLabel.pack()    
ammsLabel.pack_forget()
    
def openAmms(e):
    ammsLabel.pack()
def closeAmms(e):
    ammsLabel.pack_forget()

imgLabel.bind("<Enter>",openAmms)
imgLabel.bind("<Leave>",closeAmms)
