# *args

def sum_all(num1, num2, num3):
    return num1 + num2 + num3


print(sum_all(2, 3, 4))


# !To add any number of dynamic arguments

def sum_all2(*nums):
    print(nums)  # printing like a tuple -> (2, 3, 4)
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

print('##### kwargs ####')


# **kwargs


def fav_colors(**kwargs):
    print(kwargs)  # printing like a Dictionary -> {'tejas': 'red', 'usha': 'green', 'shailesh': 'black'}
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(tejas='red', usha='green', shailesh='black')


def special_greeting(**kwargs):
    if "tejas" in kwargs and kwargs["tejas"] == 'sabunkar':
        return "You are very special person"
    elif "tejas" in kwargs:
        return f"{kwargs['tejas']} run"
    return "Not sure why u exist?"


print(special_greeting(tejas='sabunkar'))
print(special_greeting(tejas='hero'))
print(special_greeting(usha='sabunkar'))
