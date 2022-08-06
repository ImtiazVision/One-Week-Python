# LBYL: Look Before You Leap
# It is a coding style where we explicitly test for pre-conditions before making calls or 'leaping'. It is characterized by lots of if statements.  

num = input("Enter a number: ")
# 'Look': Check to see if 'num' is numeric
if num.isnumeric():
# 'Leap': Convert 'num' to int once we know it's safe
  num = int(num)
else:
  num = 10


# EAFP: Easier to ask forgiveness than permission
# "Assume things exist or will work, and catch exceptions if you are wrong"
# It is a coding style characterized by lots of try/except blocks