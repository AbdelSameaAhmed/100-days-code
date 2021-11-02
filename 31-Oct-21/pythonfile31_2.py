# ---------------------------------
# ------- date.strftime(format) ---
# ---------------------------------

from datetime import datetime

# now = datetime.now()
# print(now)
# day = now.strftime('%a')
# day = day.strftime('%a')
# print(day)

# month = now.strftime('%m')
# print(month)

# year
# year full year
year = datetime.now().strftime('%Y')
print(year)
# year short
shortyear = datetime.now().strftime('%y')
print(shortyear)

# day
# day name
day = datetime.now().strftime('%A')
print(day)
# day name abbrifation
shortday = datetime.now().strftime('%a')
print(shortday)
# day number
daynumber = datetime.now().strftime('%d')
print(daynumber)

# month 
# month number
monthnumber = datetime.now().strftime('%m')
print(monthnumber)
# month ful name
monthname = datetime.now().strftime('%B')
print(monthname)
# month short name
shortmonth = datetime.now().strftime('%b')
print(shortmonth)

# septum
print("*" * 50)
# import datetime
from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%B-%Y'))

print(f" the current year is : {(datetime.now().strftime('%Y'))}")
print(f" the current Date is : {(datetime.now().strftime('%Y-%B-%d'))}")

# --------------------------------------------------------
print("*" * 50)

# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
import datetime

# today
today = datetime.date.today()
print(today)
print("*" * 20)
# or
now2 = datetime.datetime.now()
print(now2)