# add() will add a single value to a set. No duplicates in sets!

odd = {1,3,5,7}
odd.add(9)
print(odd)
# we can also find the length of a set using 'len' function
print(len(odd))

# remove() will remove a single value from a set
languages = {'Python', "Java", 'JavaScript'}
languages.remove('Java')
print(languages)

# discard() will remove element just like 'remove()' but won't throw error for missing value (if the value don't exists in a set)
odd = {9,11,13,15}
odd.discard(1)
odd.discard(15)
print(odd)

# clear() will completely empties out a set
languages = {'Python', "Java", 'JavaScript'}
languages.clear()
print(languages)

print({'a','b','c'} is {'a','b','c'}) # 'False' bc they hold different memory container

print({1,2,3} == {1,2,3}) # 'True' bc the elements are same inside the sets ('==' checks whether the contents are same)

# check if a value exists in sets
odd = {9, 11, 13, 15}
print(9 in odd)  # True
print(19 in odd)  # False

# iterate over set
odd = {9, 11, 13, 15}
for element in odd:
  print(element)

