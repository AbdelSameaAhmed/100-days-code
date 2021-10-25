# ------------------------
# Lambda Fuction ---------
# ------------------------

# Write a Python program to filter a list of integers using Lambda
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# Solution
# -----------------------
even_num = list(filter(lambda x : x %2 ==0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("the even number list is: ")
print(even_num)
print("*"*60)
print("the odd number list is: ")
odd_num = list(filter(lambda x : x%2 !=0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(odd_num)
print("*"*60)

#  Write a Python program to square and cube every
#  number in a given list of integers.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# solution
# ----------------------------
squarefun =list(map(lambda x : x**2,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("squar numbers are: ")
print(squarefun)

cubfun =list(map(lambda x : (x**3),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("cub numbers are: ")
print(cubfun)

print("*"*60)