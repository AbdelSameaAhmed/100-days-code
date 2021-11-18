# ----------------------------------------
# --- learn python by excercise__2 -------
# ----------------------------------------

# ex7
# --------------------------------------
# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# --------------------------------------

def testNum(num):
    return (abs(1000-num) <= 100 or abs(2000-num) <= 100)

print(testNum(900))
print(testNum(22000))

print("*" * 60)
# ex8
# --------------------------------------
# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.
# --------------------------------------
def sumnumners(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum *= 3
    return sum

# test function
print(sumnumners(1,2,3))
print(sumnumners(20,20,20))

print("*" * 60)
# -----------------------------
# ex9
# Write a Python program to get a new string from a given string where
# "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

def creatstring(l1=''):
    if l1[0:2] == "Is":
        return l1

    else:
        new_st = 'Is' + ' ' + l1
        return new_st

print(creatstring("there is anything else"))
print(creatstring("Is there is anything else "))

# l1 = "Is there is anything else"
# print(l1[0:2])

print("*" * 60)
# -----------------------------
# ex10
# Write a Python program to get a string which is 
# n (non-negative integer) copies of a given string.
def strcopies(st, n):
    result = ''
    for i in range(n):
        result = result + st
    return result
    
print(strcopies("abd", 3))
print(strcopies("sfg", 2))


print("*" * 60)
# -----------------------------
# ex11
# Write a Python program to find whether a given number 
# (accept from the user) is even or odd, print out an appropriate message to the user
def odd_or_even(num):
    if num % 2 ==0:
        return f"{num} is even number"
    return f"{num} is odd number"

# check function
print(odd_or_even(10))
print(odd_or_even(3))

print("*" * 60)
# -----------------------------
# ex11
# Write a Python program to count the number 4 in a given list.
