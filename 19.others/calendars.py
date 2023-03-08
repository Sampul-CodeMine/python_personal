import calendar as cal

# print only the week headers of a month
print("\n============= WEEK HEADERS =============\n")
print(cal.weekheader(1))  # this will print the week-headers with 1-lettered week-heads
print()
print(cal.weekheader(2))  # this will print the week-headers with 2-lettered week-heads
print()
print(cal.weekheader(3))  # this will print the week-headers with 3-lettered week-heads
print()
print(cal.weekheader(4))  # this will print the week-headers with 4-lettered week-heads

print("\n============= FIRST WEEK DAY =============\n")
print("First day of the month: ", cal.firstweekday())  # prints the first day of the week for the current month

print("\n============= PRINT A MONTH's CALENDAR =============\n")
print("Prints the fourth month in the year 2019/4/4: ", cal.month(2019, 4, 3))  # Prints the fourth month in the year 2019

print("\n============= PRINT A MONTH's CALENDAR IN MATRIX FORM =============\n")
print(cal.monthcalendar(2019, 3))  # Prints the fourth month in the year 2019

print("\n============= PRINT A YEAR's CALENDAR =============\n")
print(cal.calendar(2020, 3))  # Prints the entire calendar for the year specified

print("\n============= PRINT WEEK DAY OF THE MONTH =============\n")
day_of_week = cal.weekday(2020, 11, 13)
print("Week Day for 2020/11/13: ", day_of_week)  # Prints the day of the week

print("\n============= CHECK IF YEAR IS LEAP YEAR =============\n")
is_leap_year = cal.isleap(2020)
print("Is 2020 a leap year?: ", is_leap_year)  # Prints the day of the week

print("\n============= HOW MANY LEAP YEARS IN A RANGE OF YEARS =============\n")
how_many_leap_years = cal.leapdays(1944, 2020)
print("How many Leap Years do we have between 1944 to 2020: ", how_many_leap_years)  # Prints the day of the week
