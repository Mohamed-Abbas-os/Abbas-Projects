import random
def numbergame():
    print('Number guessing game :')
    play_again='y'
    while play_again.lower()=='y':
        number=random.randint(1,100)
        attempts=0
        guess=0
        while guess!=number:
            try:
                guess=int(input('Enter number (1 to 100):'))
                attempts+=1
                if guess<number:
                    print('too low')
                elif guess>number:
                    print('too high')
                else:
                    print(f'congratulations you guessed it in {attempts} attempts')
            except ValueError:
                print('Enter a valid number')
        play_again=input('Do you want to play agin (y,n):')
        if play_again=='n':
            print('thanks for playing!')
numbergame()