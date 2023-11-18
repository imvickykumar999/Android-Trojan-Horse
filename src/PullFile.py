
from tkinter import *
import os

root = Tk()
var = StringVar()

Rframe = Frame(root)
Rframe.pack(side=TOP)

Bframe = Frame(root)
Bframe.pack(side=TOP, expand=True)

root.geometry("300x600")
root.title("SDcard Tree")

path = '/sdcard/Download/Telegram/'
output = os.popen(f'adb shell ls -p {path}')
output = output.read().split('\n')[:-1]

event = StringVar()
entry = Entry(root, textvariable = event)

def on_click():
   name = entry.get()
   os.system(f'adb pull "{name}"')

button = Button(root, text="Pull File", command=on_click)
button.pack(side = TOP)

def sel():
   global path
   subpath = path + str(var.get())
   print(subpath)

   if str(var.get())[-1] == '/':
      output = os.popen(f'adb shell ls -p {subpath}')
      output = output.read().split('\n')[:-1]
      print(output)

   else:
      event.set(subpath)

def bullets(output):
   for widget in Rframe.winfo_children():
      widget.destroy() 

   for i in output:
      R1 = Radiobutton(
         Rframe, 
         text=i, 
         value=i, 
         command=sel,
         variable=var 
      )
      var.set(None)
      R1.pack(anchor = 's')

Button(
   root, 
   pady=5,
   padx=10, 
   text=path, 
   bg="light green",
   command=lambda: bullets(output)
).pack()

root.mainloop()
