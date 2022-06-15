avg_name_length = 12
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
full_name = first_name + last_name

if len(full_name) < avg_name_length:
  print(full_name, 'is shorter than average american name.')
elif len(full_name) > avg_name_length:
  print(full_name, 'is longer than average american name.')
elif len(full_name) == avg_name_length:
  print(full_name, 'is exactly the average length of an american name.')