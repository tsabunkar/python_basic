# Python Language Features

- Dynamic, high level, free open source and interpreted programming language
  - Dynamic: we don’t need to declare the data-type of variable because it is a dynamically typed language (bocz variable is decided at run time).
  - high level: no need to manage the memory
  - interpreted: Python code is executed line by line at a time. unlike other languages C, Java. there is no need to compile python code
- supports object-oriented programming & procedural oriented programming paradigm
- The source code of python is converted into an immediate form called bytecode.
- Cross OS language (Windows, Linux, Unix, and Mac)
- Dynamic Typing: Variables can be reassigned with to any different data type, thus python is dynamically typed language. since variable can change type readily. other languages like c, java are statically typed where variables are stuck with their originally-assigned type

---

# Python3 v/s Python2

- Python-2 is legacy version and outdated and Python-3 is latest and future version of Python language
- Python-3 is not backwards compatible to Python 2 (but vice-versa is true)
- Python-3 Readiness: http://chhantyal.net/py3readiness/#.X48I5J0zZUw (Tells you list of packages that are now supported by Python)
- latest version of python would be build upon Python-3 only

---

# Install Python

- https://www.python.org/downloads/
- Documentation: https://docs.python.org/3/

---

# Run Python File

- python3 <file_name>

---

# Python Interpreter

- Python Interpreter is REPL to play with Python its not meant for projects

---

# Maths Operator

<!--
- + Addtion
- - Subtraction
- * Multiply
- / Divide
- ** Exponentiation
- % Modulo
- // Integer Division
-->

- PEMDAS (P- parentheses, E- exponent, M- multiplication, D- division, A- addition, S- subtraction)

---

# Comments

- Single line comment ==> #
- Python does not really have a syntax for multi line comments, but you can use a multiline string. Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code

---

# Variables

- Variables Must be assigned to some value before used ==> Error : NameError: name 'variable_name' is not defined
- Syntax- variable_name: type_name
- variables are like containers for storing data, pull it out later. They can hold all sorts of things like - number, boolean, string, etc
- variable in python is like a variable in mathematics: it is named symbols that holds a value
- Thinking like JAR
- variables are always assigned with the variable name on the left and then the value on the right of equals sign.
- variables must be assigned before they are used
- Naming Restriction:
  - variables must start with a letter or underscore
  - rest of the variable name must consist of letters, numbers or underscores
  - variable names are case-sensitive
- Naming Conventions/Style/Guide-lines:
  - variable should be lower_snake_case (betweeen words underscore)
  - variable should be lower cases
  - constants should be CAPITAL_SNAKE_CASE
  - Class name should be UpperCamelCase
  - variable that starts and ends with two underscores (called dunder for double underscore) are supposed to be private or should left alone ex-
  <!-- __no_touch__ -->

---

# Data Types

- Primitive Data type:
  - Boolean Type: bool
  - Numeric Types: int, float, complex
  - Text Type: str
- Secondary Data Type: (Data-Structures)
  - Sequence Types: list, tuple, range (Ordered sequence of values like array)
  - Mapping Type: dict (Collection of key/value pairs)
  - Set Type: set, frozenset
  - Binary Type: bytes, bytearray, memoryview
- Special Value: None (Similar to null in other languages)

---

# Strings

- String literals in python can be declared with either Single quotes or double quotes. (Just like JS)
- Escape Character/Sequence: this are meta-characters which get interpreted by python to do somthing special:
  - https://docs.python.org/3/reference/lexical_analysis.html#literals
- Formatting String: There are several ways to format a string in python to interpolate a variable. New way in Python3 is F-String
- String is indexed (ie- each character has indicies)

---

# Converting DataTypes

- Can explicitly convert data type of the variable by using the built-in type as a function
  a1 = 12.3423
  b1 = int (a1)

---

# Conditional Statements

- Syntax

```

if condition:
  _code_
elif condition:
  _code_
else:
  _code_

```

- Comparsion Operators: ==, !=, <, >, >=, <=
- Logical Operators: and, or, not

---

# Truthiness or Falseness

- Truthiness : Statements or expressions which resolve to true boolean value.
- Values can that can be resolved to boolean true is Truthy or value can be be resolved to boolean false is falsy
- Beside false condition checks, other things that are naturally falsy include: empty objects, empty String, None and Zero
- Difference between "==" v/s is: (Both are used to check condition oeprator) ==> Comparsion Operator
  - == only check for values are same?
  - is: check for values and stores in the same memory ('is' operator is only truthy if the vairables reference the same item in the memory)

---

# For Loops

- Syntax:

```

for item in iterable_object:
  # logic

```

- An iterable_object is like - collection of items, ex- a list of numbers, a string of characters, a range, etc.
- item is a temporary variable which reference the current position of our iterator with in the iterable. It will iterate over every item of the collection and then go away when it has visited all the items in the collection
- range(1,8) ==> Generates numbers from 1 to 7
- range() - think ranges as just a slice of number line.
  - If we want to print numbers we can simply iterate over range()
  - range(7) will give you integers from 0 to 6
  - range(1, 8) will give you integers from 1 to 7
  - range(1, 10, 2) will give you odds from 1 to 10
  - range(7, 0, -1) will give you integers from 7 to 1 (Third param is step ==> How many to skip, also +ve -> count up or -ve -> count down)

---

# While loops

- Anything that can be done by for loops can also be done by while loops.
- Something done by while loops cannot be done by for loops.
- While loops require extra care i.e- should have condition that will manually terminates.(If not termiate: It will be in infinite loops)
- Syntax:

```

while boolean_expression:
  # while above condition is truthy this block of code will be executed

```

- break- allows us to exit the loops (while, for) explicitly (whenever we want) <-- Controlled Exists

---

# Style Guide For Python

- pep-8 styleguide (python enhancement proposal)
- https://www.python.org/dev/peps/pep-0008/
- 4 space = 1 Indentation
- If you want to use auto-linting tool in VSCode: https://code.visualstudio.com/docs/python/linting
- In general you can use: autopep8 --in-place <file_name.py> (No separate installation required in linux)

---

# List

- Collection or grouping of items
- This ds is ordered collection of elements
- data structure is higher of data-type (Secondary data types) which is general stores the primary data-type in particular fashion (i.e- structured way)
- Lists in python (in js - array)
- list always starts counting at ZERO. Thus your first element lives at index-0
- slices can be used to make the copy of the list
- list comprehension is used everywhere when iterating over list, string, ranges, and more data types
- swapping is useful for sorting or shuffling

---

# Difference b/w functions and method

- function: function is a sequence of statements that execute in a certain order, given a name. They let us implement code reusability.
- Python Functions, we talked about built-in and user-defined functions. ex- len('ab'), type(a)
- Python method is like a function, except it is attached to an object. We call a method on an object, and it possibly makes changes to that object.
 A method, then, belongs to a class. ex: list1.sort(), [1,2,3].sort(), str1.upper()
- Basically methods depends on any object (in front/prefix of it), whereas functions are on its own.

---
