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

# dictionary_keys = prices.keys()
# print(dictionary_keys)
# dict_keys(['coconut', 'strawberries', 'orange', 'blueberries', 'blackberries', 'basil'])
# dictionary_values = prices.values()
# print(dictionary_values)
# dict_values([5.11, 4.99, 3.99, 2.99, 4.15, 2.99])

# Similarly, we can iterate over the dictionary

# for item in prices.keys():
#   print(item)
# here, 'cost' is just a variable name as it could be anything but we made sure that the variable name does makes sense according to our context 
# for cost in prices.values():
#   print(cost)

# total = 0
# for price in prices.values():
#   total = total + price
# print(total/len(prices))

# for key in prices.keys():
#   print(key, prices[key])

# for item in prices.items():
#   print(item)

# dictionary unpacking 
# for key, value in prices.items():
#   print(key,value)

# to find out max price and its corresponding item
# max_price = 0
# most_costly_item = ''
# for item, price in prices.items():
#   if price > max_price:
#     max_price = price
#     most_costly_item = item
# print(f"Most costly item was ${max_price} by {most_costly_item}")

# we don't have to write .keys() when iterating over a dictionary because default behavior of a for loop is to iterate over the keys of  a dictionary 

for item in prices:
  print(item)