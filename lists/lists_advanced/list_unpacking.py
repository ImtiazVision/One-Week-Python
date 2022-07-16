# We can 'unpack' values from a list into specific variable.

member = ['John', 'Smith', 31]
# first = member[0]
# last = member[1]
# age = member[2]

first, last, age = member

# In the example above, the first value in the list is stored in a  variable called first, 2nd value as last and 3rd value as age. 

print(first, last, age) 

color = [255,43,19]

# We can use an asterisk (*) to gather any remaining unassigned values into a variable

item = [1, 'Cheese', 'Bagel', 'Candy', 'Waffle', 5.99]

quantity, items_name, price = item

print(quantity,  price)
print(items_name)
