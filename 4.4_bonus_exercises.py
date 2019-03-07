# Bonus Exercises

from functools import reduce
import string


def separator():
    print()
    print('--------------------------------------------------')
    print()


separator()

# Create a function named twelveto24. It should accept a string in the
# format 10:45am or 4:30pm and return a string that is the
# representation of the time in a 24-hour format. Bonus write a
# function that does the opposite.


def twelveto24(time):
    hour = time[:-5]  # hour
    minute = time[-4:-2]  # minute
    designator = time[-2:]  # designator
    new_hour = hour
    if designator == 'pm':
        new_hour = int(hour) + 12
        if new_hour == 24:
            new_hour = 0
    new_time = str(new_hour)+minute
    if len(new_time) == 3:
        new_time = '0'+new_time

    return new_time


print('12:30pm --> ' + twelveto24('12:30pm') + ' hours')
print('4:30am --> ' + twelveto24('4:30am') + ' hours')
print('10:30am --> ' + twelveto24('10:30am') + ' hours')
print('10:30pm --> ' + twelveto24('10:30pm') + ' hours')
print('4:30pm --> ' + twelveto24('4:30pm') + ' hours')

separator()


def twentyfourto12(time):
    string_time = str(time)
    hour = string_time[:2]  # hour
    minute = string_time[2:]  # minute
    new_hour = int(hour)
    new_minute = int(minute)
    if new_hour > 12:
        new_hour = new_hour - 12
        designator = 'pm'
    else:
        designator = 'am'

    new_time = str(new_hour) + ':' + str(new_minute) + designator

    return new_time


print('0340 --> ' + twentyfourto12('0340'))
print('1340 --> ' + twentyfourto12('1340'))

separator()

# Create a function named col_index. It should accept a spreadsheet
# column name, and return the index number of the column.
# -- col_index('A') returns 1
# -- col_index('B') returns 2
# -- col_index('AA') returns 27


def col_index(chars):
    return reduce(lambda r, x: r * 26 + x + 1, map(string.ascii_uppercase.index, chars), 0)


print(col_index('AAA'))
