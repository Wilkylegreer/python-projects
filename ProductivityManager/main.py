import pyautogui
import pygetwindow as gw
import psutil


def kill_process(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            process.terminate()


edge = 'msedge.exe'
lunar = 'Lunar Client.exe'
minecraft = 'javaw.exe'

kill_process(minecraft)


# Replace 'Browser Tab Title' with the title of the browser tab you want to close
tab_title = 'YouTube'

# List all open windows
windows = gw.getWindowsWithTitle(tab_title)

if len(windows) > 0:
    # Close the first window with the specified title
    windows[0].close()
else:
    print(f"No window with title '{tab_title}' found.")
