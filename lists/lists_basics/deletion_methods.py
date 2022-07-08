# clear() method will remove all items from a list

# language = ['Python', 'Java', 'JavaScript']

# print(language)

# language.clear()

# print(language)

# The remove(x) method will remove the 'First' element in the list that has a value of x

# language = ['Python', 'C', 'Java', 'JavaScript', 'C']

# print(language)

# language.remove('C')

# print(language)

# The pop() method removes AND return the last element from a list. pop() is the most common way to remove anything from a list. pop() also accepts a specific index. We can also specify an index like pop(index) if we want to remove a specific element.

# language = ['Python', 'C', 'Java', 'JavaScript', 'C']

# print(language)

# language.pop()

# print(language)

# language.pop(1)

# print(language)

# The 'del' statement (it's not a method!) can be used to delete an item from a specific index in a list

language = ['Python', 'C', 'Java', 'JavaScript', 'C']

print(language)

del language[4]

print(language)
