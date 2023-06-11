#Import Python Module - Generates a Random Number
import random 

#Use Random Module To Generate No. Between 1-10, Store in Variable Number.
number = random.randint(1, 10)

#Players Details
player_name = input("Hello, What's your name?")

#No. Guesses Variable
number_of_guesses = 0

print(f'okay! {player_name} I am Guessing a number between 1 and 10:')

#While Loop
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' guesses!')
else:
    print('You did not guess the number, The number was ' + str(number))