# Imports
import speech_recognition as sr
import time
import random
import pyttsx3

# Setup
re = sr.Recognizer()

jokeStart = []
jokeEnd = []

lineCount = 0

speech = pyttsx3.init()
speech.setProperty('rate', 150)

# Opening
jokes = open(
    'C:/Users/wilky/Documents/My Folders/Projects/Python/TellMeAJoke/Jokes.txt', 'r')

# Reading Line
lines = jokes.readlines()
lineCount = len(lines)

# Calculations/Appending
x = 1
while x <= (lineCount + 1) / 3:
    jokeStart.append(lines[(-2 + 3 * x) - 1])
    x += 1

y = 1
while y <= (lineCount + 1) / 3:
    jokeEnd.append(lines[(-1 + 3 * y) - 1])
    y += 1


# Grabbing Random Joke Function
def RandomJoke():
    r = random.randint(0, len(jokeEnd))
    print('Joke : {}'.format(r))
    return r


# Would You Like to Hear a Joke?
def WouldYou():
    speech.say("Would you like to hear a joke?")
    speech.runAndWait()
    WhileLoop(0)


def TellStart(rint):
    speech.say(jokeStart[rint])
    speech.runAndWait()
    WhileLoop(rint)


def TellEnd(rint):
    speech.say(jokeEnd[rint])
    speech.runAndWait()
    time.sleep(1)
    speech.say('Would you like to hear another?')
    speech.runAndWait()
    WhileLoop(rint)


def StartJoke():
    randint = RandomJoke()
    speech.say('Ok here we go')
    speech.runAndWait()
    TellStart(randint)


def WhileLoop(rint):
    while True:
        print('Sensing')
        with sr.Microphone() as source:
            audio = re.listen(source)
            try:
                text = re.recognize_google(audio)
                if(text == 'why' or text.lower() == 'okay' or text == 'how' or text == "i don't know" or text == 'no' or text == 'tell me' or text == 'what' or text == 'where' or text == 'what is it'):
                    TellEnd(rint)
                    break

                if(text == 'tell me another'):
                    StartJoke()
                    break

                if(text == 'stop'):
                    speech.say('No longer Sensing')
                    speech.runAndWait()
                    break

                if(text == 'yes'):
                    StartJoke()
                    break

            except:
                print('Could not decipher what you said.')


WouldYou()
