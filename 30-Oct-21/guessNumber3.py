
import random

def guessN(x):
    rando_number = random.randint(1, x)
    guess = 0
    while guess != rando_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > rando_number:
            print("Sorry you guessd wrong .. very high")
        elif guess < rando_number:
            print("Sorry you guessd wrong .. very low")
    print(f"Yes, You guessd true number{random.random}")

guessN(100)