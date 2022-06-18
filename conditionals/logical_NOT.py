# The 'not' operator changes True to False and False to True. It negates expressions.

from pyrsistent import b


birth_year = input("What year was your birth year? ")
if not birth_year.isnumeric():
  birth_year = input("That isn't a number. Try again please! What year was your birth year? ")
birth_year = int(birth_year)
print(f"You were born {2022 - birth_year} years ago.")
