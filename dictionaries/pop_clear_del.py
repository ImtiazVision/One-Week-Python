# The pop() method accepts a key and will delete the corresponding key-value pair in the dictionary. It returns the deleted value. 
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)
prices = {
    'coconut': 5.11,
    'strawberries': 4.99,
    'orange': 3.99,
    'blueberries': 2.99,
    'blackberries': 4.15,
    'basil': 2.99
}
expensive_product = prices.pop('strawberries')
print(prices)
print(expensive_product)