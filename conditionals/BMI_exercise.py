height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = (weight * 703) / (height ** 2)
print("Your BMI is: ", bmi)
if bmi < 16.0:
    print("You are severely underweight.")
elif bmi > 16.0 and bmi < 18.4:
    print("You are underweight.")
