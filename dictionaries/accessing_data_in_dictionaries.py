# Retrieving values using dict[key]
order = {"quantity": 5, "price": 5.99}
print(order['price']) # we use square bracket for indexing a dictionary while curly bracket for creation of dictionary

# the 'key' must match exactly as in creation of dictionary or it will give us a 'KeyError'

print(order["quantitY"])  # KeyError: 'quantitY'
