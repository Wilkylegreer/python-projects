from openpyxl import load_workbook
from time import sleep
import pyautogui
import random

# Posisitons
# Text Button: 89 19
# Desired Text Placement: 1442 112
# Personal Text Placement: 39 214

dummy = input("Text Button Pos:")
textButtonX, textButtonY = pyautogui.position()
dummy = input("Eraser Button Pos:")
eraserButtonX, eraserButtonY = pyautogui.position()
dummy = input("Desired Text Pos:")
desTextX, desTextY = pyautogui.position()
dummy = input("Personal Text Pos:")
perTextX, perTextY = pyautogui.position()
count = input("How many reps: ")
x = 0

EXCEL_FILES_FOLDER = 'Excel_Files/'

# Edit Here to Support Multiple Sets of Vocab // 'Live_The_Law_of_Chastity.xlsx', 'Keep_The_Ten_Commandments.xlsx', 'Obey_The_Word_of_Wisdom.xlsx', 'Linguistic.xlsx',
fileNames = ['Keep_The_Law_of_Tithing.xlsx']

while(x < int(count)):
    rand = random.randint(0, len(fileNames) - 1)
    excel_file_path = EXCEL_FILES_FOLDER + fileNames[rand]

    print("From: " + fileNames[rand])

    loc = (excel_file_path)
    wb = load_workbook(loc)
    sheet = wb.active

    randRow = random.randint(2, len(sheet['A']))
    randCol = random.choice("AB")
    rowValue = sheet[randCol + str(randRow)].value

    if(randCol == "A"):
        answer = sheet["B" + str(randRow)].value
    else:
        answer = sheet["A" + str(randRow)].value

    pyautogui.click(eraserButtonX, eraserButtonY)
    sleep(.5)
    pyautogui.click(desTextX, desTextY)
    sleep(.5)
    pyautogui.click(textButtonX, textButtonY)  # Text Button
    sleep(1)
    pyautogui.click(desTextX, desTextY)  # Text Placement
    sleep(1)
    pyautogui.typewrite(" " + rowValue)  # Write Text
    sleep(.2)
    pyautogui.click(39, 100)  # Random Click
    sleep(.4)
    pyautogui.click(perTextX, perTextY)  # Personal Text Placement

    x += 1

    sleep(2)
    print("Answer: " + answer)
    input("Press Enter When Ready! (" + str(int(count)-x) + " Left)")
