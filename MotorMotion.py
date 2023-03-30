import serial
from tkinter import*
import numpy as np

root = Tk()
listB = [1]
    

ser = serial.Serial("COM6", '9600', timeout=2)

position = 180

"""for j in range(0,100):
        b = ser.readline()        
        string_n = b.decode()   
        string = string_n.rstrip() 
        flt = int(string)"""
        
         

def rightHighMovement():
               
        global position
        position = position + 30
        ser.write(str(position).encode())
        print(position)

def leftHighMovement():
               
        global position
        position = position - 30
        ser.write(str(position).encode())
        print(position)

def rightMidMovement():
               
        global position
        position = position + 10
        ser.write(str(position).encode())
        print(position)

def leftMidMovement():
               
        global position
        position = position - 10
        ser.write(str(position).encode())
        print(position)

def rightLowMovement():
               
        global position
        position = position + 1
        ser.write(str(position).encode())
        print(position)

def leftLowMovement():
               
        global position
        position = position - 1
        ser.write(str(position).encode())
        print(position)

def goRef():
               
        global position
        position = 180
        ser.write(str(position).encode())
        print(position)
                
        
        

rhButton = Button(root, text = ">>>", command = rightHighMovement)
rhButton.pack()

lhButton = Button(root, text = "<<<", command = leftHighMovement)
lhButton.pack()

rmButton = Button(root, text = ">>", command = rightMidMovement)
rmButton.pack()

lmButton = Button(root, text = "<<", command = leftMidMovement)
lmButton.pack()

rlButton = Button(root, text = ">", command = rightLowMovement)
rlButton.pack()

llButton = Button(root, text = "<", command = leftLowMovement)
llButton.pack()

refButton = Button(root, text = "Go Reference", command = goRef)
refButton.pack()



root.mainloop()
                



    
          
                
        
        

    
            
        
       

       

    





