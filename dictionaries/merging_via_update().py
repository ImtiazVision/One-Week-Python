# The update() method will update a dictionary using the key-value pairs from a second dictionary, passed as the argument. 

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Cat_woman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add second phone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)
