line = '--------------------------------------------------'

# 1a. prompt the user for a day of the week, print out whether the day is Monday
#    or not

day_of_the_week = input('Day of the week? ')

if day_of_the_week.lower() == 'monday':
    print(f'The day of the week is {day_of_the_week}')
else:
    print(f'The day of the week is NOT Monday.')

print(line)

# 1b. prompt the user for a day of the week, print out whether the day is a
#    weekday or a weekend

weekdays = ['monday','tuesday','wednesday','thursday','friday']
weekend = ['saturday','sunday']

day_of_the_week = input('Day of the week? ')

if day_of_the_week.lower() in weekdays:
    print(f'"{day_of_the_week}" is a weekday.')
elif day_of_the_week.lower() in weekend:

    print(f'"{day_of_the_week}" is a weekend.')
else:
    print(f'"{day_of_the_week}" is an invalid input.')

print(line)

# 1c. create variables and make up values for
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

hours_worked_in_week = input('How many hours for this week? ')
hourly_rate = input('How much is the hourly rate?')

if hours_worked_in_week.isnumeric():
    if hourly_rate.isnumeric():
        if float(hours_worked_in_week) > 40:
            paycheck_for_week = float(hours_worked_in_week) * (float(hourly_rate) * 1.5)
        elif float(hours_worked_in_week) <= 40:
            paycheck_for_week = float(hours_worked_in_week) * (float(hourly_rate) * 1.0)
        else:
            paycheck_for_week = 'ERROR'
    else:
        print(f'"{hourly_rate}" is not a valid input."')
        paycheck_for_week = 'ERROR'
else:
    print(f'"{hours_worked_in_week}" is not a valid input.')
    paycheck_for_week = 'ERROR'

if paycheck_for_week == 'ERROR':
    print(f'There has been an error.')
else:
  print(f'{paycheck_for_week:,} is the weeks paycheck.')

print(line)



# 2a - WHILE LOOPS

i = 5
while i <= 15:
	print(i)
	i += 1

i = 0
while i <= 100:
	print(i)
	i += 2

i = 100
while i >= -10:
	print(i)
	i -= 5

i = 2
while i < 1_000_000:
	print(i)
	i *= i

i = 100
while i >= 5:
	print(i)
	i -= 5

# 2b - FOR LOOPS

number = input('Enter a number: ')
for i in range(11):
	print(f'{number} x {i} = ' + str((float(number)*i)))

for i in range(10):
	print(str(i)*i)



#2c - BREAK and CONTINUE

number = input('Enter a number between 1 and 50: ')
while not number.isdigit():
	number = input('Enter a number between 1 and 50: ')
while not (int(number) > 0 and int(number) < 51):
	number = input('Enter a number between 1 and 50: ')
while (int(number) % 2) == 0:
	number = input('Enter a number between 1 and 50: ')
print('The number to skip is: '+ number)
print()
for i in range(1,51,2):
	if i == int(number):
		print('Yikes! Skipping number: ' + str(i))
		continue
	print('Here is an odd number: ' + str(i))

number = input('Enter a positive number: ')
while not number.isdigit():
	number = input('Not a positive number. Enter a positive number:  ')
while not (int(number) > 0):
	number = input('Not a positive number. Enter a positive number:  ')
for i in range(0,int(number)+1):
	print(i)

number = input('Enter a positive number: ')
while not number.isdigit():
	number = input('Not a positive number. Enter a positive number:  ')
while not (int(number) > 0):
	number = input('Not a positive number. Enter a positive number:  ')
for i in range(int(number),0, -1):
	print(i)



# 3 - FIZZBUZZ

for i in range(0,101):
	if i % 3 == 0 and i % 5 == 0:
		print('FizzBuzz')
		continue
	if i % 3 == 0:
		print('Fizz')
		continue
	if i % 5 == 0:
		print('Buzz')
		continue
	print(i)



# 4 - TABLE OF POWERS

go_on = 'y'
while go_on == 'y':
	number = input('What number would you like to go up to? ')
	print()
	print('Here is your table!')
	print()
	print('number \t \t| squared | cubed')
	print('------ \t \t| ------  | ------')
	for i in range(1, int(number)+1):
		print(f'{i} \t \t| {i ** 2} \t \t| {i ** 3}')
	go_on = input('Would you like to continue? [y/N] ')
	if go_on == 'y':
		print()
		continue
print()
print('Thank you; good bye!')



# 5 - NUMBER TO LETTER GRADES

go_on = 'y'
while go_on == 'y':
	number_grade = input('Enter a number grade between 0 to 100: ')
	number_grade = int(number_grade)
	if number_grade < 60:
		letter_grade = 'F'
	elif number_grade >= 60 and number_grade <= 66:
		letter_grade = 'D'
	elif number_grade >=67 and number_grade <= 79:
		letter_grade = 'C'
	elif number_grade >= 80 and number_grade <= 87:
		letter_grade = 'B'
	else:
		letter_grade = 'A'
	print('Letter grade is: ' + letter_grade)
	print()
	go_on = input('Would you like to continue? [y/N] ')
	if go_on == 'y':
		print()
		continue
print()
print('Thank you; good bye!')



# 6 - DD'S LIBRARY OF BOOKS

books = [
	{	'title':'Python Data Analysis',
		'author':'Fabio Nelli',
		'genre':'Python' },
	{	'title':'Adventures in Minecraft',
		'author':'David Whale',
		'genre':'Minecraft' },
	{	'title':'Raspberry Pi By Examples',
		'author':'Ashwin Pajankar',
		'genre':'Raspberry Pi' },
	{	'title':'Python Data Analysis 2',
		'author':'Fabio Nelli',
		'genre':'Python' },
	{	'title':'Adventures in Minecraft 2',
		'author':'David Whale',
		'genre':'Minecraft' },
	{	'title':'Raspberry Pi By Examples 2',
		'author':'Ashwin Pajankar',
		'genre':'Raspberry Pi' },
	{	'title':'Python Data Analysis 3',
		'author':'Fabio Nelli',
		'genre':'Python' },
	{	'title':'Adventures in Minecraft 3',
		'author':'David Whale',
		'genre':'Minecraft' },
	{	'title':'Raspberry Pi By Examples 3',
		'author':'Ashwin Pajankar',
		'genre':'Raspberry Pi' }
]

for i in range (0,len(books)):
	print('Title: ' + books[i]['title'])
	print('Author: ' + books[i]['author'])
	print('Genre: ' + books[i]['genre'])
	print()

user_genre = input('Enter a genre: (Python, Minecraft, or Raspberry Pi): ')
print()
for i in range (0,len(books)):
	if books[i]['genre'] == user_genre:
		print('Title: ' + books[i]['title'])
		print('Author: ' + books[i]['author'])
		print('Genre: ' + books[i]['genre'])
		print()



































