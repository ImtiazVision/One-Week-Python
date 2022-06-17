height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = (weight * 703) / (height ** 2)
if bmi < 16.0:
    print(f"Your BMI of {bmi} makes you severely underweight.")
elif bmi < 18.4:
    print(f"Your BMI of {bmi} makes you underweight.")
elif bmi < 24.9:
  print(f"Your BMI of {bmi} makes you normal.")
elif bmi < 29.9:
  print(f"Your BMI of {bmi} makes you overweight.")
elif bmi < 34.9:
  print(f"Your BMI of {bmi} makes you obese.")
elif bmi < 39.9:
  print(f"Your BMI of {bmi} makes you obese.")
else:
  print(f"Your BMI of {bmi} makes you morbidly obese.")
