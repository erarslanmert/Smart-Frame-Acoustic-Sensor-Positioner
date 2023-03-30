


from tkinter import*
import PIL
from PIL import Image,ImageTk

t = Tk()
t.title("Transparency")

frame = Label(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="PAMMSTR.png")
canvas.create_image(150, 150, image=photoimage)

t.mainloop()
