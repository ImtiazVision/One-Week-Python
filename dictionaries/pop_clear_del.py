# The pop() method accepts a key and will delete the corresponding key-value pair in the dictionary. It returns the deleted value. 
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)
