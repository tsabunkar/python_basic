list1 = ['tejas', 12, True, 6.777]

print(list1)
print('To know the number of the item in the list', len(list1))
# Another way of making the list using builtin function --> list()

r = range(1, 10)

print(r)
print(list(r)) # Converting range to a list --> so that we get list of numbers

colors = ['purple', 'red', 'yellow']

print(colors[0]) # Accesing the value inside the list
# print(colors[3]) # IndexError: list index out of range
print(colors[-1]) # list will start counting from backwards

# Check if the value exist in the list
print('yellow' in colors) # True
print('white' in colors) # False

# TO change the value inside the list
colors[0] = 'white'
print(colors)

print('_________________________')
# Accessing all the values in the list
# Using for loop
for color in colors:
    print(' **', color, ' **')

for x in range(1, 4):
    print(x)

# Using while loop
numbers = [2,4,56,9]
i = 0
while i < len(numbers):
    print(f'{i} :: {numbers[i]}')
    i += 1

print('_________________')

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

sounds_str_val = ''
for sound in sounds:
    sounds_str_val += sound.upper()

print(sounds_str_val)

print('_____METHODS OF LIST_____')

things = ['cpu_cabinate', 'mouse', 'keyboard']

# append() is a method of things object. NOTE: append is not function
print(things)
things.append('monitor')
print('After Append method ->', things)

#  extend() -> if we want to append multiple items then used this method
things.extend(['speaker', 'router'])
print('After extend -> ', things)

things.append(['mobile', 'charger'])
print('trying to append multiple -> ', things) # ['cpu_cabinate', 'mouse', .. , ['mobile', 'charger']]

# insert() -> Can insert at any given position using index
things.insert(2, 'books')
print('\n', things)

# clear() -> Will remove all the items from the list
things2 = things
print(things2)

things2.clear()
print('AFTER clear() method ran')
print(things2) # []
print(things) # [] the above copy is both -> by-value & by-address

# pop() -> remove the item from a given position in the list and return it
# if no index passed as params- then bydefault last item is popped out
books = ['deception point', 'da vinci code', 'origin']
books.pop(1)
print(books)
popped_item = books.pop()
print(books)
print(popped_item)

# remove() -> as an argument should pass -> item/value to be removed.
cs_books = ['algo clsr', 'db korth']

# cs_books.remove() # TypeError: remove() takes exactly one argument (0 given)
cs_books.remove('db korth')
# cs_books.remove('iejfi') # ValueError: list.remove(x): x not in list


arrays_nums = [1, 2, 4, 4, 4, 4, 3]

arrays_nums.remove(4)
print(arrays_nums) # [1, 2, 4, 4, 4, 3]   <-- Removes only the first occurrence of matched item as argument

















