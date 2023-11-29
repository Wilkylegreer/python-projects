import os
import linecache
from datetime import date
from time import sleep


def MondayCheck():
    print(chr(27) + "[2J")
    print('Today is Monday, time to plan everything for the week!')
    sleep(1)


def RunCheck():
    print(chr(27) + "[2J")
    if date.today().isoweekday() == 1:
        print('Today IS Monday so')
        print('Running Monday Check...')
        sleep(.5)
        MondayCheck()
    else:
        print('Today is NOT Monday so')
        print('Running Assignment Splitter...')

        saveFile = open('saved_data.txt', 'a')
        saveFile.write('\nThis is a Test')
        saveFile.close()


def SetClasses():

    print(chr(27) + "[2J")

    classes = input(
        'What classes do you have? (Separate each class with a single space)\n')

    classes = classes.split(' ')

    saveFile = open('saved_data.txt', 'a')
    finalString = ''
    for x in classes:
        finalString += x + ' '

    saveFile.write(finalString.rstrip())
    saveFile.close()

    print('Successfully set classes!')
    sleep(2)
    StartUp()


def ChangeClasses():

    print(chr(27) + "[2J")

    classes = linecache.getline('saved_data.txt', 1).strip()

    print('----Classes----')
    print('------ ' + classes + ' ------')

    classes = classes.split(' ')
    classToChange = input(
        'Enter the name of the class you want to change and what you are changing it with (Separate with space)\n')

    classToChange = classToChange.split(' ')

    replaceIndex = classes.index(classToChange[0])
    classes[replaceIndex] = classToChange[1]

    saveFile = open('saved_data.txt', 'a')
    finalString = ''
    for x in classes:
        finalString += x + ' '

    saveFile.write(finalString.rstrip())
    saveFile.close()

    print('Successfully Changed Class!')
    sleep(1)
    StartUp()


def FileAdjustments():
    if os.path.exists('saved_data.txt'):
        print('Opening File...')
        sleep(1)
        choice = int(
            input('What would you like to do - Set classes (1) || Change class(es) (2)\n'))
        if choice == 1:
            print('Running set classes...')
            SetClasses()
        elif choice == 2:
            print('Running change class(es)...')
            ChangeClasses()

    else:
        print('Creating File...')
        sleep(1)
        for x in range(3):
            print('.', end=" ", flush=True)
            sleep(.5)
        print('\nFile Created!')
        saveFile = open('saved_data.txt', 'x')
        sleep(1)
        SetClasses()


def StartUp():

    print(chr(27) + "[2J")

    userinput = int(
        input('Would you like to change/set classes (1) || Run day check (2) || Remove saved data (3) || Exit (Any other #)\n'))

    if userinput == 1:
        FileAdjustments()
    elif userinput == 2:
        sleep(1)
        RunCheck()
    elif userinput == 3:
        sleep(1)
        confirm = input('Are you sure? (y/n)\n')
        if confirm == 'y':
            print('Removing File...')
            try:
                os.remove('saved_data.txt')
                print('Successfully removed file!')
                StartUp()
            except:
                print('File does not exist!')
                sleep(1)
                print('Returning to start.')
                StartUp()
        else:
            print('Returning to start.')
            sleep(1)
            StartUp()
    else:
        sleep(1)
        print('Exiting...')
        sleep(.5)


# Starts the scheduler
StartUp()
