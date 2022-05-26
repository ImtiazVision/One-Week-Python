# Concatenation: The + operator is used to concatenate strings. There will be no extra space between them.

message = 'Hello' + ' ' + 'World'
print(message)
message = 'Hello' + ' World'
print(message)

first_name = 'John'
last_name = 'Smith'

full_name = first_name + ' ' + last_name

one = '1'
fifty_four = '54'
concatenation = one + fifty_four

print(concatenation)

# We can multiply a string by a number. However, we can't multiply a string by a string.

string = 'Imtiaz' * 8
print(string)

# this will give an error message
str = 'imtiaz' * 'imtiaz'
print(str)  # TypeError: can't multiply sequence by non-int of type 'str', can only concatenate str (not "str") to str