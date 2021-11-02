# -----------------
# break_continue --
# -----------------

# Ex1
for i in range(2, 10):
    for x in range(2, i):
        if i % x == 0:
            print(i, 'equals', x, '*', i//x)
            break
    else:
        print(i, 'is a prime number')

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

ex5

dir() 
dir(set)


# range(start, stop[, step])
range(10)

print(list(range(10)))
print(list(range(1, 10, 2)))
# try excepet
def check_number(num=0):
    try:
        num = int(num)
        if num > 0:
            print('this is digit positive')
        elif num <0:
            print('this is digit negative')
        elif num==0:
            print('this is digit is zero')
        else:
            print('this value is string')
    except ValueError:
        print('please enter valid value')
check_number(num = 10)
check_number(num = -10)
check_number(num = '10')
check_number(num = "-10")
check_number(num = '-10a')
check_number(num = "10a")
