
> # `SD Card Manipulator` || `scrcpy GUI`
>
> ![images-2 fill size_2000x1334 v1611688517](https://github.com/imvickykumar999/Android-Trojan-Horse/assets/50515418/8806c02a-a7a3-425b-a241-51917965dc75)

    Watch Tutorial on YouTube: https://www.youtube.com/watch?v=HD-c2H3NoW8

<br>

<table>
<tr>

<td>
keyevent.json absent
</td>

<td>
keyevent.json present
</td>

</tr>

<tr>
<td><img src="https://github.com/imvickykumar999/Android-Trojan-Horse/assets/50515418/3e951fd0-de62-486f-b8c7-9debd0998b78" width="100%" alt="keyevent_absent"></td>
<td><img src="https://github.com/imvickykumar999/Android-Trojan-Horse/assets/50515418/5789b05a-0bf4-4d71-9e6b-fcacf670ea7d" width="100%" alt="keyevent_present"></td>
</tr>

</table>

<br>

## `One Time USB Connect via Social Engineering`

```bash
>>> adb devices
    * daemon not running; starting now at tcp:5037
    * daemon started successfully
    List of devices attached

>>> adb tcpip 5555
    restarting in TCP mode port: 5555

>>> adb devices
    List of devices attached
    RZ8N60JN0EE     device

>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
    192.168.0.103

>>> adb connect 192.168.0.103:5555
    connected to 192.168.0.103:5555

>>> adb pair 192.168.0.103:40535
    Enter pairing code: 230630
    Successfully paired to 192.168.0.103:40535 [guid=adb-RZ8N60JN0EE-DzkZ1Q]
```
