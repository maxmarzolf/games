import random as rand
import datetime

count = 0
level = 0
game_range = 100
lap_time = []


def random_addition():
    global count
    global level
    global game_range
    global lap_time
    number1 = rand.randrange(game_range)
    number2 = rand.randrange(game_range)
    print(number1, '+', number2, '=')
    start_timer = get_time()
    answer = input()
    lap = get_time() - start_timer
    lap_time.append(lap.seconds)
    correct_answer = (number1 + number2)
    if int(answer) == correct_answer:
        is_true = True
        count += 1
        if count % 10 == 0:
            game_range = game_range * 10
            average_time = sum(lap_time)/len(lap_time)
            print('Your average time was ', average_time, ' seconds')
        start_game(is_true)
    else:
        is_true = False
        start_game(is_true)

    return is_true


def start_game(is_true):
    if is_true:
        random_addition()
    else:
        print('game over')


def get_time():
    return datetime.datetime.now()


random_addition()
