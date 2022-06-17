# f - 212
# c - 100
# k - 373
unit = input("Enter the unit of measurement: ")
temp = input("What is the  temperature of the water: ")

if unit == 'f':
  if temp == '212':
    print("Water is boiling")
  else:
    print("Water is not boiling. Must hit 212 degrees")
elif unit == 'c':
  if temp == '100':
    print("Water is boiling")
  else:
    print("Water is not boiling. Must hit 100 degrees")
elif unit == 'k':
  if temp == '373':
    print("Water is boiling")
  else:
    print("Water is not boiling. Must hit 373 degrees")