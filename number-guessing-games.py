# python number guessing game
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0 

is_running = True

print("This is a python number guessing game.")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    else:
        print("Invalid guess")
        print(f"Please guess a number between {lowest_num} and {highest_num}")
        continue
    
    if guess < lowest_num or guess > highest_num:
        print("Your guess is out of range, try again!")
        print(f"Please guess a number between {lowest_num} and {highest_num}")

    elif guess < answer:
        print("Too low!, try again!")

    elif guess > answer:
        print("Too high!, try again!")

    else:
        print(f"You got it right, the answer was {answer}")
        print(f"Number of guesses: {guesses}")
        is_running = False
