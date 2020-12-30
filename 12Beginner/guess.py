import random


def guess(x):
    rand = random.randint(1,x)
    gues = 0
    while rand != gues:
        gues = int(input(f"Guess a number between 1 and {x}? "))
        if gues < rand:
            print('Sorry, guess again. Too high!')
        elif gues > rand:
            print('Sorry, guess again. Too low!')
    print(f'Yay, congrats. You have guessed the number {rand} correctly!')

guess(10)
