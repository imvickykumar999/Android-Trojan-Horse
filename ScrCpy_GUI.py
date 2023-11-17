
from tkinter import *
import os, json, threading
from tkinter import filedialog
from tkinterweb import HtmlFrame
from ppadb.client import Client as AdbClient

ip = input('''
----------------------------------------
Press `CTRL + PAUSE/BREAK` keys to exit.

Press ENTER for default IP 
    192.168.0.103
----------------------------------------

Paste IP Address of Device : ''')


def task1():
    global ip
    print()

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

    if ip == '':
        ip = '192.168.0.102'

    while True:
        print()
        os.system(f'scrcpy --tcpip={ip}')


def task2():
    print()

    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

    def power():
        os.system(f'adb -s {ip} shell input keyevent 26')

    def volup():
        os.system(f'adb -s {ip} shell input keyevent 24')

    def voldown():
        os.system(f'adb -s {ip} shell input keyevent 25')

    def submit(x):
        try: 
            if x == '': 
                os.system('src/keyevents.json')
            else:
                os.system(f'adb -s {ip} shell input keyevent {x}')
        except Exception as e: 
            print(e)

    def fun():
        key = num_list.get(num_list.curselection()[0])
        key = key.split(' : ')[0]
        os.system(f'adb -s {ip} shell input keyevent {key}')

    def UploadAction(push_stop_path='Download/Telegram/static/'):
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.device(f'{ip}:5555')

        push_start_file = filedialog.askopenfilename()
        file = os.path.basename(push_start_file)

        if file.split('.')[-1] in ['apk', ]:
            print(f'\n>>> Installing {file}...')
            device.install(push_start_file)
            print(f'\n>>>\tInstalled.')

        else:
            print(f'\n>>> Sending {file} ...')
            device.push(f"{push_start_file}", f"/sdcard/{push_stop_path}/{file}")
            print(f'\n>>>\tSent.')
 
    while True:
        root = Tk()
        root.geometry("300x600")
        root.title("ScrCpy GUI")
        root.config(bg="gray")

        try:
            bg = PhotoImage(file = "src/wallpaper.png") 
            label = Label(root, image = bg) 
            label.place(x = 0, y = 0) 

        except:
            frame = HtmlFrame(root)
            frame.load_website("https://github.com/imvickykumar999/ADB-Screen-Copy/blob/main/Projects/TkinterGUI/Executable/wallpaper.png?raw=true")
            frame.pack(fill="both", expand=True)

        try:
            rely3 = 0.7
            rely4 = 0.8
            rely5 = 0.9

            num_list = Listbox(root, height=15, width=30)
            with open('src/keyevents.json') as f:
                data = json.load(f)

            for i in data['key_events']:
                j = data['key_events'][i]
                k = j.split('adb shell input keyevent ')
                num_list.insert(k[1], f'{k[1]} : {i.split("key_")[1]}')

            num_list.place(relx=0.5, rely=0.4, anchor='center')
            get_num_btn = Button(root, bg='green', text="Run ADB", command=fun)
            get_num_btn.place(relx=0.5, rely=0.55, anchor='center')

        except:
            rely3 = 0.5
            rely4 = 0.6
            rely5 = 0.8

            event = StringVar()
            btn1 = Entry(root, textvariable = event)

            btn1.insert(0, '209') # Open Music App
            btn1.place(relx=0.5, rely=0.2, anchor='center')

            btn2 = Button(root, bg='green', text = 'Keyevent', command = lambda: submit(event.get()))
            btn2.place(relx=0.5, rely=0.3, anchor='center')

        push_stop_path='Download/Telegram/static/'
        upload = Button(root, text='Send File', command = lambda: UploadAction(push_stop_path))
        upload.place(relx=0.5, rely=0.1, anchor='center')

        btn3 = Button(root, text="Volume Up", command=volup)
        btn3.place(relx=0.5, rely=rely3, anchor='center')

        btn4 = Button(root, text="Volume Down", command=voldown)
        btn4.place(relx=0.5, rely=rely4, anchor='center')
        
        btn5 = Button(root, bg='red', text="Power ON / OFF", command=power)
        btn5.place(relx=0.5, rely=rely5, anchor='center')
        root.mainloop()


if __name__ == "__main__":
    os.system('color 2')
    print()

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')  
  
    t1.start()
    t2.start()
  
    t1.join()
    t2.join()

'''
# https://stackoverflow.com/a/21725893/11493297
Option  Description

-a  Displays all files.
-b  Displays nonprinting characters in octal.
-c  Displays files by file timestamp.
-C  Displays files in a columnar format (default)
-d  Displays only directories.
-f  Interprets each name as a directory, not a file.
-F  Flags filenames.
-g  Displays the long format listing, but exclude the owner name.
-i  Displays the inode for each file.
-l  Displays the long format listing.
-L  Displays the file or directory referenced by a symbolic link.
-m  Displays the names as a comma-separated list.
-n  Displays the long format listing, with GID and UID numbers.
-o  Displays the long format listing, but excludes group name.
-p  Displays directories with /
-q  Displays all nonprinting characters as ?
-r  Displays files in reverse order.
-R  Displays subdirectories as well.
-t  Displays newest files first. (based on timestamp)
-u  Displays files by the file access time.
-x  Displays files as rows across the screen.
-1  Displays each entry on a line.

>>> adb shell ls -p /sdcard/Download/Telegram

    Archive/
    Reels.apk
    screenshot.png
    static/
'''
