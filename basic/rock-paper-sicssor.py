
#####################
""" 

print('.....rock.....')
print('.....paper.....')
print('.....sicssor.....')

player1 = input('(enter Player-1"s choice): ')
print('****NO CHEATING!\n' * 20)
player2 = input('(enter Player-2"s choice): ')

if player1 == 'rock' and player2 == 'sicssor':
    print('Player1 wins')
elif player1 == 'sicssor' and player2 == 'paper':
    print('Player1 wins')
elif player1 == 'paper' and player2 == 'rock':
    print('Player1 wins')
else:
     print('Player2 wins')

 """
################################################################

from random import choice, randint
 
artificial_input = choice(['rock', 'paper', 'sicssor'])
user_input = input('(enter your choice): ')

if artificial_input == 'rock' and user_input == 'sicssor':
    print('AI wins' + f' AI choosed {artificial_input}')
elif artificial_input == 'sicssor' and user_input == 'paper':
    print('AI wins' + f' AI choosed {artificial_input}')
elif artificial_input == 'paper' and user_input == 'rock':
    print('AI wins' + f' AI choosed {artificial_input}')
elif artificial_input == user_input:
    print('Its a Draw')
else:
    print('user wins' + f' AI choosed {artificial_input}')