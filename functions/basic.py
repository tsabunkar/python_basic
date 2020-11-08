from random import random


# !function Structure

# def name_of_the_function():
#    ____logic

# def - stands for define


def say_hi():  # Function definition
    print('hi')


say_hi()  # Function called/invoked


# ?NOTE: Function should be called after it is defined it, else you will get -NameError: name 'say_hi' is not defined


def print_square(x):  # x-> is called parameter of function not argument
    return x ** 2


print(print_square(3))  # 3-> is called argument of function not parameter

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


# !Default Parameters

def exponents(num, power=2):
    return num ** power


print(exponents(2, 3))
print(exponents(2))


def add(a, b):
    return a + b


def maths(a, b, foo=add):
    return foo(a, b)


def subtract(a, b):
    return a - b


print(maths(2, 3))
print(maths(3, 2, subtract))


# !keyword Arguments <-- provides more flexibility

def fullname(first, last):
    return f"hello, {first} {last}"


print(fullname('tejas', 'sabunkar'))
print(fullname(last='sabunkar', first='usha'))


# !Scope
#  where our variable can be accessed, example for functional scope:


def say_hello():
    instructor = 'joe'
    return f"hello there, {instructor}"  # instructor <- this variable is functional scoped


say_hello()
# print(instructor) # NameError: name 'instructor' is not defined

# !global scope
total = 0

"""""
def increment():
    total += 1  # UnboundLocalError: local variable 'total' referenced before assignment
    return total
"""""


# ? so inorder-to assign the reference variables that were originally assigned on the global scope

def increment():
    global total
    total += 1
    return total


increment()

print(total)


# ! nonlocal scope

def outer_foo():
    count = 1  # variable scope -> functional scope

    def inner_foo():
        nonlocal count  # this variable is defined in above one level function, but not as global scope
        count += 1
        return count

    return inner_foo()


print(outer_foo())


########## Documentation ##########

def foo_bar():
    """This is Documentation abt this foo_bar function"""
    return 'Documentation is Great'


print(foo_bar())
print(foo_bar.__doc__)  # prints the doc return in the first line of function

print('_______')
print(print.__doc__)
print('_______')
print(random.__doc__)
print('_______')
print([].pop.__doc__)
