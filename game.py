#Import Python Module - Generates a Random Number
import random 

# Create a function to create a random number between 1 and 10
def guess_number():
    return random.randint(1, 10)

#Players Details
player_name = input("Hello, What's your name?")

# Number of guesses variable
number_of_guesses = 0

print(f'okay! {player_name} I am Guessing a number between 1 and 10:')

# Get the random number
number = guess_number()

#While Loop
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        print(f"Congratulations, {player_name}! You guessed the number in {number_of_guesses} guesses!")
        break
        
if number_of_guesses == 5 and guess != number:
    print(f"You did not guess the number, {player_name}. The number was {number}.")