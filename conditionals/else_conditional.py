# 'else' is the last conditional statement in the if statement. It is used when none of the other conditional statements are true.

age = int(input("How old are you?\n"))

if age >= 18:
  print('Your ticket price is $10')
elif age >= 21:
    print('Your ticket price is $8.00')
else:
  print('Your ticket price is $5.00')
