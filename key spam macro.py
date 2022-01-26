import win32api, win32con
import keyboard
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")



def leftClick():
    for _ in range(10):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


keyboard.add_hotkey(f"{config.get('main','hotkey_to_press')}",leftClick)
keyboard.wait()