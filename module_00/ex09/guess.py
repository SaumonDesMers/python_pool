from random import randint


print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!''')

N = randint(1, 99)
guess = 1

while True:
    str = input('\n>> ')

    if str == 'exit':
        print('Goodbye!')
        exit()
    elif not str.isnumeric():
        print('This is not a number')
    elif int(str) == N:
        if N == 42:
            print('The answer to the ultimate question of life, the universe and everything is 42.')
        if guess == 1:
            print('Congratulations! You got it on your first try!')
        else:
            print('Congratulations, you\'ve got it!')
            print('You win in {} attemps!'.format(guess))
        exit()
    else:
        print('Too high!' if int(str) > N else 'Too low!')
        guess += 1
