
# Exercises for start learning python
source: "http://www.py4e.com/code3/"<br>
Ebook: Python for Everybody<br>
        Exploring Data Using Python 3<br>
          Dr. Charles R. Severance<br>
# Chapter 2

Exercise 2: Write a program that uses input to prompt a user for their
name and then welcomes them.
Enter your name: Chuck
Hello Chuck
"""

# create function 
def greating():
  name = input("enter your name")
  return f"Hello {name} you are welcome"
greating()

"""Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

"""

def pament_hrs():
  working_hrs = input("plz enter working hours")
  working_hrs = float(working_hrs)
  hrs_rate = input("please enter rate for working hrs")
  hrs_rate = float(hrs_rate)
  return f"your payment is {working_hrs * hrs_rate}"
pament_hrs()

"""Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the
type (of the value of the expression).
1. width//2
2. width/2.0
3. height/3
4. 1 + 2 * 5

"""

width = 17
height = 120
print(width//2)
print(width/2.0)
print(height/3)
print(1+2*5)

"""Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.
"""

def convert_to_c():
  fh =input("please enter teperature in Fahrenheit")
  fh = float(fh)
  c = 5/9 * (fh - 32)
  c = round(c,0)
  return f"The Temperature {fh} Fehrenheit, is: {c} celsius"
convert_to_c()



"""# Chapter 3 Conditional execution<br>
# Try except statement

 

---


"""

# Example for Try except 
# the following is program for converting Fehrenhiet temprature to celsius 

Fehrenhiet_Temp = input("Please enter Fehrenhite Temp: ")
Fehrenhiet_Temp=float(Fehrenhiet_Temp)
celsius_Temp = 5.0/9.0 *(Fehrenhiet_Temp - 32.0)
print(celsius_Temp)
#in case the user enter wrong input as string "99 celsius"
#the output will be valueError: like
#ValueError: could not convert string to float: '99 celsius'

# try except will solve this error as follow"
try:
  Fehrenhiet_Temp = input("Please enter Fehrenhite Temp: ")
  Fehrenhiet_Temp=float(Fehrenhiet_Temp)
  celsius_Temp = 5.0/9.0 *(Fehrenhiet_Temp - 32.0)
  print(celsius_Temp)
except:
  print("please enter valid Value")

"""Exercise 1 
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

"""

def pament_hrs(wrk_hrs , hrs_rate ):

    wrk_hrs = float(wrk_hrs)
    hrs_rate = float(hrs_rate)
    if wrk_hrs <= 40:
      return f"'regular', overtime = 0.0 and your payment is {wrk_hrs * hrs_rate}"
    else:
      overtime = (wrk_hrs - 40)*(hrs_rate * 1.5)
      regular_pay = 40 * hrs_rate
      total_pament = overtime + regular_pay
      return f"'overtime', overtime = {overtime} and total = {total_pament}"


print(pament_hrs(45, 10))
print(pament_hrs(60, 10))

"""Use Try except to avoid nun-numeric input and ValueError """

x = input('enter the hours:')
y = input('enter the rate:')
try:
    hour = float(x)
    rate = float(y)
except:
    print('Error,Please enter the numeric digit:')
    exit()
if hour <= 40:
    print(hour*rate)
else:
    print((((hour-40)*rate)*1.5)+rate*40)

