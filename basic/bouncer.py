# Ask for age

ageStr = input('How old are you? \n')

if ageStr: #  age != '' (Check Truth of String --> Also check empty str)
    age = int(ageStr)
    if age>=18 and age<=21:
        print('Wistband')
    elif age>21:
        print('Normal Entry')
    else:
        print('You are too young')
else:
    print('Please enter an Age it cannot be empty')



################################################################

from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)         
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /



# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(str(x) + ' ' + str(y))

if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")


################################################################


# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

if (actually_sick and sick_days > 0) or (kinda_sick and hate_your_job and sick_days > 0):
    calling_in_sick = True
else:
    calling_in_sick = False

print(calling_in_sick)