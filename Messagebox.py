from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('learn')

def open():
    top = Toplevel()
    top.title('second window')
    response = messagebox.askyesno("this", "Hello")
    btn2 = Button(top, text='close window', command=top.destroy).pack()

Btn = Button(root, text="Open second window", command=open).pack()

mainloop()