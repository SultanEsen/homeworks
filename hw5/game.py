import os
from envparse import env
from random import choice

env.read_envfile('options.env')
start_balance = int(os.environ.get('MY_MONEY'))
start_balance_2 = int(os.environ.get('MY_MONEY_2'))
# print(start_balance)
# print(start_balance_2)

a = list(i for i in range(1, 6))
b = list(i for i in range(6, 11))
c = list(i for i in range(11, 16))
d = list(i for i in range(16, 21))
e = list(i for i in range(21, 26))
f = list(i for i in range(26, 31))
# random_slot = choice([a, b, c, d, e, f])
# print(random_slot)

def game():
    round_balance = int(start_balance_2)
    answer = 'y'
    print('Welcome to Casino Las Vegas!')
    while answer == 'y':
        random_slot = choice([a, b, c, d, e, f])
        # print(random_slot)
        print(f'Your balance is {round_balance} USD')
        n = int(input('Enter your lucky number from 1 to 30: '))
        s = int(input('How much money are you putting into game: '))
        if n in random_slot:
            s = s * 2
            round_balance += s
            print(f'Congrats! You have won {s} USD! Your balance is {round_balance} USD')
        else:
            round_balance -= s
            print(f'You lost {s} USD! Your balance is {round_balance} USD')
        answer = input('\nWill you play one more time? Type "y" or "n": ')
    if answer != 'y':
        if round_balance > start_balance_2:
            print(f'Your current balance is {round_balance} USD! You won {abs(start_balance_2 - round_balance)} USD')
        elif round_balance < start_balance_2:
            print(f'Your current balance is {round_balance} USD! You lost {start_balance_2 - round_balance} USD ')