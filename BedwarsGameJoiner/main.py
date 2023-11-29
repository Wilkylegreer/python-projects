import requests
import time
import os
import win10toast as nf
from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup
from playsound import playsound

# API Setup
# 3aca7173-f1b3-4a0d-8b8f-d93a23454c6c

print('# To Get API Key Login to Hypixel and type /api #')
apiKey = input('Input your API Key:\n')

userLookup = input('Input the player you want to try and join:\n')

# Webscraping Logic Here...
resp = requests.get('https://mcuuid.net/?q=' + userLookup)
respTxt = resp.text

soup = BeautifulSoup(respTxt, 'lxml')

data = soup.find("input", {"id": "results_id"})
requestedUUID = data['value']

joinable = False


def write():
    keyboard = Controller()
    keyboard.type("/")
    time.sleep(.1)
    keyboard.type('play bedwars_eight_one')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def PlayAble(ja, dta):
    try:
        dta = requests.get(
            "https://api.hypixel.net/status?key=" + apiKey + "&uuid=" + requestedUUID).json()
        while True:
            dta = requests.get(
                "https://api.hypixel.net/status?key=" + apiKey + "&uuid=" + requestedUUID).json()

            joinable = ja
            currentGame = dta["session"]["mode"]

            if currentGame == 'EIGHT_ONE' and joinable == True:
                currentMap = dta["session"]["map"]
                print(currentGame + ' on ' + currentMap)
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(.5)
                print('Current Map: ' + currentMap)
                print('\nTrying to join game...')
                time.sleep(.1)

                playsound(
                    'C:/Users/wilky/Documents/My Folders/Projects/Python/BedwarsGameJoiner/Audio/sound.wav')

                # Simulate Keyboard inputs
                # write()
                joinable = False
                MainCheck()
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Not in a game yet, trying again')
                for x in range(3):
                    time.sleep(.2)
                    print('.', end=" ", flush=True)

    except:
        print('Unknown API Key or Player!')


# 3aca7173-f1b3-4a0d-8b8f-d93a23454c6c

# 0f102fc9-2265-4de2-b939-1172cd942e39
def MainCheck():
    try:
        while True:
            data = requests.get(
                "https://api.hypixel.net/status?key=" + apiKey + "&uuid=" + requestedUUID).json()

            onlineStatus = data['session']['online']

            joinable = False

            if onlineStatus == True:
                currentGame = data["session"]["mode"]
                print('\nPlayer is online!')
            else:
                print('Player not online!')
                break

            time.sleep(.5)

            if currentGame == 'LOBBY' and joinable == False:
                print(userLookup + ' has entered the lobby')
                joinable = True
                PlayAble(joinable, data)
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Not in Lobby Yet')
                currentMap = data["session"]["map"]
                print('Current Map: ' + currentMap)
                for x in range(3):
                    time.sleep(.2)
                    print('.', end=" ", flush=True)
                continue
    except:
        print('Unknown API Key or Player!')


MainCheck()
