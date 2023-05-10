# 1. Conditional Basics
# Prompt the user for a day of the week, print out whether the day is Monday or not
user_day = input('Enter the day of the week:').lower()
if user_day == 'monday':
    print('Blue Monday')
else:
    print('Not Monday! Livin for the weekend!')

# Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
user_day = input('Enter the day of the week:').lower()
weekend = ['saturday','sunday']
if user_day in weekend:
    print('Have a good weekend!')
else:
    print('Weekday. Livin for the weekend!')
# Calculate a weekly paycheck, accounting for overtime pay. Create variables and make up values for:
# The number of hours worked in one week
# The hourly rate
# For calculating pay:
# For working 40 hours or less, each hour is paid at the hourly rate
# For working more than 40 hours
# the first 40 hours are paid at the hourly rate
# each hour after 40 is paid at time and a half (hourly rate * 1.5)
def check_cal():
    rate = int(input('Enter your hourly wage:'))
    hours = int(input('Enter the hours you worked this week:'))
    ot_pay = 1.5
    pay = 0
    if hours <= 40:
        pay = rate*hours
        return pay
    else:
        pay = (rate*hours)*ot_pay
        return pay
check_cal()

# 2. Loop Basics
# While:
# Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less 
# than or equal to 15. Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2

# Create a while loop that starts at 2, and displays the number squared on each line while the 
# number is less than 1,000,000.
i = 2
while i < 1000000:
    print(i)
    i **= 2


# Write a while loop that uses print to create the output shown below:
100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
#
i = 100
while i >= 5:
    print(i)
    i -= 5

# For Loops
# Write some code using a for loop that prompts the user for a number, then shows a multiplication 
# table up through 10 for that number.
user_num = int(input('Enter a non negative integer:'))
for i in range(1,11):
    print('{} x {} = {}'.format(user_num, i, user_num*i))

# Create a for loop that uses print to create the output shown below:
1
22
333
4444
55555
666666
7777777
88888888
999999999
#
n = 1
for i in range(1,10):
    print(n*i)
## 
for i in range(1,10):
    print(str(i)*i)

# break and continue
# Write a program that prompts the user for a positive integer. Next write a loop that prints 
# out the numbers from the number the user entered down to 1.
user_in = int(input('Enter a positive integer:'))
while user_in >=1:
    print(user_in)
    user_in -= 1

# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: note that the input function returns a string, so you'll need to convert this to a numeric type.)
user_in = int(input('Enter a positive integer:'))
for i in range(0,user_in + 1):
    print(i)

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue 
# prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to 
# determine this). Use a loop and the continue statement to output all the odd numbers between 
# 1 and 50, except for the number the user entered.
user_in = int(input('Enter an odd integer between 1 and 50:'))
print('Number to skip is: {}'.format(user_in))
for i in range(0, 51):
    if user_in % 2 == 0:
        print('You entered a positve number.')
        break
    elif i % 2 == 0:
        continue
    elif i == user_in:
        continue
    else:
        print('Here is an odd number: {}'.format(i))

# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

-- 1-100
-- x3 = fizz
-- x5 = buzz
-- x3x5 = fizzbuzz


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

# Display a table of powers.

# Prompt the user to enter an integer
# Display a table of squares and cubes from 1 to the value entered
# Ask if the user wants to continue
# Assume that the user will enter valid data
# Only continue if the user agrees to
# ex:
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
#
#

user_prompt = int(input('Enter an integer please:'))
valida = input('Would you like to proceed? y/n:').lower()
if valida == 'y':
    print('number| squared| cubed')
    for i in range(1,user_prompt + 1):
        print('{}     | {}      | {}'.format(i,i**2,i**3))
        valida = input('Would you like to proceed? y/n:').lower()

# Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100
# Display the corresponding letter grade
# Prompt the user to continue
# Assume that the user will enter valid integers for the grades
# The application should only continue if the user agrees to
# Grade Ranges:
        A : 100 - 88
        B : 87 - 80
        C : 79 - 67
        D : 66 - 60
        F : 59 - 0

grade = int(input('Enter a numeric grade 0-100:'))
verifa = input('Would you like to continue? y/n:').lower
#if verifa == 'y':
if 88 <= grade <= 100:
    print('A')
elif 80 <= grade <= 87:
    print('B')
elif 67 <= grade <= 79:
    print('C')
elif 60 <= grade <= 66:
    print('D')
else:
        print('F')
#else:
#    print('Have a nice day!')


# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and print out the titles 
# of all the books in that genre.





