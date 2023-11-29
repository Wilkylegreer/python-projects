from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# RGB: (255, 219, 195)

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(658, 368, 604, 424))
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if (b in range(180, 210)):
                click(x+658, y+368)
                time.sleep(.05)
                break
