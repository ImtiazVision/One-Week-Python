# The 'and' operator will evaluate to True only if both the left and right sides evaluate to True.
# nested conditionals are an alternative for logical conditions but logical are shorter and better.  

age = float(input("Enter your age : \n"))
if age > 10 and age < 25:
  print("You ar a youngster!")
else:
  print("You are not a youngster!")