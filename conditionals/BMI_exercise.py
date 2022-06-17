height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = (weight * 703) / (height ** 2)
print("Your BMI is: ", bmi)
if bmi < 16.0:
    print("You are severely underweight.")
elif bmi < 18.4:
    print("You are underweight.")
elif bmi < 24.9:
  print("You are normal.")
elif bmi < 29.9:
  print("You are overweight.")
elif bmi < 34.9:
  print("You are obese.")
elif bmi < 39.9:
  print("You are severely obese.")
else:
  print("You are morbidly obese.")
