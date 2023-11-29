from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# 74, 74, 86

# https://lagged.com/play/1461/

# Row ONE
# Column 1: x: 2649, 259
# Column 2: x: 2808, 259
# Column 3: x: 2968, 259
# Column 4: x: 3128, 259

# Row TWO
# Column 1: x: 2649, 418
# Column 2: x: 2808, 418
# Column 3: x: 2968, 418
# Column 4: x: 3128, 418

# Row THREE
# Column 1: x: 2649, 577
# Column 2: x: 2808, 577
# Column 3: x: 2968, 577
# Column 4: x: 3128, 577

# Row FOUR
# Column 1: x: 2649, 736
# Column 2: x: 2808, 736
# Column 3: x: 2968, 736
# Column 4: x: 3128, 736

time.sleep(5)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.000001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:

    try:
        # Row ONE
        if pyautogui.pixel(2649, 259)[0] == 74:
            print('Column 1 Row 1')
            click(2649, 259)
        if pyautogui.pixel(2808, 259)[0] == 74:
            print('Column 2 Row 1')
            click(2808, 259)
        if pyautogui.pixel(2968, 259)[0] == 74:
            print('Column 3 Row 1')
            click(2968, 259)
        if pyautogui.pixel(3128, 259)[0] == 74:
            print('Column 4 Row 1')
            click(3128, 259)

        # Row TWO
        if pyautogui.pixel(2649, 418)[0] == 74:
            print('Column 1 Row 2')
            click(2649, 418)
        if pyautogui.pixel(2808, 418)[0] == 74:
            print('Column 2 Row 2')
            click(2808, 418)
        if pyautogui.pixel(2968, 418)[0] == 74:
            print('Column 3 Row 2')
            click(2968, 418)
        if pyautogui.pixel(3128, 418)[0] == 74:
            print('Column 4 Row 2')
            click(3128, 418)

        # Row THREE
        if pyautogui.pixel(2649, 577)[0] == 74:
            print('Column 1 Row 3')
            click(2649, 577)
        if pyautogui.pixel(2808, 577)[0] == 74:
            print('Column 2 Row 3')
            click(2808, 577)
        if pyautogui.pixel(2968, 577)[0] == 74:
            print('Column 3 Row 3')
            click(2968, 577)
        if pyautogui.pixel(3128, 577)[0] == 74:
            print('Column 4 Row 3')
            click(3128, 577)

        # Row FOUR
        if pyautogui.pixel(2649, 736)[0] == 74:
            print('Column 1 Row 4')
            click(2649, 736)
        if pyautogui.pixel(2808, 736)[0] == 74:
            print('Column 2 Row 4')
            click(2808, 736)
        if pyautogui.pixel(2968, 736)[0] == 74:
            print('Column 3 Row 4')
            click(2968, 736)
        if pyautogui.pixel(3128, 736)[0] == 74:
            print('Column 4 Row 4')
            click(3128, 736)

    except:
        print('Cannot get pixel for the moment!')
