# -----------------
# break_continue --
# -----------------

# Ex1
# for i in range(2, 10):
#     for x in range(2, i):
#         if i % x == 0:
#             print(i, 'equals', x, '*', i//x)
#             break
#     else:
#         print(i, 'is a prime number')

# ex2
# pass
while True:
    pass
# ex3
def passtatment():
    pass

# ex4
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number:", num)
        continue
    print("Found an odd number", num)
