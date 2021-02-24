from tkinter import *

from PIL import ImageTk, Image

root = Tk()
canvas = Canvas(root, width = 300, height = 160)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\CubeTechBiz\\Desktop\\NX 10 picture\\image.png"))

canvas.create_image(0, 0, anchor = NW, image = image)
canvas.pack()

root.mainloop()