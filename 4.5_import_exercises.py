from operator import itemgetter
import statistics as s
from babel.numbers import format_currency
from decimal import Decimal
from re import sub
import itertools as t
import json
from functions_exercises import is_two as twofer
from functions_exercises import is_two
import functions_exercises as f
import heapq
import collections
import re


#  1. import the module and refer to the function with the . syntax
print(f.is_two('three'))

# 2. use from to import the function directly
print(is_two('2'))

# 3. use from and give the function a different name
print(twofer(2))


# 1. How many different ways can you combine the letters
#  from "abc" with the numbers 1, 2, and 3?
print(list(t.zip_longest('abcd', '123', fillvalue='-')))
print(list(zip(['a', 'b', 'c'], [1, 2, 3],)))
print(list(t.product('ABC', '123')))


# 2. How many different ways can you combine two of the letters from "abcd"?
print(list(t.combinations('ABCD', 2)))
print(list(t.combinations_with_replacement('ABC', 2)))
print(list(t.permutations('ABCD', 2)))


x = open('profiles.json')
data = json.loads(x.read())
x.close()

print('Total number of users: '+str(len(data)))

active_list = []
for row in data:
    if row['isActive'] == True:
        active_list.append(row['isActive'])

print('Total number of active users: '+str(len(active_list)))

inactive_list = []
for row in data:
    if row['isActive'] == False:
        inactive_list.append(row['isActive'])

print('Total number of inactive users: '+str(len(inactive_list)))

balance = 0
for row in data:
    balance += Decimal(sub(r'[^\d.]', '', row['balance']))
    avg = balance / len(data)

print('Grand total balance for all users: ' +
      format_currency(balance, 'USD', locale='en_US'))
print('Average balance for all users: ' +
      format_currency(avg, 'USD', locale='en_US'))


balance_list = []
for row in data:
    balance_list.append(row['balance'])

for row in data:
    if row['balance'] == min(balance_list):
        print('User with lowest balance: '+row['name'])

for row in data:
    if row['balance'] == max(balance_list):
        print('User with highest balance: '+row['name'])

fruit_list = []
for row in data:
    fruit_list.append(row['favoriteFruit'])

print(s.mode(fruit_list))


def least_common_values(array, to_find=None):
    counter = collections.Counter(array)
    if to_find is None:
        return sorted(counter.items(), key=itemgetter(1), reverse=False)
    return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))


print('Least favorite fruit: ' + str(least_common_values(fruit_list, 1)))

greeting_list = []
unread_total = 0
for row in data:
    greeting_list.append(re.sub("\D", "", row['greeting']))
    unread_total += int(re.sub("\D", "", row['greeting']))

print('Total number of unread messages: ' + str(unread_total))
