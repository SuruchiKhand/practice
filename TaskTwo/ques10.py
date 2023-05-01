# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as

# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1

# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.


import random

counter = 0
number = random.randint(1,5)

guess = None

while counter <= 5:
    guess = input("Guess the lucky number between 1 and 5:   ")
    guess = int(guess)
    counter += 1

    if guess == number:
        print("Good Guess!")
        break

    else:

        if counter == 5:
            print("Game over")
            break

        else:
            print("Try again!")
       
        