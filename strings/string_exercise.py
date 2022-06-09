first = "John"
last = "Smith"

# Concatenate first and last name into a full name with a space in between
full_name = first + ' ' +  last
print(full_name)

# creating an initials variable that holds the first letter of each first and last name
initials = first[0] + last[0]
print(initials)

# creating a variable that holds the first character of each first and last name with a period after each name

initials_2 = first[0] + '.' + last[0] + '.'
print(initials_2)

# creating a 'nickname' variable that holds the first 4 characters of the last name
nickname = last[0:4]
print(nickname)