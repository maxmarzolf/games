import random as rand

count = 0
game_range = 100


def random_addition():
    global count
    global game_range
    number1 = rand.randrange(game_range)
    number2 = rand.randrange(game_range)
    print(number1, '+', number2, '=')
    answer = input()
    correct_answer = (number1 + number2)
    if int(answer) == correct_answer:
        is_true = True
        count += 1
        if count >= 10:
            game_range = game_range * 10
        call_function(is_true)
    else:
        is_true = False
        call_function(is_true)

    return is_true


def call_function(is_true):
    if is_true:
        random_addition()
    else:
        print('game over')


random_addition()
