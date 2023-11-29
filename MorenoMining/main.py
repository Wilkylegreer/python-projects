import pyperclip
from time import sleep

def live_update():
    print('New Copy')

live_update()
pyperclip.copy('ssh pi@172.20.1.109')
sleep(5)
live_update()
pyperclip.copy('cd xmrig')
sleep(2)
live_update()
pyperclip.copy('cd build')
sleep(2)
live_update()
pyperclip.copy('./xmrig -o gulf.moneroocean.stream:10128 -u 434uHiCpqt7PcuHs5k5DCzMrVcCLp4FNJJGQap9PFkJX5jEvHTJZbqqNrVt9N3GVargWX4cdj6egxABnYYUy3NyERowo3hT -p pi1')