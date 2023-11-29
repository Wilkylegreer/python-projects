# 4 Types of variables
# int
# bool
# float
# string
import os
def clear(): return os.system('cls')  # on Windows System


clear()

cows = int(input('How many cows do you want?\n'))
horses = int(input('How many horses do you want?\n'))
chickens = int(input('How many chickens do you want?\n'))
pigs = int(input('How many pigs do you want?\n'))

cowLegs = 4
horseLegs = 4
pigLegs = 4
chickenLegs = 2

totalAnimals = cows + pigs + horses + chickens

print('How many pigs does Farmer Joe have? ' + str(pigs))
print('How many cows does Farmer Joe have? ' + str(cows))
print('How many horses does Farmer Joe have? ' + str(horses))
print('How many chickens does Farmer Joe have? ' + str(chickens))
print('How many total animals does Farmer Joe have? ' + str(totalAnimals))


def LegAdder(an1, an2, an3, an4):
    cowTotal = an1 * cowLegs
    horseTotal = an2 * horseLegs
    chickenTotal = an3 * chickenLegs
    pigTotal = an4 * pigLegs
    return cowTotal


print('Farmer Joe has {} cow legs!'.format(
    LegAdder(cows, horses, chickens, pigs)))
