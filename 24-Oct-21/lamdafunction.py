# lambda --------------------------
# ---------------------------------
# ex1
# ----------------
# wite function take 2 numbers and return averafe

def ave(x, y):
    return (x+y)/2
# test function
print(ave(2,8))



print("*"*80)
# using lambda
print((lambda x,y: (x+y)/2)(2,8))

print("*"*80)
print("*"*80)
# ex2
# ----------------

# 1 Write a Python program to create a lambda function that
#  adds 15 to a given number passed in as an argument,
# 2 also create a lambda function 
# that multiplies argument x with argument y and print the result.

# solution
# 1
print((lambda x : (x + 15)) (20))
# 2
print((lambda x, y: (x*y))(2,2))
print("*"*20)
print("another style of sybtax")
# another style
# 1
result = lambda x: x +15
print(result(20))
# 2
a = lambda x, y : x*y
print(a(2,2))

print("*" * 80)


# ex3
# ----------------
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# solution 
# ---------------------
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)