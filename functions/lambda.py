def square(num):
    return num * num


print(square(9))

# Above function can be converted to lambda syntax (Anonymous functions)

square2 = lambda num: num * num
print(square2(6))

print(square.__name__)  # print of the function -> square
print(square2.__name__)  # <lambda>

add = lambda a, b: a + b
print(add(2, 3))

# Map

nums = [1, 2, 3, 4]
double = map(lambda num: num * 2, nums)
print(double)  # <map object at 0x7f4ec3f39b20>
# for d in double:
#     print(d)
print(list(double))
print(list(double))  # NOTE: map object can only be iterated one time

people = ['tejas', 'usha', 'Shailesh']
upper_case_people = map(lambda p: p.upper(), people)
print(list(upper_case_people))
