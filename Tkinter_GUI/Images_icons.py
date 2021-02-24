from tkinter import *

root = Tk()

photo = PhotoImage(file = "sigma.png")
label = Label(root, image = photo)
label.pack()

root.mainloop()