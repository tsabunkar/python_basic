from random import choice, randint

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
""" 
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

 """
################################################################


total_count = 0
user_win_count = 0
ai_win_count = 0
winning_series = 3  # Best of 3 games

while total_count < winning_series:
    total_count += 1
    artificial_input = choice(['rock', 'paper', 'sicssor'])
    user_input = input('(enter your choice): ')

    if artificial_input == 'rock' and user_input == 'sicssor':
        print('AI wins' + f' AI choosed {artificial_input}')
        ai_win_count += 1
    elif artificial_input == 'sicssor' and user_input == 'paper':
        print('AI wins' + f' AI choosed {artificial_input}')
        ai_win_count += 1
    elif artificial_input == 'paper' and user_input == 'rock':
        print('AI wins' + f' AI choosed {artificial_input}')
        ai_win_count += 1
    elif artificial_input == user_input:
        print('Its a Draw')
    else:
        print('user wins' + f' AI choosed {artificial_input}')
        user_win_count += 1

if user_win_count > ai_win_count:
    print('FINAL WINNER IS: USER')
elif user_win_count < ai_win_count:
    print('FINAL WINNER IS: AI')
else:
    print('Both Played well its a draw')
