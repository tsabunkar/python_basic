# Python Language Features

- Dynamic, high level, free open source and interpreted programming language
  - Dynamic: we don’t need to declare the data-type of variable because it is a dynamically typed language (bocz variable is decided at run time).
  - high level: no need to manage the memory
  - interpreted: Python code is executed line by line at a time. unlike other languages C, Java. there is no need to compile python code
- supports object-oriented programming & procedural oriented programming paradigm
- The source code of python is converted into an immediate form called bytecode.
- Cross OS language (Windows, Linux, Unix, and Mac)

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
  - variable should be snake_case (betweeen words underscore)
  - variable should be lower cases
  - constants should be CAPITAL_SNAKE_CASE
  - Class name should be UpperCamelCase
  - variable that starts and ends with two underscores (called dunder for double underscore) are supposed to be private or should left alone ex-
  <!-- __no_touch__ -->

---
