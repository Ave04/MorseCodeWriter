import random as r

rock = 1
paper = 2
scissors = 3

computer = r.randint(1,3)
user_input = int(input('Choose any number between 1 and 3(inclusive): '))


if computer == user_input:
    print(f'draw, computer chose {computer}')
elif computer == user_input - 1 or (user_input == 1 and computer == 3):
    print(f'win, computer chose {computer}')
else:
    print(f'You lost, computer chose {computer} vs your {user_input}')

