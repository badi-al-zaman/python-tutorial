# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    """
    return false if the year is not a leap year
    :param year: is an integer
    :return: boolean
    """
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            return leap
        return True
    return leap

year = int(input())
print(is_leap(year))