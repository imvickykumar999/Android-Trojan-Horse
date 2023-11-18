
from tkinter import *
import os

root = Tk()
var = StringVar()

path = '/sdcard/Download/'
output = os.popen(f'adb shell ls -p {path}')
output = output.read().split('\n')[:-1]

event = StringVar()
btn = Entry(root, textvariable = event)

btn.insert(0, path)
btn.pack()

def sel():
   global path
   if str(var.get())[-1] == '/':
      event.set(path + str(var.get()))

      subpath = str(var.get())
      path += subpath
      output = os.popen(f'adb shell ls -p {path}')
      output = output.read().split('\n')[:-1]

      subdir = str(var.get()).split('/')[0] + '/'
      submit = Button(root, text=subdir, command=lambda: bullets(output))
      submit.pack(anchor = N)
   else:
      event.set(str(var.get()))

def bullets(output):   
   for i in output:
      R1 = Radiobutton(root, text=i, variable=var, value=i, command=sel)
      var.set(None)
      R1.pack(anchor = W)

submit = Button(root, text="sdcard/", command=lambda: bullets(output))
submit.pack()
root.mainloop()
