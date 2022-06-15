avg_name_length = 10
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
full_name = first_name + last_name

if len(full_name) < avg_name_length:
  print(full_name, 'is a short name.')
elif len(full_name) > avg_name_length:
  print(full_name, 'is a long name.')