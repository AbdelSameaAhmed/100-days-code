
# ----------------------------
# if else statement ---------------
# ----------------------------
print("*" * 50)
x = False
y = True
if x or y:
    print(' True')
elif x and y:
    print("False")
else:
    print("nothing")
print("*" * 50)
# ----------------------------
# if else statement in one line
# ----------------------------
a = 10
b = 2

result = (a*b if a > b else a/b)

print(result)

print("*" * 50)
# ------------------------
# if not 

z = 10 
print(z)

if not z == 10:
    print('the value of z defferent from 10')
else:
    print('the value of x is equal to 10')
# -----------------------------
print("*" * 50)

# --------------------------------
# ----------- for loop -----------
# --------------------------------
print("*"*50)
# print("//"*30)
# ex1
# count odd numbers and even numbers in specific sries list
numbers = [3, 4, 5, 6, 7, 8, 9, 11, 13, 17] # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
    if x % 2== 0:
        count_odd+=1
    else:
        count_even+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

print("*" * 50)
# ex2
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],\
    {"class":'V', "section":'A'}]
# print(datalist)
for i in datalist:
    print(f"the item is {i} and its type is {type(i)}")

print("*" * 50)
# ex3
# iterates for Dict
# return key and value
print("return key and value")
color = {"c1": "Red", "c2": "Green", "c3": "Orange"} 
for key, value in color.items():
    print(key, value)

# return key 
print("*" * 50)
print("return key")
for key in color.keys():
    print(key)

# return value 
print("*" * 50)
print('return value')
for value in color.values():
    print(value)

print("*" * 50)
print("*" * 50)
# ----------------------------------------
# ------------- while loop ---------------
# ----------------------------------------

print("*" * 50)
print("*" * 50)
x = 0
while x < 5:
    print(x)
    x += 1

print("*" * 50)
x = 0
s = 0
while x < 10:
    s = s + x 
    x = x + 1
print(f"the sum of first 9 numbers 1-9 is {s} and thier count is {x}")

print("*" * 50)
print("*" * 50)
# while loop with if-else and break statement
x = 1;
s = 0
while (x < 10):
    s = s + x
    x = x + 1
    if (x == 5):
        break
else :
    print('The sum of first 9 integers : ',s)        
print('The sum of ',x,' numbers is :',s)