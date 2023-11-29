import os

path = input('What is the folder path?\n')
prefix = input('What prefix would you like?\n')

pathList = os.listdir(path)

final = ''
index = 1

for filename in pathList:
    final = ''
    fileSplit = filename.split('.')
    final += prefix + str(index) + '.' + fileSplit[1]
    os.rename(path + '\\\\' + filename, path + '\\\\' + final)
    index += 1

print('Files Renamed Successfully!')
