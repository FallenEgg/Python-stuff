import math
import random

#Taking inputs
    #generate lower  and higher bounds
lower = int(input("Enter lower bound number:- "))

upper = int (input("Enter higher bound number:- "))

x = random.randint(lower, upper)
print("\nt You've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer")

#initialize number of guesses
count = 0

#calculation of minimum number of guesses (depends on range)
while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))

    #Conditions
    if x == guess:
        print("Congratulations you did it in ", 
            count, " try")
        break

    elif x > guess:
        print ("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

#if guessing is more than required guesses
#show this output

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("Better luck next time")