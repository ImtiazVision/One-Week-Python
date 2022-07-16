# The copy() method returns a 'shallow copy' of a list. Nested objects are not copied. 

list1 = [1,3,5,7,9]
list2 = list1.copy()
print(list2)
# list1 and list2 has different id in the memory (2549609097792 and 2549609441536) and thus it is called a 'shallow copy' 
print(id(list1), id(list2))
print(list1 is list2) # we can also compare the type(identity) of both list 

# Copying with [:] (slicing)
# We can also copy lists by creating slices of an entire list. It's not the most readable, but it works!
