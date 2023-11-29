# Libraries
import math

name = "Kyle"  # String
age = 20  # Int
count = 0  # Int
pi = 3.14  # Float
my_list = [1, 2, 3]  # List
my_tuple = (4, 5, 6)  # Tuple
my_dict = {"name": "Bob", "age": 30}  # Dictionary


def Output():
    if age == 20:
        return 20 - 2
    elif age == 19:
        return 19 + 1
    else:
        return 2


def Loops():
    for i in range(5):
        print(i)

    while count <= 10:
        print(count)
        count += 1


def Lists():
    colors = ['red', 'green', 'blue']
    for color in colors:
        print(color)


def MathSqr(variable):
    return math.sqrt(variable)


# Lists()
name = input('Enter your name: ')
numVar = float(input('Square Root a number: '))
print(MathSqr(numVar))
print(name + ' is ' + str(age) + ' years old.')
print('Basic Math Output: ' + str(Output()))
