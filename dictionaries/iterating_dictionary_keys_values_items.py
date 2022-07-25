# We utilize the dict.items() method to iterate through the dictionary, which converts a dictionary into a collection of (key, value) tuples.
prices = {
    'coconut': 5.11,
    'strawberries': 4.99,
    'orange': 3.99,
    'blueberries': 2.99,
    'blackberries': 4.15,
    'basil': 2.99
}

# items_price = prices.items()
# print(items_price)
# output: dict_items([('coconut', 5.11), ('strawberries', 4.99), ('orange', 3.99), ('blueberries', 2.99), ('blackberries', 4.15), ('basil', 2.99)])

# Similarly, we can use .keys() to get only the keys and .values() to get only the values respectively

dictionary_keys = prices.keys()
print(dictionary_keys)