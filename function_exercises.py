# Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_vowel(letter):
    vowels = ['a','e','i','o','u']
    if letter.lower() in vowels:
        return True
    else:
        return False


def is_consonant(letter):
    if is_vowel(letter) == False:
        return True
    else:
        return False
    
is_consonant('c')
is_consonant('A')




# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip():
    bill = int(input('Enter the bill total:'))
    tip_perc = float(input('Enter a % you wish to tip, format ex: 0.18'))
    return bill*tip_perc
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
#

#grade = int(input('Enter a numeric grade 0-100:'))
#verifa = input('Would you like to continue? y/n:').lower
#if verifa == 'y':
#if 88 <= grade <= 100:
#    print('A')
#elif 80 <= grade <= 87:
#    print('B')
#elif 67 <= grade <= 79:
#    print('C')
#elif 60 <= grade <= 66:
#    print('D')
#else:
#        print('F')

#
def get_letter_grade():
    while True:
        grade = int(input('Enter a numeric grade 0-100:'))
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
        verifa = input('Would you like to continue? y/n:').lower
        if verifa in ['y']:
            continue
        else:
            break

get_letter_grade()


    
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
    #Name will become name
    #First Name will become first_name
    #% Completed will become completed