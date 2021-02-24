from tkinter import *

root = Tk()

photo = PhotoImage(file = "wavelet logo.png")
label = Label(root, image = photo)
label.pack()

root.mainloop()