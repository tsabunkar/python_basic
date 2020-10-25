# data = input('what is your favorite color?')
# print('you said ' + data)

# print('what is your favorite color?')
# data = input()
# print('you said ' + data)

# ! Elseif Ladder

name = input('what is your name? \n')
if name == 'Tony':
    print('He is Iron Man') # !Indentation MATTERS in PYTHON there is no brackets
elif name == 'Bruce':
    print('He is Hulk')
else:
    print('You are regular person')


################################################################

from random import randint
choice = randint(1,10)

if choice == 7:
    print('lucky')
else:
    print('unlucky')

###################################

from random import randint
num = randint(1, 1000) #picks random number from 1-1000

if num % 2 == 0:
    print("even")
else:
    print("odd")


###################################
# Truthiness or Falsiness

x = 10
print(x is 10) # True (Truthiness bcoz the value would be resolved to Boolean True value)
print(x is 20) # False (Value would be resolved to Boolean False ==> Falsiness)

###################################

age = 18
if age >= 18:
    print('Your are allowed inside the club, since ur 18')
else:
    print('Your are not allowed')

###################################

is_girl_friend_available = False

if age >= 18 and is_girl_friend_available:
    print('Your are allowed inside the club, since ur 18 and have GF')
else:
    print('Your are not allowed')


###################################

from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

print(f'option got selected {food}')

if food == 'apple' or food == 'grape':
    print('Fruits')
elif food == 'bacon' or food == 'steak':
    print('meat')
elif food == 'worm' or food == 'dirt':
    print('yuck!!')
else:
     print('Sorry Something went wrong')
    
###################################

is_weekend = True

if not is_weekend:
    print('Go To Work')
else:
    print('Lets Learn new things')

###############################

x = 15
y = 0
print(x or 15) # Think this as --> bool(x or y) [In order to understand Truthiness or Falseness]

###############################

print(not -1)
print(not 0)

print('+++++++++++++++++')
a2 = 18
print(a2 == 18) # True
print(a2 is 18) # True

array1 = [1, 2, 3]
array2 = [1, 2, 3]
print(array1 == array2) # True
print(array1 is array2) # False

b1 = 12
c1 = b1
print(c1 == b1) # True
print(c1 is b1) # True

###############################