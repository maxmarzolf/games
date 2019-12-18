import random

verbs = {'abrir': 'to open', 'acabar': 'to finish/end', 'aceptar': 'to accept', 'alcanzar': 'to reach',
         'aparecer': 'to appear', 'ayudar': 'to help', 'buscar': 'to look for', 'caer': 'cambiar',
         'comenzar': 'to begin', 'comprender': 'to understand',
         'conocer': 'to know/meet', 'conseguir': 'to get', 'considerar': 'to consider', 'contar': 'to count',
         'convertir': 'to convert/change',
         'correr': 'to run', 'crear': 'to create', 'creer': 'to believe', 'cumplir': 'to achieve', 'dar': 'to give',
         'deber': 'to owe',
         'decir': 'to say', 'dejar': 'to leave/allow', 'descubrir': 'to discover', 'dirigir': 'to direct',
         'empezar': 'to start', 'encontrar': 'to find',
         'entender': 'to understand', 'entrar': 'to enter', 'escribir': 'to write', 'escuchar': 'to listen',
         'esperar': 'to wait/hope', 'estar': 'to be',
         'estudiar': 'to study', 'existir': 'to exist', 'explicar': 'to explain', 'formar': 'to form/make',
         'ganar': 'to earn/win', 'gustar': 'to like', 'haber': 'to have',
         'hablar': 'to speak/talk', 'hacer': 'to do', 'intentar': 'to try', 'ir': 'to go', 'jugar': 'to play',
         'leer': 'to read', 'levantar': 'to get up/raise', 'llamar': 'to call',
         'llegar': 'to arrive', 'llevar': 'to carry', 'lograr': 'to achieve/manage', 'mantener': 'to maintain/keep',
         'mirar': 'to watch/look', 'morir': 'to die',
         'nacer': 'to be born', 'necesitar': 'to need', 'ocurir': 'to occur/happen', 'ofrecer': 'to offer',
         'oir': 'to hear', 'pagar': 'to pay', 'parar': 'to stop',
         'parecer': 'to seem', 'partir': 'to leave', 'pasar': 'to happen/pass', 'pedir': 'to ask for',
         'perder': 'to loose', 'permitir': 'to permit/allow', 'poder': 'to be able to',
         'poner': 'to put', 'preguntar': 'to ask', 'presentar': 'to introduce/present', 'producir': 'to produce',
         'quedar': 'to stay', 'querer': 'to want/love', 'realizar': 'to achieve',
         'recibir': 'to recieve', 'reconocer': 'to recognize', 'recordar': 'to remember', 'resultar': 'to turn out',
         'saber': 'to know', 'sacar': 'to take out', 'salir': 'to go out',
         'seguir': 'to follow', 'sentir': 'to feel', 'ser': 'to be', 'servir': 'to serve/function',
         'suponer': 'to suppose', 'tener': 'to have', 'terminar': 'to finish', 'tocar': 'to touch/play',
         'tomar': 'to take', 'trabajar': 'to work', 'traer': 'to bring', 'tratar': 'to treat', 'utilizar': 'to use',
         'venir': 'to come', 'ver': 'to see', 'vivir': 'to live', 'volver': 'to return/come back'}


def start():
    print('Type Number to Choose Practice Format \n1. English Translation \n2. Spanish Translation')
    choice = input()
    check_key(choice)
    # if choice == '1':
    #    entire_list_random_english_translation()
    # if choice == '2':
    #    entire_list_random_spanish_translation()


def entire_list_random_english_translation():
    correct = 0
    incorrect_list = []
    for item in verbs:
        randomkey, randomvalue = random.choice(list(verbs.items()))
        print(randomkey)
        print('Enter English Translation: ')
        Answer = input()
        if Answer == 'restart':
            start()
        if (Answer == randomvalue):
            print('CORRECT')
            print("\n")
            correct = correct + 1
        else:
            incorrect_list.append(randomkey)
            print('INCORRECT')
            print('The correct answer is', randomvalue)
            print("\n")
    print('You got', ((correct / 50) * 100), '% correct')
    print(incorrect_list)
    print('Do you want to practice the verbs you got incorrect? yes/no')
    retry = input()
    # if retry == 'yes':


def entire_list_random_spanish_translation():
    correct = 0
    incorrect_list = []
    for item in verbs:
        randomkey, randomvalue = random.choice(list(verbs.items()))
        print(randomvalue)
        print('Enter Spanish Translation: ')
        Answer = input()
        if Answer == 'restart':
            start()
        if (Answer == randomkey):
            print('CORRECT')
            print("\n")
            correct = correct + 1
        else:
            incorrect_list.append(item)
            print('INCORRECT')
            print('The correct answer is', randomkey)
            print("\n")
    print('You got', ((correct / 50) * 100), '% correct')


print(incorrect_list)


def check_key(english_translation):
    for key, value in verbs.items():
        if value == english_translation:
            print(key)


def check_value(spanish_translation):
    for key, value in verbs.items():
        if key == spanish_translation:
            print(value)


start()