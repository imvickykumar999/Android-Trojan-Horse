
from tkinter import *

root = Tk()
var = IntVar()

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
