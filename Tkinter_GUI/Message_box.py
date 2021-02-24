from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo('Window Title', 'Cube software is under progress..')

answer = tkinter.messagebox.askquestion('Warning', 'Do you want to cancle?')

if answer == 'yes':
    print('-_-')

root.mainloop()
