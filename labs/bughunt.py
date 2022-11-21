# daniel roberts
# bughunt.py
# 11/14/2022
# bug hunt
import random
playing=True

# outer loop:
while playing==True:
    solved=False
    maximum=int(input("What should the maximum number be? "))
    chosenRandom=random.randint(1, maximum)
    # print(chosenRandom) \t

    guess=int(input("Please guess a number from 1 to "+ str(maximum) + ": "))
    # inner loop:
    while solved==False:
        if guess < chosenRandom:
             guess=int(input("Too low! Please try again: "))
        elif guess > chosenRandom:
            guess=int(input("Too high! Pleae try again: "))
        else:
            print("Good job! the number was " + str(chosenRandom) + "!")
            solved=True

    playagain=input("Thanks for playing! would you like to play again? (y/n): ")
    if playagain.lower()=='n':
        playing=False