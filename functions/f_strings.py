# f-strings are a simple technique to construct strings with interpolated expressions. Any code enclosed by curly brackets will be evaluated and the result converted to a string before being placed into the overall string.

age = input('How old are you (in years) ?\n')
age_in_days = float(age) * 365
print(f'You are {age_in_days} days old!!!')
