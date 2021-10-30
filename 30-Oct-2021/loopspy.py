"""
for \while loop:
"""

# program print 1,2,3,4,5

# for
for i in range(1,6):
    print(i)

print("*"*80)

# while
i = 1
while i <= 5:
    print(i)
    i = i +1 
print("*"*80)
# ---------------------------
# ex1
# write program sum numbers from 1 to 100 and print the result of sum
# -------------------------------
"""
algorithm
start
num = 1
end = 100
range = (1,100)
i = 1
s = 0
while i <=100:
    sum = i + s
    print(num)
end
"""
i = 1
s = 0
while i <=100:
    s = i +s
    i = i + 1

print(s)

print("*"*80)

i = 1
s = 0
for i in range(1, 101):
    s = i + s
    i = i + 1
print(f'the sum of range 1:100 is : {s} and the count is {i}')
print("*"*80)
# ---------------------------
# ex1
# write program multibly numbers from 1 to 100 and print the result of sum
# -------------------------------

i = 1
m = 1
while i <=10 :
    m = m * i
    i += 1
print (m)


