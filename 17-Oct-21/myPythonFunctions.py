import os
from random import randint
print(os.getcwd())

# create function called getUserPoint()
def getUserPoint(userName=""):
    try:
        userfile = open("userScores.txt", "r")
    except:
        print("file cannot be opened")

    for line in userfile:
        line = line.split()
        if userName in line:
            return line
            df.close()
    else:
        userfile.close()
        


getUserPoint(userName = "Ann")
