def separator():
	print()
	print('--------------------------------------------------')
	print()


separator()

# 1. Define a function named is_two. It should accept one input and
# return True if the passed input is either the number or the string 2,
# False otherwise.
def is_two(x):
	if x == '2' or x == 2:
		return True
	else:
		return False

print(is_two(2))
print(is_two('2'))
print(is_two(3))
print(is_two('Hello!'))

separator()

# 2. Define a function named is_vowel. It should return True if the
# passed string is a vowel, False otherwise.
def is_vowel(x):
	if x.lower() in ['a','e','i','o','u',]:
		return True
	else:
		return False

print(is_vowel('a'))
print(is_vowel('A'))
print(is_vowel('b'))

separator()

# 3. Define a function named is_consonant. It should return True if the
# passed string is a consonant, False otherwise. Use your is_vowel
# function to accomplish this.

def is_consonant(x):
	if is_vowel(x):
		return False
	else:
		return True

print(is_consonant('b'))
print(is_consonant('a'))

separator()

# 4. Define a function that accepts a string that is a word. The function
# should capitalize the first letter of the word if the word starts with 
# consonant.

def capitalize(word):
	if is_consonant(word[0]):
		return word.capitalize()
	else:
		return word

print(capitalize('regal'))
separator()

# 5. Define a function named calculate_tip. It should accept a tip
# percentage (a number between 0 and 1) and the bill total, and return 
# the amount to tip.

def calculate_tip(bill,tip):
	return bill*tip

print(calculate_tip(100,.18))
separator()

# 6. Define a function named apply_discount. It should accept a
# original price, and a discount percentage, and return the price
# after the discount is applied.
def apply_discount(original_price,discount_percentage):
	return original_price - (original_price * discount_percentage)

print(apply_discount(100,.1))
separator()

# 7. Define a function named handle_commas. It should accept a string
# that is a number that contains commas in it as input, and return a
# number as output.

def handle_commas(string):
	new_string = string
	for x in string.lower():
		if x == ',':
			new_string = new_string.replace(x,'')
	return new_string

print(handle_commas(',234,00,0'))
separator()

# 8. Define a function named get_letter_grade. It should accept a
# number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
	if grade < 60:
		return 'F'
	elif grade >= 60 and grade <= 66:
		return 'D'
	elif grade >=67 and grade <= 79:
		return 'C'
	elif grade >= 80 and grade <= 87:
		return 'B'
	else:
		return 'A'

print(get_letter_grade(81))
separator()

# 9. Define a function named remove_vowels that accepts a string and
# returns a string with all the vowels removed.

def remove_vowels(word):
	new_word = word
	vowels = ('a','e','i','o','u',)
	for x in word.lower():
		if x in vowels:
			new_word = new_word.replace(x,'')
	return new_word

print(remove_vowels('abracadabra'))
separator()

# 10. 







