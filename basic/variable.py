x = 100
y = 25
print(x + y)

print(x * 3)

y = 50

print(x + y)

# in python we can assign variables in one line
a, b = True, False

print(a)


# Data Types

is_male = True # IT is Capital True not true <-- Remeber about boolean
print(is_male)

first_name = 'tejas'

print(first_name)
print(type(first_name))

last_name = "Shailesh Sabunkar" # Single quotes is same as single quotes for String (just like js)

print(last_name)

# !Special Value- None

child_name = None

print(child_name)
print(type(child_name)) # <class 'NoneType'>


msg = "He said 'hello there!'"
print(msg)

line = 'tejas \n sabunkar'
print(line)

# Print this Mountain: /\/\/\
print('/\\/\\/\\')

quotation = "My cat said \"meow\""
print(quotation)

print(first_name + ' ' + last_name)

# print(8 + 'hello') # !TypeError: unsupported operand type(s) for +: 'int' and 'str'

greeting = None
name = None
greet_name = None

greeting = 'hello'
name = 'Heisenberg'
great_name = greeting + ' ' + name

print(great_name)


# F-String (String Interpolate)

x = 10
formatted = f"I have variable called {x + 1}"
print(formatted)

# Another way of interpolating a variable
y = 20
formatted2= "I have variable called {}".format(y)
print(formatted2)


################################################################

first = None
last = None

formattedStr = None

first = "Tejas"
last = "Sabunkar"

formattedStr = "First name : {}, last name: {}".format(first, last)
print(formattedStr)

# !String is indexed

print('Sabunkar'[0])
print('Tejas'[-2])