# !Tuples
x = (1, 2, 3)
print(x)
print(type(x))  # <class 'tuple'>
print(1 in x)
print(x[0])  # Trying to access first item in the tuples (just like a list)
# x[0] = 23 # TypeError: 'tuple' object does not support item assignment
# This is bcoz are tuples are immutable in nature thus above we cannot modify value inside the x

# ! Tuples are commonly used for UNCHANGING data (immutable) ex-

# Creating Tuples -> tuple() or () bracket
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

weeks = tuple(('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'))

# Accessing Tuples
print(weeks[2])
print(weeks[-1])

copy_weeks = weeks
print(copy_weeks)

location = {
    (10.32, 24.24): 'Bangalore',  # using tuples as key, list cannot be used as key
    (43.768, 56.75): 'korea'
}

print(location[(10.32, 24.24)])

person = {
    'name': ' Tejas',
    'is_male': True
}

print(person.items())  # gives you tuples

# Iterate with tuples

friends = ('shailesh', 'sabunkar', 'tejas')
for name in friends:
    print(name)

print('______while______')
i = len(friends) - 1
while i >= 0:
    print(friends[i])
    i -= 1

# tuples builtin Method

# !count() - returns the times a value appears in a tuple
x = (1, 2, 3, 4, 2, 1)
print(x.count(1))  # Gives the count of 1
print(friends.count('tejas'))

# !index() -return the index at which a value is found in tuple
print(x.index(1))
print(friends.index('tejas'))
