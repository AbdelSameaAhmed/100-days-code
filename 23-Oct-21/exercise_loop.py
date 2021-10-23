# --------------------------------------
# by exercises
# ---------------------------------------

# exercis
# Write a Python function that takes a sequence of numbers
# and determines whether all the numbers are different from each other

# solution
# -----------------------------------------
print("*" * 80)
def checknum(num1, num2, num3):
    numbers_1 = [num1, num2, num3]
    # count = len(numbers_1)
    for num in numbers_1:
        if numbers_1[0] != numbers_1[1] and numbers_1[0] != numbers_1[2]:
            if numbers_1[1] != numbers_1[2]:
                print("")
            print("these list is different")
        else:
            print("there is at leat one match")

# check function
# The following solution from:
# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.php

print(checknum(1, 1, 2))

# better solution

def chekdistnict(data):
    data = list(data)
    if len(data) == len(set(data)):
        return True
    else:
        return False
# check Function
print(chekdistnict(data = [3,3,4,5,6,7,8]))
print("*" * 80)
print("*" * 80)
# ---------------------------------------------------
l1 = [1, 2, 4, 5, 5, 8,10, 3, 2, 1]
l2 = set(l1)

print(l1)
print(l2)
print(f"the lenght of l1 is: \'{len(l1)}\'")
print(f"the lenght of l1 is: \'{len(l2)}\'")
# ----------------------------------------------------


print("*"*80)
# exercise
# write program return x**2 for each number in range of 1 to 5

m = {1,2,3,5,4}
for i in m:
    i = i**2
    print(i)

# another simple way

print("*"*80)
m = {x**2 for x in range(1,6)}
print(m)
print("*"*80)
print({x**2 for x in range(1,6)})