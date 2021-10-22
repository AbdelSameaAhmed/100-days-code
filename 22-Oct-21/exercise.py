def swaplist(a, b):
    y = a
    a = b
    b = y
    return f'the value of a is{a} and the value of b is {b}'


# test
print(swaplist(a =[1, 2, 4] , b = ['qq', 'ww', 'rr']))



# ex
# define a function called sign which takes a numerical argument and 
# returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.


def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    elif num == 0:
        return 0
# Check your answer
print(sign(0))
print(sign(-10))
print(sign(100))

# ex
# find largest number among 3 numbers

def findlargest(a, b, c):
    l1 = [a, b, c]
    largest = max(l1)
    return largest
print(findlargest(1, 3, 2))

# ex 

