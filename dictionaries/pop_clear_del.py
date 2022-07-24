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


# popitem() takes no arguments and deletes the most recently (the last) added key-value pair. It returns the item as a tuple. 

# print(prices)
prices = {
    'coconut': 5.11,
    'orange': 3.99,
    'blueberries': 2.99,
    'blackberries': 4.15,
    'basil': 2.99
}

# last_added_product = prices.popitem()
# print(last_added_product)
# print(prices)

# updating exiting products price
prices["orange"] = 5.11 
# adding one more product
prices['banana'] = 5.00
# popitem() will remove the last added product from the dictionary and if we print it, it will give us the deleted last item and its value as a form of tuple i.e. ('banana', 5.0)
last_added_product = prices.popitem()
print(last_added_product)

print(prices)

# 'del' statement removes items from a dictionary. However, it is not a method!
prices = {
    'coconut': 5.11,
    'orange': 3.99,
    'blueberries': 2.99,
    'blackberries': 4.15,
    'basil': 2.99
}

del prices['orange']
print(prices)

# clear() deletes all items from a dictionary. It returns "None".

prices = {
    'coconut': 5.11,
    'blueberries': 2.99,
    'blackberries': 4.15,
    'basil': 2.99
}
# clear() will erase all the elements from a dictionary but keeps the empty dictionary 
prices.clear()

print(prices)
