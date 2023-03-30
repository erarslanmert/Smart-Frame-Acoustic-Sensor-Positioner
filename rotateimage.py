import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk ()
root.geometry("1600x900")
canvas = tk.Canvas (root,width=800,height=800, bg = "gray")
canvas.pack ()
def rotate (degrees):
    global img
    img = img.rotate (degrees)
    global tkimg
    tkimg = ImageTk.PhotoImage (img)
    canvas.create_image (200,200, image = tkimg, tags = "img")
img = Image.open(r"C:\Users\Quantum1\Desktop\QEPC\Inner Projects\SmartFrame\ThirdAMMS (2).png")
rotate (0)
def pressed (event):
    rotate (45)
canvas.tag_bind ("img", "<ButtonPress-1>", pressed)
root.mainloop ()
