import webbrowser
import pandas as pd

# This program will force me to do a few things on my computer to make sure I do important things, possibly will be able to keep track of things I've done

excel_file_path = './file.xlsx'

df = pd.read_excel(excel_file_path)

print(df)

def open_youtube():
    youtube_url = ''
    webbrowser.open(youtube_url)