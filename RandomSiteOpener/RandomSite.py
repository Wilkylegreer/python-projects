import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com', 'youtube.com', 'apple.com', 'gmail.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 5)
    time.sleep(seconds)