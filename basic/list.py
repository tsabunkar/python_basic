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

##################################

dan_brown_books = ['deception point', 'da vinci code', 'origin']

# index - return the index/position but take args as param
print(dan_brown_books.index('origin'))
# print(dan_brown_books.index('ef')) # ValueError: 'ef' is not in list

nums_array = [5, 5, 6, 7, 8, 5, 9, 6,  2]
print(nums_array.index(5))
print(nums_array.index(5, 1)) # (o/p- 1) finds the index after the start point -> 1
print(nums_array.index(5, 2)) # (o/p- 5)
print(nums_array.index(6, 1, 4)) # (o/p- 5) start = 1 and end = 4

# count - number of times occurred
print(nums_array.count(5)) # 3
print(nums_array.count(111)) # 0 (bcoz does not present)

# reverse - reverse order of the list in-place (does not create a duplicate)
print(dan_brown_books.reverse()) # None
print(dan_brown_books) # ['origin', 'da vinci code', 'deception point']

# sort - alphabetical sorted, ascending order for nums (in-place)
print(dan_brown_books.sort())
print(dan_brown_books)

# join - it is the string method not a list method
# it returns a new string <-- NOTE
words = ['coding', 'is', 'fun']
print(' '.join(words))
full_name = ['tejas', 'shailesh', 'sabunkar']
print('.'.join(full_name))

##################################

# SLICING
# helps to create the copy of the entire/portion of the source list







