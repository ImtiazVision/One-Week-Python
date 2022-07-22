empty_dictionary = {} # we need curly braces to create a dictionary
empty_dictionary = dict() # this a built-in dictionary function to create a dictionary just like list() 
print(type({}))  # <class 'dict'>
# syntax of a dictionary
order = {"quantity": 5, "price": 5.99} # we separate the elements by coma(,) and separate the key & value by a colon (:)

# we can't use list [] as a key of a dictionary
invalid_dict = {[111]: 'list'}
print(invalid_dict)  # TypeError: unhashable type: 'list'
