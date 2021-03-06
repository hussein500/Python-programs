def isLeapYear(year):
    if year % 4 == 0:
        return True
    return False

def dayinmonth(month):
    if (month%2!=0 and month<=7) or (month%2==0 and month>=8):
        return 31
    elif month ==2:
        return 28
    return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if isLeapYear(year):
        if month == 2:
            if day == 29:
                return year, month, 1
        elif month == 12:
            if day < dayinmonth(month):
                return year, month, day + 1
            else:
                return year + 1, month, day
        else:
            if day < dayinmonth(month):
                return year, month, day + 1
            else:
                return year, month + 1, 1
    else:

        if month == 2:
            if day == dayinmonth(month):
                return year, month, 1
        elif month == 12:
            if day < dayinmonth(month):
                return year, month, day + 1
            else:
                return year + 1, month, day
        else:
            if day < dayinmonth(month):
                return year, month, day + 1
            else:
                return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates,
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()