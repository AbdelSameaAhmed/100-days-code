import os
from random import randint
print(os.getcwd())

# create function called getUserPoint()
def getUserPoint(userName):
    try:
        userfile = open('userScores.txt', 'r')
        for line in userfile:
            content = line.split(',')
            if content[0] == userName:
                userfile.close()
                return content[1]
        else:
            userfile.close()
            return "-1"
    except:
        print("file connot be opened")


print(getUserPoint("Benny"))
