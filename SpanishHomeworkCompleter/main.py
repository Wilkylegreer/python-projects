import os
import sys
import openpyxl
import requests
from bs4 import BeautifulSoup

cellList = ['C2', 'C19', 'C36']
letterList = ['B', 'C', 'D', 'E', 'F']
letterList2 = ['G', 'H']
numList = [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]


def present_conjugation(offset):
    rows = 0

    for index, conjugate_element in enumerate(conjugate_elements, start=0):
        conjugate = conjugate_element.text

        if rows == 6 and index % 5 == 0:
            break
        elif index % 5 == 0 and rows is not 6:
            rows += 1

        if index % 5 == 0:
            sheet[letterList[index % 5] +
                  str(numList[rows-1] + offset)] = conjugate
        elif index % 5 == 1 or index % 5 == 3:
            sheet[letterList[(index+1) % 5] +
                  str(numList[rows-1] + offset)] = conjugate
        elif index % 5 == 2 or index % 5 == 4:
            sheet[letterList[(index-1) % 5] +
                  str(numList[rows-1] + offset)] = conjugate


def subjunctive_conjugation(offset):
    rows = 0

    for index, conjugate_element in enumerate(conjugate_elements, start=30):
        conjugate = conjugate_element.text

        if rows == 6 and index % 2 == 0:
            break
        elif index % 2 == 0 and rows is not 6:
            rows += 1

        sheet[letterList2[index % 2] +
              str(numList[rows-1] + offset)] = conjugate_elements[index].text


def perfect_conjugation(offset):
    rows = 6

    for index, conjugate_element in enumerate(conjugate_elements, start=40):
        conjugate = conjugate_element.text

        if rows == 12 and index % 5 == 0:
            break
        elif index % 5 == 0 and rows is not 12:
            rows += 1

        if index % 5 == 0:
            sheet[letterList[index % 5] +
                  str(numList[rows-1] + offset)] = conjugate_elements[index+2].text
        elif index % 5 == 1 or index % 5 == 3:
            sheet[letterList[(index+1) % 5] + str(numList[rows-1] + offset)
                  ] = conjugate_elements[index + 2].text
        elif index % 5 == 2 or index % 5 == 4:
            sheet[letterList[(index-1) % 5] + str(numList[rows-1] + offset)
                  ] = conjugate_elements[index + 2].text


def perfect_sub_conjugation(offset):
    rows = 6

    for index, conjugate_element in enumerate(conjugate_elements, start=70):
        conjugate = conjugate_element.text

        if rows == 12 and index % 2 == 0:
            break
        elif index % 2 == 0 and rows is not 12:
            rows += 1

        sheet[letterList2[index % 2] +
              str(numList[rows-1] + offset)] = conjugate_elements[index + 2].text


verbList = input('What are the verbs? (Separate with spaces): ')

if verbList == 'exit':
    sys.exit()

verbList = verbList.split(" ")

if getattr(sys, 'frozen', False):
    # Running as a PyInstaller executable
    current_directory = sys._MEIPASS
else:
    # Running in a regular Python environment
    current_directory = os.path.dirname(os.path.abspath(__file__))

excel_file_name = "OutlineVerbs.xlsx"
excel_file_path = os.path.join(current_directory, excel_file_name)

workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

url = f"https://www.spanishdict.com/conjugate/{verbList[0]}"
url1 = f"https://www.spanishdict.com/conjugate/{verbList[1]}"
url2 = f"https://www.spanishdict.com/conjugate/{verbList[2]}"

for x in range(len(verbList)):
    sheet[cellList[x]] = verbList[x]

# VERB 1

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    conjugate_elements = soup.find_all('td', class_='BY2tUqJf')

    del conjugate_elements[138:144]
    del conjugate_elements[120 + 2:137 + 1:3]
    del conjugate_elements[48:90]
    del conjugate_elements[30 + 2:48 + 1:3]

    # for test, x in enumerate(conjugate_elements, start=0):
    #     print(f'{x.text}-{test}')

    # Present Conjugations

    present_conjugation(0)

    # Subjunctive Conjugations

    subjunctive_conjugation(0)

    # Perfect Conjugations

    perfect_conjugation(0)

    # Perfect Subjunctive Conjugations

    perfect_sub_conjugation(0)

# VERB 2

response = requests.get(url1)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    conjugate_elements = soup.find_all('td', class_='BY2tUqJf')

    del conjugate_elements[138:144]
    del conjugate_elements[120 + 2:137 + 1:3]
    del conjugate_elements[48:90]
    del conjugate_elements[30 + 2:48 + 1:3]

    # Present Conjugations

    present_conjugation(17)

    # Subjunctive Conjugations

    subjunctive_conjugation(17)

    # Perfect Conjugations

    perfect_conjugation(17)

    # Perfect Subjunctive Conjugations

    perfect_sub_conjugation(17)


# VERB 3

response = requests.get(url2)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    conjugate_elements = soup.find_all('td', class_='BY2tUqJf')

    del conjugate_elements[138:144]
    del conjugate_elements[120 + 2:137 + 1:3]
    del conjugate_elements[48:90]
    del conjugate_elements[30 + 2:48 + 1:3]

    # Present Conjugations

    present_conjugation(34)

    # Subjunctive Conjugations

    subjunctive_conjugation(34)

    # Perfect Conjugations

    perfect_conjugation(34)

    # Perfect Subjunctive Conjugations

    perfect_sub_conjugation(34)

homeworkNumber = input('What homework number? ')

new_file_name = f"Span-3050_Tarea{homeworkNumber}_Kyle_Greer.xlsx"
save_path = os.path.join(current_directory, new_file_name)

workbook.save(save_path)
workbook.close()
