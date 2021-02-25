from tkinter import *

root = Tk()

root.minsize(50, 50) # it will not small than this
root.maxsize(250, 150)
canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill = "red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill = "green")

canvas.delete(redLine)
canvas.delete(ALL)

root.mainloop()