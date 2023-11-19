
from tkinter import *
import os, json, threading
from tkinter import filedialog
from ppadb.client import Client as AdbClient

ip = input('''
----------------------------------------
Press `CTRL + PAUSE/BREAK` keys to exit.

Press ENTER for default IP 
    192.168.0.103
----------------------------------------

Paste IP Address of Device : ''')

try: os.mkdir('ScreenRecord')
except: pass

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
                os.system('static/keyevents.json')
            else:
                os.system(f'adb -s {ip} shell input keyevent {x}')
        except Exception as e: 
            print(e)

    def fun():
        key = num_list.get(num_list.curselection()[0])
        key = key.split(' : ')[0]
        os.system(f'adb -s {ip} shell input keyevent {key}')

    def pull_file(file="screenshot.png", pull_start_path='Download/Telegram/static/'):        
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.device(f'{ip}:5555')

        file = dir_list.get(dir_list.curselection()[0])
        pull_start_path = entry.get()
        event.set(f'{pull_start_path}/{file}')

        if file[-1] == '/':
            print(f'\n>>> {pull_start_path}/{file} Selected ...')

        else:
            try:
                print(f'\n>>> Receiving {file} ...')
                device.pull(f"/sdcard/{pull_start_path}/{file}", f"ScreenRecord/{file}")
                print(f'\tReceived Successfully.')

            except:
                print(f'\tFile NOT Received.')
            event.set(pull_start_path)

    def push_file(push_stop_path='Download/Telegram/static/'):
        client = AdbClient(host="127.0.0.1", port=5037)
        device = client.device(f'{ip}:5555')

        push_start_file = filedialog.askopenfilename()
        push_stop_path = entry.get()

        try:
            file = os.path.basename(push_start_file)

            if file.split('.')[-1] in ['apk', ]:
                print(f'\n>>> Installing {file} ...')
                device.install(push_start_file)
                print(f'\n>>>\tInstalled.')

            else:
                print(f'\n>>> Sending {file} ...')
                device.push(f"{push_start_file}", f"/sdcard/{push_stop_path}/{file}")
                print(f'\tSent Successfully.')
        except:
            print(f'\tFile NOT Selected.')
            pass
 
    while True:
        root = Tk()
        root.geometry("300x600")
        root.title("ScrCpy GUI")
        root.config(bg="gray")

        event = StringVar()
        dir_list = Listbox(root, height=7, width=30)
        dir_list.place(relx=0.5, rely=0.3, anchor='center')

        entry = Entry(root, textvariable = event)
        entry.place(relx=0.5, rely=0.14, anchor='center', width=270)

        rely3 = rely4 = 0.8
        rely5 = 0.9
        try:

            num_list = Listbox(root, height=8, width=30)
            with open('static/keyevents.json') as f:
                data = json.load(f)

            for i in data['key_events']:
                j = data['key_events'][i]
                k = j.split('adb shell input keyevent ')
                num_list.insert(k[1], f'{k[1]} : {i.split("key_")[1]}')

            num_list.place(relx=0.5, rely=0.6, anchor='center')
            get_num_btn = Button(root, bg='light green', text="Run ADB", command=fun)
            get_num_btn.place(relx=0.5, rely=0.67, anchor='center')

        except:
            btn = StringVar()
            btn1 = Entry(root, textvariable = btn)

            btn1.insert(0, '209') # Open Music App
            btn1.place(relx=0.5, rely=0.6, anchor='center')

            btn2 = Button(root, bg='light green', text = 'Keyevent', command = lambda: submit(btn.get()))
            btn2.place(relx=0.5, rely=0.65, anchor='center')

        path='Download/Telegram/static/'
        event.set(path)

        upload = Button(root, bg='yellow', text='Send File', command = lambda: push_file(path))
        upload.place(relx=0.5, rely=0.08, anchor='center')

        def on_click():
            path = event.get()

            output = os.popen(f'adb shell ls -p /sdcard/{path}')
            output = output.read().split('\n')[:-1]
            dir_list.delete(0, END)

            for i,j in enumerate(output):
                dir_list.insert(i, j)
            dir_list.place(relx=0.5, rely=0.3, anchor='center')

        button = Button(root, bg='light blue', text="Update Folder", command=on_click)
        button.place(relx=0.3, rely=0.43, anchor='center')

        download = Button(root, bg='yellow', text='Receive Selected', command = lambda: pull_file(path))
        download.place(relx=0.62, rely=0.43, anchor='center')

        btn3 = Button(root, text="Volume Up", bg='green', command=volup)
        btn3.place(relx=0.32, rely=rely3, anchor='center')

        btn4 = Button(root, text="Volume Down", bg='red', command=voldown)
        btn4.place(relx=0.63, rely=rely4, anchor='center')
        
        btn5 = Button(root, bg='pink', text="Power ON / OFF", command=power)
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
