# import the random module for generating pseudo random nunmbers
import random

print("Welcome to the guessing game!")
number_of_guesses = 3
user_won = False

# define range of random numbers, (lowest, highest)
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:

    # User Guesses
    user_guess = input("guess the number: ")
    user_guess = int(user_guess)

    if user_guess == correct_answer:
        print("Good Guess")
        print("You are correct!")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("Too high!")
    elif user_guess < correct_answer:
        print("Too low!")

    number_of_guesses -= 1

if user_won == True:
    print("You Win!")
else:
    print("You Lose!")
    print("The correct answer was " + str(correct_answer))