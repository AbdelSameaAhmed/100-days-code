# Ex1
#  Write a Python function that takes a sequence of numbers 
# and determines whether all the numbers are different from each other.

# Solution
def checkDeff(Data):
    # data = []
    if len(Data) == len(set(Data)):

        return True
    else:
        return False
# check Function
print(checkDeff([1,5,7,9]))
print(checkDeff([2,4,5,5,7,9]))

print("*" * 80)
# ex2

# Write a Python function to find the Max of three numbers
# Solution
# ----------------------------------

def findMaxnum(num1, num2, num3):
    l1 = [num1, num2, num3]
    maxNum= max(l1)
    return f"The Max number of these three numbers is: {maxNum}"
# test function 
print(findMaxnum(num1 = 100, num2= 400, num3 =200))

print("*" * 80)
# ex2

#  Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7)
# Solution
# ----------------------------------

def sum_count(data):
    # data = [data]
    count = 0
    addition = 0
    for x in data:
        addition = addition + x
        count += 1
    return f"The sum of data list is: {addition}\nthe count of data element is: {count}"
# test function

print(sum_count([1,2,3,4,5,6]))
print("-" * 50)
print(sum_count([200,1,3,4,5,66,7,0,11]))


print("*" * 80)
# ex2
#  Write a Python function to multiply all the numbers in a list
# Solution
# ----------------------------------

def mult(data):
    m = 1
    for i in data:
        m = m*i
    return f"the multibly of data numbers is: {m}"
# test function 
print(mult([1,2,2,2,2,2]))