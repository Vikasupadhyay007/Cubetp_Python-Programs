from tkinter import *
from PIL import Image, ImageTk # in terminal type: pip install pillow

root = Tk()

# PNG picture import 

photo = PhotoImage(file = "wavelet logo.png")

label = Label(root, image = photo)
label.pack()

# JPG picture import

#image = Image.open("B_01.jpg")
#photo = ImageTk.PhotoImage(image)

#label = Label(image = photo)
label.pack()

root.mainloop()