import random as rand
import math as math

count = 0
range = 100


def random_addition():
    global count
    global range
    istrue = bool
    number1 = rand.randrange(range)
    number2 = rand.randrange(range)
    print(number1, '+', number2, '=')
    answer = input()
    correctanswer = (number1 + number2)
    if (int(answer) == correctanswer):
        istrue = True
        count += 1
        if count >= 10:
            range = range * 10
        call_function(istrue)
    else:
        istrue = False
        call_function(istrue)

    return istrue


def call_function(istrue):
    if istrue == True:
        random_addition()
    else:
        print('game over')


random_addition()