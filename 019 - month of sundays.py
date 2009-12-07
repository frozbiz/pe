# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

# Sunday = 0
# January = 0
# 1/1/1901 was a Tuesday
nDayOfWeek = 2
nMonth = 0
nYear = 1901
bLeapYear = 0
anDaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

nSundays = 0
while nYear < 2001:
    # count first
    if (nDayOfWeek == 0):
        nSundays += 1
    # increment to the next month
    nDayOfWeek = (nDayOfWeek + anDaysInMonth[nMonth] + (nMonth == 1 and bLeapYear)) % 7
    nMonth = (nMonth + 1) % 12
    if (nMonth == 0):
        nYear += 1
        bLeapYear = ((nYear % 4) == 0)

print nSundays
