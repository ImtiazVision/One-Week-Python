# The update() method will update a dictionary using the key-value pairs from a second dictionary, passed as the argument. 

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678, "Cat_woman": 11141}

second_phone_book = {"Cat_woman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add second phone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

# We can use two stars ** to combine multiple dictionaries into a new resulting dictionary known as dictionary unpacking. 

# right hand side will take precedence in case of both dictionary having  duplicated keys 
third_phone_book = { **phone_book, **second_phone_book}
print(third_phone_book)

# 'dict union'. Python 3.9 added the dict union operator (|). It will return a new dictionary containing the items from the left and the right dictionaries. In the case of duplicated keys, the right side 'wins' i.e. the key of the right hand side dictionary will take precedence. 

dict1 = {'a':1, 'b':2, 'c':5}
dict2 = {'c':3, 'd':4} # since dict2 is on the right side, it's value 'c': 3 took precedence over 'c':5 of the dict1 
dict3 = dict1 | dict2
print(dict3)