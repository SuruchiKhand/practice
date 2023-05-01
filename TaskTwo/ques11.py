# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

import random

counter = 0
number = random.randint(1,5)

guess = None


while counter <= 5:

    try: 
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

    except ValueError:
        print("Sorry but that was not very successful.")
        
        