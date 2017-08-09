# coding=utf-8
def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # assert + expression if expression is false : throw an AssertionError
    # assert 后跟表达式, 若表达式为False，中断程序运行
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    num = 0
    # while year != year2 or month != month2 or day != day2:
    # BUG: 若第一个年份大于第二个年份,会导致死循环
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        num = num + 1
    return num


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def daysInMonth(year, month):
    days_in_normal_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_leap_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        return days_in_leap_month[month - 1]
    else:
        return days_in_normal_month[month - 1]


print daysBetweenDates(2000, 12, 31, 2001, 1, 1)
