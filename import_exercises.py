# Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
#   Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
#   Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.

# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.
import function_exercises
from function_exercises import calculate_tip

calculate_tip()
# run in interactive window and use values. $100 bill with a 10% tip is a $10tip. 

from function_exercises import get_letter_grade as grading

grading()

# Read about and use the itertools module from the python standard library to help you 
# solve the following problems. Note: Many of these functions in this library 
# return an object, to see the results of the function, cast this object as a list.
# How many different ways can you combine a single letter from "abc" with 
# either 1, 2, or 3?
import itertools
from itertools import combinations

combo_1 = list(combinations('abc',1))
print(combo_1)
combo_2 = list(combinations('abc',2))
print(combo_2)
combo_3 = list(combinations('abc',3))
print(combo_3)

# How many different combinations are there of 2 letters from "abcd"?
from itertools import combinations

combo_x = list(combinations('abcd',2))
print(combo_x)

# How many different permutations are there of 2 letters from "abcd"?
from itertools import permutations

permu_2 = len(list(permutations('abcd',2)))
print(permu_2)

# Your code should produce a list of dictionaries. Using this data, write some code 
# that calculates and outputs the following information:
import json

json_var = json.load(open('profiles.json'))

count = 0
for i in json_var:
    count += 1
print(count)


# Total number of users
count = 0
for i in json_var:
    count += 1
print(count)
# total is 19 users

# Number of active users
print(json_var[1]['isActive'])

count = 0
for i in range(len(json_var)):
    if json_var[i]['isActive'] == True:
        count += 1
print(count)
# total active is 9 users

# Number of inactive users
count = 0
for i in range(len(json_var)):
    if json_var[i]['isActive'] == False:
        count += 1
print(count)
# total inactive is 10 users

# Grand total of balances for all users
print(json_var)

balance = []
for i in range(len(json_var)):
    balance.append(json_var[i]['balance'])
print(balance)

len(balance) # verify balance has 19 entries

new_balance = [] # create new list for cleaning
for i in balance:
    i = i.replace('$','')
    i = i.replace(',','')
    new_balance.append(i)
print(new_balance)

float_balance = [] # create new list for string to float
for i in new_balance:
    i = float(i)
    float_balance.append(i)
print(float_balance)
len(float_balance) # verify list still has 19 entries

total_balance_users = sum(float_balance)
print(total_balance_users)
# total is $52,667.02


# Average balance per user
avg_per_user = total_balance_users / len(float_balance)
print(round(avg_per_user,2))
# avg per user is $2,771.95

# User with the lowest balance
min(float_balance)
for i in range(len(json_var)):
    if json_var[i]['balance'] == 

# User with the highest balance

# Most common favorite fruit

fav_fruit = []
for i in range(len(json_var)):
    fav_fruit.append(json_var[i]['favoriteFruit'])
print(fav_fruit)


s_count = 0
a_count = 0
b_count = 0
for i in fav_fruit:
    if i == 'strawberry':
        s_count += 1
    elif i == 'apple':
        a_count += 1
    else:
        b_count += 1
print(s_count)
print(a_count)
print(b_count)
# most common is strawberry


# Least most common favorite fruit

# least common is bananas

# Total number of unread messages for all users
