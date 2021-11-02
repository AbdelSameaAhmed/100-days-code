# --------
# guss number
# --------

# project describtion
# program generate number between 1 and 199
# user guess the number
# program check if number is valid or not
# program compare between the gussed number and generated Number

import random

generateNumber = random.randint(1, 100)
print(generateNumber)
guessednumber = input('please enter number: ')
try:
    guessednumber = int(guessednumber)
    while True:
        if guessednumber == generateNumber:
            print('True you guessed the true number..')
            break
    else:
        guessednumber = input('please enter number: ')
        while guessednumber != generateNumber:
            if guessednumber > generateNumber:
                print('Wrong, very high!..  try again')
                guessednumber = input('please enter integer number: ')
            else:
                guessednumber < generateNumber
                print('Wrong, very low!..  try again')
                guessednumber = input('please enter integer number: ')
            
except Exception as e:
    print(str(e))