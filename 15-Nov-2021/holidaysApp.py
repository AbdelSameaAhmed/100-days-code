
import holidays
from datetime import datetime

year = int(input("please enter year: "))
for day in holidays.USA(years=year).items():
    print(day)

