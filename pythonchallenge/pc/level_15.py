"""Level 15: whom
http://www.pythonchallenge.com/pc/return/cat.html and it implies the name should
be uzi
http://www.pythonchallenge.com/pc/return/uzi.html
It seems like guessing a person
"""

import calendar
from datetime import date

import requests


def solution():
    """1. todo: buy flowers for tomorrow -> Jan 27, Tuesday
    2. he -> male
    3. Feb 1xx6 (right-down corner) -> 29 days -> leap year
    4. he ain’t the youngest, he is the second -> the last second one chronologically
    5. Search "1756 Jan 27" in Google -> 1st relevant result is Mozart
    """
    candidates = [y for y in range(1006, 1997, 10) if is_jan_tue(y) and is_leap_year(y)]
    # [1176, 1356, 1576, 1756, 1976]
    result = date(candidates[-2], calendar.January, 27)
    return "mozart"


def is_jan_tue(year):
    """predicate if Jan 27 of the year is Tuesday"""
    return calendar.weekday(year, calendar.January, 27) == calendar.TUESDAY


def is_leap_year(year):
    """as last digit is not zero, so it only computes the case dividing 4"""
    return year % 4 == 0
