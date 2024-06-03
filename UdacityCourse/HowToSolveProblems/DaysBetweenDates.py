'''
Problem Summary

Given a date in the past, and the current date, calculate the number of days between the two dates
'''
'''
How to solve:

Given Input:
Year, Month, Day
Curr Year, Curr Month, Curr Day

Simple Mechanical Pseudocode;

days = 0
while date1 is before date2:
    date1 = advance to the next day
    days += 1

'''

past = 1 / 1 / 2022
curr = 1 / 2 / 2023


def leap(year):
    if year % 4 == 0:
        return True
    return False

def daysbetween(before, now):
    before[]
    for i in range()