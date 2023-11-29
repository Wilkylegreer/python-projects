import os
clear = lambda: os.system('cls') #on Windows System
clear()

chickenl = 2
cowl = 4
pigl = 4
def legCount(chickens, cows, pigs):
    chickTotal = chickenl * chickens
    cowTotal = cowl * cows
    pigTotal = pigl * pigs
    grandTotal = chickTotal + cowTotal + pigTotal
    return grandTotal

print("Help Farmer Joe figure out how many legs in total are in his farm!")
x = int(input("How many Chickens: "))
y = int(input("How many Cows: "))
z = int(input("How many Pigs: "))

result = legCount(x, y, z)

print("There are a total of " + "{:,}".format(result) + " legs!")