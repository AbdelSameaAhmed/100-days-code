# -------------------------------------------------
# Data TYPE 
# -------------------------------------------------
print("*"*60)
# NUMBER
i = 100 # integer
print(type(i))
print("*"*30)
f = 100.309 # float
print(type(f))
print("*"*30)
s = 'python'
a = 100
print(type(s))
print("*"*30)

# Complex composed of 2 parts real part and imaginary part
# import math
x = complex(1, 2)
print(type(x))
print(x)
print("*"*60)

# Self-assignment
# -------------------------------------------
count = 0
count += 2
print(count)

print("*"*30)
d = 4
d -= 2
print(d)

print("*"*30)
b = 2
b *= 2
print(b)

print("*"*30)
a = 5
a **= 2
print(a)
# from sys import argv
print("*"*60)
print("*"*30)
xx =15
def var_test():
    xx = 25
    return xx
var_test()
print(xx)
print("*"*60)
print("*"*30)
# print(f"Python {3 + .2}")

var_test = "Jhones" * 3 * 2 
print(var_test)
