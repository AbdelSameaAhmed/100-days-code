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
# print(generateNumber)
guessednumber = input('please enter number: ')
try:
    guessednumber = int(guessednumber)
    while guessednumber != generateNumber:
        guessednumber = input('please enter integer number: ')
        print('Wrong!.. try again')
    else:
        if guessednumber == generateNumber:
            print('True you guessed the true number..')
except Exception as e:
    print(str(e))
        

