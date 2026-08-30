import random
print('Die rolling game')
while True:
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    roll=input('do you want to roll the dice (y,n):').lower()
    if roll=='y':
        print(f'({die1},{die2})')
    elif roll=='n':
        print('Thanks for playing!')
        break
    else:
        print('enter valid input(y,n)')
