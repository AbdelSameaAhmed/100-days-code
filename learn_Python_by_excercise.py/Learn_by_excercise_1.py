# ----------------------------------------
# --- learn python by excercise__1 -------
# ----------------------------------------

print(abs.__doc__)
# ex1
# --------------------------------------
# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
help("calendar")
import calendar

# my_calendar = calendar.Calendar(firstweekday=6)
my_calendar = calendar.Calendar(firstweekday=6)
print(my_calendar)
for weekday in my_calendar.iterweekdays():
    print(weekday, end = ",")
for weekday in my_calendar.itermonthdays3(2022,6):
    print(weekday, end = ',')


# for date in my_calendar.monthdatescalendar(2022, 11):
#     print(date)
# for date in my_calendar.monthdayscalendar(2022, 11):
#     print(date)

# print(calendar.month(2022,12))

# print(calendar.calendar(2022, w=2, l=1, c=6, m=3))
# # print(my_calendar.monthdatescalendar(2022, 7))

# -------------------------------------------------
# generate calendar for specific year '2022'

print(calendar.calendar(2022, w=2, l=1, c=6, m=3))

print("*" * 60)
# generate month ''jan''
print(calendar.month(2022, 1))
print("*" * 60)
leepday = calendar.leapdays(2021, 2031)
print(leepday)

#######################################################################
# ----------------------------------------------------------------------
# ex2
# --------------------------------------
# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
import datetime
from datetime import date
firstdate = date(2014, 7, 2)
seconddate = date(2014, 7, 11)
no_of_daysa = seconddate - firstdate
print(no_of_daysa)

# ------------------
# ex3
# --------------------------------------
# r = 6 
# v = 4/3 * (3.14) * (6**3)
# print(v)

# ----------------------------------------------
print("*" * 50)
# ex4
# --------------------------------------
#  Write a Python program to get the difference between a given number
#  and 17, if the number is greater than 17 return double the absolute difference.

given_number = int(input("PLZ enter number"))
num = 17
if given_number > num:
    dif = (given_number - num) * 2

    print(dif)
else:
    print("it is not greater than 17")

# ex5
# --------------------------------------

# Write a Python program to test whether a number is within 100 of 1000 or 2000
# ----------------------------------------------------

# ex6
# --------------------------------------

#  Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.
# num1 = 40
# num2 = 30
# num3 = 20

# sum_of_num = num1 + num2 + num3
if num1 == num2 and num1 == num3 and num3 == num2:
    return sum_of_num * 3

def sum_thi(x, y, z):
    sumofelement = x + y + z
    if x == y == z:
        sumofelement *=3
    return sumofelement

print(sum_thi(1, 2, 3))
print(sum_thi(3, 3, 3))
        

# ex6
# --------------------------------------

# Write a Python program to test if a variable is a list or tuple or a set.

def che(var):
    if type(var) is list:
        print(f"the type of {var} is: list")
    elif type(var) is tuple:
        print(f"the type of {var} is: tuple")
    elif type(var) is set:
        print(f"the type of {var} is: set")
print(che({1, 2, 4, "wq"}))

x = 30
print(format(x, '02x'))

y = 14
print(format(y, '02x'))