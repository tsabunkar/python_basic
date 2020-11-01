# New way to create a list
nums_list = [1, 2, 3]
result = [x * 10 for x in nums_list]  # Syntax of list comprehension
print(result)

# Traditional way of doing same thing as above
result2 = []
for x in nums_list:
    result2.append(x * 10)  # There is no push for list in python

print(result2)

# Example-2
name = 'Tejas'
names_char_array = [ch.upper() for ch in name]
print(names_char_array)  # ['T', 'E', 'J', 'A', 'S']

# Example-3
names = ['tejas', 'shailesh', 'sabunkar', 'usha']
result_names = [name[0].upper() + name[1:] for name in names]
print(result_names)

# Example-4
print([num * 10 for num in range(1, 6)])

# Example-5 (boolean representation of each value)
print([bool(ele) for ele in [0, [], '', 1, 'Tejas', {}]])  # [False, False, False, True, True, False]

# Example-6 convert to string
print([str(ele) for ele in [1, 2, 3, 4]])

# !List Comprehension with condition
numbers_list = [1, 2, 3, 4, 5]
even = [x for x in numbers_list if x % 2 == 0]
odd = [x for x in numbers_list if x % 2 != 0]
print(f'list of even numbers: {even}')
print(f'list of odd numbers: {odd}')

# Example:2 (Multiply even numbers and Divide odd numbers)
results_list = [x * 2 if x % 2 == 0 else x / 2 for x in numbers_list]
print(results_list)

# Example:3
with_vowels = 'Python is really fun language to learn'
result_str = ''.join([ch for ch in with_vowels if ch not in 'aeiou'])
print(result_str)
