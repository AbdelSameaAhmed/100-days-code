
# Exercise 2_1:
#  Write a program that uses input to prompt a user for their
# name and then welcomes them.
# Enter your name: Chuck
# Hello Chuck
# ------------------------------
# Solution:
# create function called greatings
def greatings():
    # create var called name to reiceve user input
    name = input("please enter Name: ")
    # desplay greating
    return f"Welcome {name}.. nice to meet you.."
# test Function
print(greatings())
print("*" * 30)
print("*" * 30)

# Exercise 2_2: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# -----------------------------------
# Solution:

# create function to recieve
def payment(hrs, rate):
    try:
        hrs = float(hrs)
        rate = float(rate)
    except:
        print("Please enter valid values")
    result = hrs * rate
    return result
# test payment Function
print(payment(hrs = 35, rate = 2.75))

print("*" * 30)
print("*" * 30)

# Exercise 2_3:
# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions,
# write the value of the expression and the
# type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
# -----------------------------------
# Solution:
# 1. width//2
width = 17
print(width//2)
# 2. width/2.0
print(width/2.0)
# 3. height/3
height = 12.0
print(height/3)
# 4. 1 + 2 * 5
print(1 + 2 * 5)

print("*" * 30)
print("*" * 30)

# Exercise 2_4: Write a program which prompts the user for
#  a Celsius temperature, convert the temperature to Fahrenheit,
#  and print out the converted temperature.
# -----------------------------------
# Solution
def conver_to_celsius(fahrin_temp):
    celsius = 0
    try:
        f = float(fahrin_temp)
    except :
        print("please enter valid Value")
    
    celsius = (5/9)* (f-32)
    celsius = round(celsius, 0)
    return f" the {f} Fahrenheit is {celsius} celsius"
# test function
print(conver_to_celsius(22))
print(conver_to_celsius(90))


print("*" * 30)
print("*" * 30)

# Exercise 2_5 
# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
# ----------------------------------
# solution

def payment_r(hrs, rate):

    try:
        hrs = float(hrs)
        rate = float(rate)
    except :
        print("please enter valid values")

    finally:
        
        if hrs < 40:
            print("regular payment")
            print("no overtime")
            reglar_pay = hrs*rate
            reglar_pay = round(reglar_pay,1)
            return f"Your payment is regular pament :{reglar_pay}"

        else:
            print("extra payment")
            print("with overtime")
            overtime = (hrs - 40)*1.5
            reglar_pay = hrs * 40  
            total = round((overtime + reglar_pay),1)
        
            return f"Your overtime is: {overtime}\nand reglar_pay is {reglar_pay}\ntotal is {total}"
    # test payment_r Function
print(payment_r(20, 10)) # test less than 40 hr
print("*" * 50)
print("*" * 50)
print(payment_r(45, 10)) # test More than 40 hr
print("*" * 50)
print("*" * 50)
# print(payment_r(d, 10)) # test less wrong value