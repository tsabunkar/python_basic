from random import random


# !function Structure

# def name_of_the_function():
#    ____logic

# def - stands for define


def say_hi():  # Function definition
    print('hi')


say_hi()  # Function called/invoked


# ?NOTE: Function should be called after it is defined it, else you will get -NameError: name 'say_hi' is not defined


def print_square(x):
    return x ** 2


print(print_square(3))

print('____flip a coin____')


def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"


print(type(flip_coin))  # * <class 'function'>
print(flip_coin)  # * <function flip_coin at 0x7fc2adc3d550>
print(flip_coin())
