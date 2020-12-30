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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or (C) correct? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'Yay! The computer guessed your number, {guess}, correctly!!')

computer_guess(10)