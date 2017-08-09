# coding=utf-8
### Dave's code ############################################################################
def nextDay(year, month, day):
    if day < 30:
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


### Dave's code ############################################################################

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


print daysBetweenDates(2013, 1, 1, 2014, 1, 1)
