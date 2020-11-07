# ! Create a set

x = set((1, 2, 3, 4, 5, 5, 5))
print(x)  # {1, 2, 3, 4, 5} <- Set will remove all duplicates

# Another way of creating a set
y = {1, 2, 3, 4, 5, 5, 5}
print(y)

print(5 in y)
# print(y[0]) # TypeError: 'set' object is not subscriptable
print(type(y))  # <class 'set'>

val = {1, 'a', True, 'd'}

print(val)  # {'d', 1, 'a'} <-- Order is changed and also True is converted to 1 (duplicate removed)

print({1, True})  # {1}
print({True, 1})  # {True}

# print({'a', [1, 2, 3]}) # TypeError: unhashable type: 'list'

# print({'a', {'b': 'tell'}})  # TypeError: unhashable type: 'dict'

# !Iterate over set
print('_________')
for v in val:
    print(v)

# ! Convert list to Set

cities = ['Bangalore', 'Mumbai', 'Bellary']
print(set(cities))  # {'Bellary', 'Bangalore', 'Mumbai'}
print(list(set(cities)))

# ! Builtin method in set

# ! add() -> adds elements to set, if already present then does not add
friends = {'tejas', 'shailesh', 'sabunkar'}
friends.add('Chennai')
print(friends)

# !remove() -> remove a value from the set, return keyError if value not found
friends.remove('sabunkar')
print(friends)

# friends.remove('Ram') # KeyError: 'Ram'

# If need to avoid keyError --> .discard()

friends.discard('Ram')

print(friends)

# ! copy() -> create a copy of the set
another_friends = friends.copy()
print(another_friends == friends)  # True
print(another_friends is friends)  # False (not pointing to same address)

# !clear() -> deletes all the items in the set
print(another_friends)
another_friends.clear()
print(another_friends)

# ! Set Math Operation

math_student = {'tejas', 'shailesh'}
computer_student = {'usha', 'tejas'}

# Union of two sets
print(math_student | computer_student)  # {'usha', 'shailesh', 'tejas'} <- no duplicate

# intersection (Common items b/w both sets)
print(math_student & computer_student)  # {'tejas'}

# ! Set Comprehension

print({x ** 2 for x in range(10)})  # set

print({x: x ** 2 for x in range(10)})  # dictionary

print({char.upper() for char in 'hello'})  # {'H', 'L', 'E', 'O'}


def are_all_vowels(string_value):
    return len({char for char in string_value if char in 'aeiou'}) == 5


print(are_all_vowels('uieoa'))
print(are_all_vowels('ueoa'))  # length is 4 -> False
print(are_all_vowels('aeiof'))  # not vowel -> False
