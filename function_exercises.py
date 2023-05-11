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
