''' game finding a secret number within 3 attempts using while loop'''
import random
number = random.randint(1, 10)
number_of_guesses = 0
while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print(' Try again')
    if guess > number:
        print('Try again')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))