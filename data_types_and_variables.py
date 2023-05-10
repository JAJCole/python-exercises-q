#1
# float
# string
# boolean
# string
# int
# boolean
# string
# list w/ array
# dictionary

#2 What data type would best represent the following?

#    A term or phrase typed into a search box
-- string
#    Whether or not a user is logged in
-- boolean
#    A discount amount to apply to a user's shopping cart
-- float
#    Whether or not a coupon code is valid
-- boolean
#    An email address typed into a registration form
-- string
#    The price of a product
-- float/int
#    The email addresses collected from a registration form
string/dictionary
#    Information about applicants to Codeup's data science program
-- string

# 3 For each of the following code blocks:
# Read the expression and predict the evaluated results
# Execute the expression in a Python REPL.
'1' + 2 # error
6 % 4 # 2
type(6 % 4) # int
type(type(6 % 4)) # type
'3 + 4 is ' + 3 + 4 # error
0 < 0 # false
'False' == False # false
True == 'True' # false
5 >= -5 # true
True or "42" # true
6 % 5 # 1
5 < 4 and 1 == 1 # false
'codeup' == 'codeup' and 'codeup' == 'Codeup' # false
4 >= 0 and 1 !== '1' # error
6 % 3 == 0 # true
5 % 2 != 0 # true
[1] + 2 # error
[1] + [2] # [1,2]
[1] * 2 # [1,1]
[] + [] == [] # true
{} + {} # {} (was error)

# Describe the following scenarios. You will need to create and assign variables and use operators.

# 5. You have rented some movies for your kids: 
# The Little Mermaid for 3 days
# Brother Bear for 5 days
# Hercules for 1 day
# If the daily fee to rent a movie is 3 dollars, how much will you have to pay?

lm = 3
bb = 5
hc = 1
fee = 3
total = (lm + bb + hc) * fee
print(total)
# total = $27

# 6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

# They pay you the following hourly rates:
#Google: 400 dollars
#Amazon: 380 dollars
#Facebook: 350 dollars

#This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
#How much will you receive in payment for this week? 

goo_rate = 400
ama_rate = 380
fab_rate = 350
goo_hour = 6
ama_hour = 4
fab_hour = 10
total_check = (goo_rate*goo_hour) + (ama_rate*ama_hour) + (fab_rate*fab_hour)
print(total_check)
# total check is $7420

# 7. A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.
class_elig = True
class_full = False
class_schedule_conflict = False
if class_full == True or class_schedule_conflict == True:
    class_elig == False
else:
    class_elig == True
print(class_elig)

# 8. A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

prod_purch = 6
offer_exp = False
product_offer = {} 

if prod_purch > 2 and offer_exp != True:
    product_offer = True

# 9. Continue working in the data_types_and_variables.py file. 
# Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'
pw_len = len(pw)
pw_ver = []
un_len = len(un)
un_ver = []
pw_not_un = []
def cred_req(un,pw):
    if pw_len >= 5 and un_len <= 21 and un != pw:
        print('Your pw and un combo meet criteria.' )
        pw_ver = True
        un_ver = True
        pw_not_un = True
    else:
        print('Credentials are not appropriate.')
    return
cred_req('codeup','notastrongpassword')

print(pw_ver)







