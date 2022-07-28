# To access elements of a tuple, we use index of that element 
dishes = ('burrito', 'taco', 'quesadilla', 'fajita', 'taco')
print(dishes[2])
# we can also use .index('value') method to ask for index of an element by providing the elements value inside the index method
print(dishes.index('fajita'))

# Slicing of tuple
print(dishes[0:3]) # 0,1,2 but 3rd element is omitted

# we can also find out how many times an element occurs in a tuple by .count('value') method
print(dishes.count('taco'))

# we can use 'in' operator to see if an element exists in a tuple and it will either give 'True' or 'False' value

print('nachos' in dishes)  # output: False

# we can iterate over a tuple using 'for' loop

for item in dishes:
  print(item)