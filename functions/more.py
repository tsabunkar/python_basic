# *args

def sum_all(num1, num2, num3):
    return num1 + num2 + num3


print(sum_all(2, 3, 4))


# !To add any number of dynamic arguments

def sum_all2(*nums):
    print(nums)  # printing like a tuple
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all2(2, 3, 4))
print(sum_all2(2, 3, 4, 5, 6, 7))


def ensure_my_names(*args):
    if 'tejas' in args and 'sabunkar' in args:
        return 'Welcome back my King!!'
    return 'Sorry you are not known to me'


print(ensure_my_names())
print(ensure_my_names(1, True, 'tejas', 'usha', 'sabunkar'))
