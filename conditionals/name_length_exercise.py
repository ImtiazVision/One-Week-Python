avg_name_length = 12
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
name_length = len(first_name) + len(last_name)
full_name = first_name + " " + last_name

if name_length < avg_name_length:
  print(full_name, 'is shorter than average american name.')
elif len(name_length) > avg_name_length:
  print(full_name, 'is longer than average american name.')
elif len(name_length) == avg_name_length:
  print(full_name, 'is exactly the average length of an american name.')