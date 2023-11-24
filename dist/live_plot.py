
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import style
import requests, json

def convert(ts):
    ts /= 1000
    unix = datetime.utcfromtimestamp(ts)
    mili = unix.strftime('%Y-%m-%d %H:%M:%S')
    return mili

username = 'imvickykumar999'
password = 'imvickykumar999'

ip,port = '192.168.0.102', 8080
link = f"http://{ip}:{port}/sensors.json"

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

print()
sensor = {}
filename = 'ScreenRecord/sensor.json'

try:
    r = requests.get(link, auth=(username, password))
    data = r.json()

    with open(filename, 'w') as outfile: 
        json.dump(data, outfile)
except:
    with open(filename, 'r') as f: 
        data = json.load(f)

for i, j in enumerate(data.keys()):
    # print(i, j)
    sensor.update({i : j})

inp = 0
# inp = input('\nEnter sensor number : ')
# if inp == '':
#     inp = 0
# else:
#     inp = int(inp)

def animate(k):
    try:
        r = requests.get(link, auth=(username, password))
        data = r.json()

        xs, ys = [], []
        keys = data[sensor[inp]]

        for i in keys['data']:
            if i[1][2] < 0:
                side = 'Screen Down'
            else:
                side ='Screen Up'

            print(side,
                '\t', 
                format(i[1][2], ".5f"), 
                keys['unit'], 
                convert(int(i[0]))
            )
            xs.append(float(i[0]))
            ys.append(float(i[1][2]))

        ax1.clear()
        ax1.plot(xs, ys)
        ax1.set_ylim(-80, 80)

        plt.title(side)
        # plt.title(' '.join(sensor[inp].title().split('_')))

        plt.savefig(f"ScreenRecord/{sensor[inp]}.png")
        return fig
    
    except Exception as e:
        print('\nPress CTRL+PAUSE/BREAK to exit.\n', e)

        plt.savefig(f"ScreenRecord/{sensor[inp]}.png")
        exit()

print(f'Graph of {sensor[inp]}')
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()


rf'''
>>> python live_plot.py

0 accel
1 battery_charging
2 mag
3 gyro
4 proximity
5 gravity
6 lin_accel
7 rot_vector
8 battery_voltage
9 battery_level
10 battery_temp

Enter sensor number : 0
Graph of accel
.
.
.
-0.7111 m/s²     2023-11-23 07:46:25
-1.3647 m/s²     2023-11-23 07:46:25
-1.1636 m/s²     2023-11-23 07:46:25
-0.9625 m/s²     2023-11-23 07:46:25

 'accel'
QObject::~QObject: Timers cannot be stopped from another thread
^C
'''
