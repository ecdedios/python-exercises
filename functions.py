

# 1. Define a function named is_two. It should accept one input and
# return True if the passed input is either the number or the string 2,
# False otherwise.


def is_two(x):
    if x == '2' or x == 2:
        return True
    else:
        return False


# 2. Define a function named is_vowel. It should return True if the
# passed string is a vowel, False otherwise.


def is_vowel(x):
    if x.lower() in ['a', 'e', 'i', 'o', 'u', ]:
        return True
    else:
        return False


# 3. Define a function named is_consonant. It should return True if the
# passed string is a consonant, False otherwise. Use your is_vowel
# function to accomplish this.


def is_consonant(x):
    if is_vowel(x):
        return False
    else:
        return True


# 4. Define a function that accepts a string that is a word. The function
# should capitalize the first letter of the word if the word starts with
# consonant.


def capitalize(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word


# 5. Define a function named calculate_tip. It should accept a tip
# percentage (a number between 0 and 1) and the bill total, and return
# the amount to tip.


def calculate_tip(bill, tip):
    return bill*tip


# 6. Define a function named apply_discount. It should accept a
# original price, and a discount percentage, and return the price
# after the discount is applied.


def apply_discount(original_price, discount_percentage):
    return original_price - (original_price * discount_percentage)


# 7. Define a function named handle_commas. It should accept a string
# that is a number that contains commas in it as input, and return a
# number as output.


def handle_commas(string):
    new_string = string
    for x in string.lower():
        if x == ',':
            new_string = new_string.replace(x, '')
    return new_string


# 8. Define a function named get_letter_grade. It should accept a
# number and return the letter grade associated with that number (A-F).


def get_letter_grade(grade):
    if grade < 60:
        return 'F'
    elif grade >= 60 and grade <= 66:
        return 'D'
    elif grade >= 67 and grade <= 79:
        return 'C'
    elif grade >= 80 and grade <= 87:
        return 'B'
    else:
        return 'A'


# 9. Define a function named remove_vowels that accepts a string and
# returns a string with all the vowels removed.


def remove_vowels(word):
    new_word = word.lower()
    vowels = ('a', 'e', 'i', 'o', 'u',)
    for x in word:
        if x in vowels:
            new_word = new_word.replace(x, '')
    return new_word


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 	anything that is not a valid python identifier should be removed
# 	- leading and trailing whitespace should be removed
# 	- everything should be lowercase
# 	- spaces should be replaced with underscores
# 	for example:
# 	- 'Name' will become 'name'
# 	- 'First Name' will become 'first_name'
# 	- '% Completed' will become 'completed'


def normalize_name(name):
    new_name = name
    for x in name.lower():
        if x == ' ':
            new_name = new_name.replace(x, '_')
    acceptable_characters = ('_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)
    for x in name.lower():
        if x not in acceptable_characters:
            new_name = new_name.replace(x, '')
    return (new_name.strip('_')).lower()


# 11. Write a function named cumsum that accepts a list of numbers and
# returns a list that is the cumulative sum of the numbers in the list.
# - cumsum([1, 1, 1]) returns [1, 2, 3]
# - cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumsum(list):
    new_list = []
    sum = 0
    for n in list:
        sum += n
        new_list.append(sum)
        #print(sum, end=', ')
    print(new_list)
