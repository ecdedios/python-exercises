line = '--------------------------------------------------'

# 1a. prompt the user for a day of the week, print out whether the day is Monday
#    or not

# day_of_the_week = input('Day of the week? ')

# if day_of_the_week.lower() == 'monday':
#     print(f'The day of the week is {day_of_the_week}')
# else:
#     print(f'The day of the week is NOT Monday.')

print(line)

# 1b. prompt the user for a day of the week, print out whether the day is a
#    weekday or a weekend

# weekdays = ['monday','tuesday','wednesday','thursday','friday']
# weekend = ['saturday','sunday']

# day_of_the_week = input('Day of the week? ')

# if day_of_the_week.lower() in weekdays:
#     print(f'"{day_of_the_week}" is a weekday.')
# elif day_of_the_week.lower() in weekend:

#     print(f'"{day_of_the_week}" is a weekend.')
# else:
#     print(f'"{day_of_the_week}" is an invalid input.')

print(line)

# 1c. create variables and make up values for
#
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

# hours_worked_in_week = input('How many hours for this week? ')
# hourly_rate = input('How much is the hourly rate?')

# if hours_worked_in_week.isnumeric():
#     if hourly_rate.isnumeric():
#         if float(hours_worked_in_week) > 40:
#             paycheck_for_week = float(hours_worked_in_week) * (float(hourly_rate) * 1.5)
#         elif float(hours_worked_in_week) <= 40:
#             paycheck_for_week = float(hours_worked_in_week) * (float(hourly_rate) * 1.0)
#         else:
#             paycheck_for_week = 'ERROR'
#     else:
#         print(f'"{hourly_rate}" is not a valid input."')
#         paycheck_for_week = 'ERROR'
# else:
#     print(f'"{hours_worked_in_week}" is not a valid input.')
#     paycheck_for_week = 'ERROR'

# if paycheck_for_week == 'ERROR':
#     print(f'There has been an error.')
# else:
#   print(f'{paycheck_for_week:,} is the weeks paycheck.')

print(line)


# 2a - WHILE LOOPS

# i = 5
# while i <= 15:
# 	print(i)
# 	i += 1

# i = 0
# while i <= 100:
# 	print(i)
# 	i += 2

# i = 100
# while i >= -10:
# 	print(i)
# 	i -= 5

# i = 2
# while i < 1_000_000:
# 	print(i)
# 	i *= i

# i = 100
# while i >= 5:
# 	print(i)
# 	i -= 5

# 2b - FOR LOOPS

# number = input('Enter a number: ')
# for i in range(11):
# 	print(f'{number} x {i} = ' + str((float(number)*i)))

# for i in range(10):
# 	print(str(i)*i)

#2c - BREAK and CONTINUE

number = input('Enter a number between 1 and 50: ')
while not number.isdigit():
	number = input('Enter a number between 1 and 50: ')
while not (float(number) > 0 and float(number) < 51):
	number = input('Enter a number between 1 and 50: ')
print(number)



















































