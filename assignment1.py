#!/usr/bin/env python3



'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py
Author: Hussein Jundi-hjundi-186931218
The python code in this file (a1_hjundi.py) is original work written by
Hussein Jundi. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''



import sys


def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]





def mon_max(month: int, year: int) -> int:

    "returns the maximum day for a given month. Includes leap year check"

    # This is checking for the months that are 30 or 31 days. The months are: April, June, Sebtember, or November. If they are 30 days they return 30.

    if month in [4, 6, 9, 11]:
        return 30

    # This is checking the 2nd month which is February.

    # If it is a leap year, it is going to give us 29.

    # If it is not a leap year, it is going to give us 28.

    elif month == 2:

        if leap_year(year):

            return 29
        else:
            return 28

    # If the month is not 30 or it is not a leap year it will give us the month is 31 days.

    else:

        return 31

def after(date: str) -> str:

    '''

    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.

    This function takes care of the number of days in February for leap year.

    This fucntion has been tested to work for year after 1582

    '''

    str_year, str_month, str_day = date.split('-')

    year = int(str_year)

    month = int(str_month)

    day = int(str_day)

    tmp_day = day + 1  # next day


    if tmp_day > mon_max(month, year):

        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1

        tmp_month = month + 1

    else:

        to_day = tmp_day

        tmp_month = month + 0


    if tmp_month > 12:

        to_month = 1

        year = year + 1

    else:

        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date





def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")





def leap_year(year: int) -> bool:

    "return True if the year is a leap year"

    # This code is checking for the leap year. If there is a leap year we will get True, if no leap year we will get False.

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False





def valid_date(date: str) -> bool:

    "check validity of date and return True if valid"

    # This seperates the  output of the day, month, and year by -.

    try:
        str_day, str_month, str_year = date.split('-')
        # This makes them integers.
        day = int(str_day)
        month = int(str_month)
        year = int(str_year)

 # Makes sure that the days are at 1, and that it takes from the mon_max to see the month dates.
        if day < 1 or day > mon_max(month, year):
            return False
       

# Makes sure that the months is between 1 and 12. Anything before 1 or after 12 will be a error.
        if month < 1 or month > 12:
            return False
        
        # This is to make sure that the years are correct and nothing is below a year.
        if year < 1 or len(str_year) != 4:
            return False

        return True

    except ValueError:

        return False


def day_count(start_date: str, stop_date: str) -> int:

    "Loops through range of dates, and returns number of weekend days"

    # Variable to count the days

    weekend_num = 0

    date_now = start_date

    while date_now <= stop_date:
        str_day, str_month, str_year = date_now.split('-')
# This makes them to integers.
        day = int(str_day)

        month = int(str_month)

        year = int(str_year)

        # day_of_week function to get the day of the week specefied.

        day = day_of_week(day, month, year)

        if day in ['sat', 'sun']:

            weekend_num =  weekend_num + 1

        date_now = after(date_now)

    return weekend_num



if __name__ == "__main__":

    #3 arguments have to be used
    if len(sys.argv) != 3:
        usage()
        sys.exit(0)
    start_date = sys.argv[1]
    stop_date = sys.argv[2]

    if not valid_date(start_date) or not valid_date(stop_date):
        usage()
        sys.exit(0)

    if start_date > stop_date:
        weekend_num = day_count(start_date, stop_date)
        print("The beginning date should not be later than the end date")

    else:
        weekend_num = day_count(start_count, stop)
        print("The number fo weekend days between {start_count} and {stop} is {weekend_num}")
