import random as rand
import datetime

count = 0
level = 0
game_range = 100


def random_addition():
    global count
    global level
    global game_range
    number1 = rand.randrange(game_range)
    number2 = rand.randrange(game_range)
    print(number1, '+', number2, '=')
    start_timer = get_time()
    answer = input()
    print(get_time() - start_timer)
    correct_answer = (number1 + number2)
    if int(answer) == correct_answer:
        is_true = True
        count += 1
        if count % 10 == 0:
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


def get_time():
    return datetime.datetime.now()


random_addition()

