
import os, time
from ppadb.client import Client as AdbClient


class Manuipulate_sdcard():
    def __init__(self, host, port) -> None:

        print(f'\nConnecting ...')
        os.system(f'adb connect {host}')

        self.client = AdbClient(
            host="127.0.0.1", 
            port=5037
        )

        self.serial = f'{host}:{port}'
        self.device = self.client.device(self.serial)


    def all_devices(self):
        print('\nList of Connected Devices.')

        for device in self.client.devices():
            print('\t', device.serial)


    def get_version(self):
        print('\nVersion:', self.client.version())


    def disconnect(self):
        self.client.remote_disconnect(self.serial)
        print('\nADB Disconnected.')


    def screenshot(self, ss):
        result = self.device.screencap()

        with open(f"static/{ss}", "wb") as fp:
            fp.write(result)
            print('\nScreenshot saved.')


    def install_apk(self, apk):
        apk_path = f"static/{apk}"

        print('\nInstalling APK ...')
        self.device.install(apk_path)
        print('APK Installed.')


    def push_file(self, push_start_file='static/screenshot.png', push_stop_path='Download/Telegram/static/'):
        file = os.path.basename(push_start_file)
        
        self.device.push(f"{push_start_file}", f"/sdcard/{push_stop_path}/{file}")
        print(f'\nFile "{push_start_file}" Pushed.')


    def push_folder(self, path='Download/'):
        self.device.push("static/", f"/sdcard/{path}/static/")
        print(f'\nFolder "{path}/static" Pushed.')


    def pull_file(self, file='screenshot.png', path='Download/'):        
        self.device.pull(f"/sdcard/{path}/{file}", f"static/{file}")
        print(f'\nFile "{path}/{file}" Pulled.')


if __name__ == '__main__':
    host, port = "192.168.0.102", 5555
    sdcard = Manuipulate_sdcard(host, port)

    # sdcard.get_version()
    # sdcard.all_devices()

    # apk = 'example.apk'
    # sdcard.install_apk(apk)

    # pullpath = 'Movies/Instagram'
    # pullfile = 'reels.mp4'
    # sdcard.pull_file(pullfile, pullpath)

    # time.sleep(1)
    # push_stop_path = 'Download/Telegram/static'
    push_start_file = 'static/screenshot.png'

    sdcard.push_file(push_start_file)
    # sdcard.push_folder(pushpath)

    time.sleep(1)
    ss = 'screenshot.png'

    sdcard.screenshot(ss)
    # sdcard.disconnect()
