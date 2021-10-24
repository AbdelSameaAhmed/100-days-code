# -----------------------------
# function, loop and condition
# -----------------------------

# break continue

# break
# to break a for and while loop
# example1
# write program can sum and count first 5 element and return them
# Solution
# -----------------------------

print("*" * 80)
print(" " , '\n')
l1 = list(range(1,10))
# print(l1)
num_s = 0
count_s = 0
for x in l1:
    num_s = num_s + x
    count_s += 1
    if count_s == 5:
        break
print(f"the sum of first five element is: {num_s} and count is {count_s}")
print(" " , '\n')
print("*" * 80)


print("*" * 80)
print(" " , '\n')
# example2
# convert the above to function can recieved the list 
# and return the same output
# solution 
# -------------------------------------
def sumandcount(l1):
    
# print(l1)
    num_s = 0
    count_s = 0
    for x in l1:
        num_s = num_s + x
        count_s += 1
        if count_s == 5:
            break
    print(f"the sum of first five element is: {num_s} and count is {count_s}")

# test Fuction
sumandcount(l1 = [11,22,34,44,55,66,67,8,9,10,11,12])
print(" " , '\n')
print("*" * 80)
