# Guessing Game Code

from random import randint

random_compute = randint(1, 10)

input_str = 'guess a number between 1 and 10 \n'
user_input  = int(input(input_str))

while True:
    if user_input == random_compute:
        print('You guesed it right ! Hurry')
        user_option = input('Do you want to continue [y/n]?')
        if user_option != 'y':
            print('Thanks for playing with us, see you soon')
            break
    elif user_input > random_compute:
        print('Sorry, You guessed it high')
    elif user_input < random_compute:
        print('Sorry, You guessed it low')
    else:
        print('Invalid user input')
    random_compute = randint(1, 10)
    user_input  = int(input(input_str))