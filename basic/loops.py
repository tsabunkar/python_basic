# For loops

for i in "Tejas":
    print(i)

###############################
print('Range')

for i in range(1,8):
    print(i)

###############################

#! Range
print(list(range(0,10)))
print(list(range(1,10, 2)))
print(list(range(0,7, 1)))
print(list(range(7,0,-1)))

###############################

numTimes = input('How many times should I tell you?')
for i in range(int(numTimes)):
    print(f'Read for today {i}')

###############################

for i in range(1, 21):
    if i == 4 or i == 13:
        print(f'{i} is unlucky')
    elif i % 2 == 0:
        print(f'{i} is even ')
    elif i % 2 != 0:
        print(f'{i} is odd')

###############################

# !While loops

""" 

while True:
    print('Infinite Loop')

 """


# password cracker
""" 
password = input('What is the password?')
while password != 'tejas':
    print('Wrong, Please try again')
    password = input('what is the password?')
print('Correct, Welcome to Tejas World')

 """
###############################

# !similar code in while and for loop

for i in range(1, 11):
    print(i)

print('_____')

i = 1
while i< 11:
    print(i)
    i += 1


###############################

# Print Emojis in Mountain
# emoji = print("\U0001f600")

""" 
😀
😀😀
😀😀😀
😀😀😀😀
😀😀😀😀😀
😀😀😀😀😀😀
😀😀😀😀😀😀😀
😀😀😀😀😀😀😀😀
😀😀😀😀😀😀😀😀😀
"""

for i in range(1, 11):
    j = i
    while j:
        print("\U0001f600", end='')
        j-=1
    print('\n')
    
# !Alternatively (Using String Multiplication)

for i in range(1, 11):
    print("\U0001f600" * i) # print() * i ==> is also like a loop

# !Alternatively

i = 1
while i < 11:
    print("😀" * i)
    i+=1


###############################

# Stop Copying me

""" 

sentence = input('Please provide input \n')

while sentence != 'you win':
    print(sentence)
    sentence = input()
print("Thanks for confronting")

 """

# ! Alternatively

sentence = input('Please provide input \n')

while sentence != 'you win':
    sentence = input(f'{sentence}\n')
print("Thanks for confronting")



###############################


