# what is the output

# ------------ex1
x = []
if x :
    print(x ,"True")
else:
    print(x ,"False")

# Answer:
# False , empty list return False
# ------------------

print("*" * 80)

# ------------ex2

p = (1,10)
q = 0
r = []
if p or q or r:
    print(x ,"True")
else:
    print(x ,"False")

# Answer:
# True , empty list return False
# ------------------
print("*" * 80)
# ------------ex2

list1 = ["ABC", "XYZ", "PQR"]
for i in list1:
    i.lower()
print(list1)
# Answer: ['ABC', 'XYZ', 'PQR']

print("*" * 80)
# ------------ex3

# list2 = ["abc", '123']
# for i in list2:
#     list2.append(i)
# print(f"list2 is: {list2}")
# Answer: infinit loop
print("*" * 80)

# remember os 
import os
print(os.getcwd())

# os.rename()
print(os.listdir())
# os.chdir()