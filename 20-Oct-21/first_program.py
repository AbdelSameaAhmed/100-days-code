

# program can guess numbers
# program generate a random number
# user guess the Number
# program return TRUE or FALSE
# program continue untill user exit useing "done" key word.

# Solution
# # -----------------

# # import required modules()
# import os
# from random import randint, random
# import string

# # create function return a rondom number

# progNumber = randint(1, 100)
#     # recieve a guessed number from user 
# guessedNumber = input("please enter your guessed number")

# # print(progNumber)
# while guessedNumber:
#     try:
#         guessedNumber = int(guessedNumber)
#         if guessedNumber != progNumber:
#             print("wrong you guessed wrong number, try again ...")
#             guessedNumber = input("please enter your guessed number")
#         elif guessedNumber == progNumber:
#             print("correct you guessed the true number")
            
#             user = input('please type q to exit or c to continue')
#         elif user == 'q' or user == 'Q' or user == 'quit' or user == 'Quit':
#             os.exit()
#         elif user == 'c' or user == 'C' or user == 'continue' or user== 'Continue':
#             guessedNumber = input("please enter your guessed number")
#     except :
#         print("please enter valid number: ")

# Wrong program


import os
from random import randint, random

progNumber = randint(1, 100)
    # recieve a guessed number from user 
guessedNumber = int(input("please enter your guessed number: "))
try:
    # guessedNumber = int(guessedNumber)
    while Type(guessedNumber) == int:
    # if guessedNumber != progNumber:
        if guessedNumber > progNumber:
            print("very high number")
        elif guessedNumber < progNumber:
            print("very low number")
        if guessedNumber == progNumber:
            print("excellent.. you enter correct number")
except :
    print('ERROR ... please enter valid number')