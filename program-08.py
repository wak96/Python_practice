# write a python program display  calendar.

import calendar
year = int(input("Enter Year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)

# if i want to see full year calender
import calendar

Year = int(input("Enter the Year you want to see full calender: "))

ful_cal = calendar.calendar(Year)
print(f"full year calendar {ful_cal}")