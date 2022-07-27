# The update() method will update a dictionary using the key-value pairs from a second dictionary, passed as the argument. 

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Cat_woman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add second phone_book to phone_book
# phone_book.update(second_phone_book)
# print(phone_book)

# We can use two stars ** to combine multiple dictionaries into a new resulting dictionary known as dictionary unpacking. 

# third_phone_book = { **phone_book, **second_phone_book}
# print(third_phone_book)

# 'dict union'. Python 3.9 added the dict union operator (|). It will return a new dictionary containing the items from the left and the right dictionaries. In the case of duplicated keys, the right side 'wins' i.e. the key of the right hand side dictionary will take precedence. 

