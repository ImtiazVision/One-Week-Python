# 'in' operator will only look at the 'keys', not the values in a dictionary. The 'in' operator is used to find out whether a key exists in a dictionary or not. 

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print("Batman" in phone_book)
print("Godzilla" in phone_book)

prices = {
  'coconut': 5.11,
  'strawberries': 4.99,
  'orange': 3.99,
  'blueberries': 2.99,
  'blackberries': 4.15,
  'basil': 2.99
}

# product = input("What product are you going to purchase today? ")
# if product in prices:
#   price = prices[product]
#   print(f"{product} is ${price}")
# else:
#   print("This product is not available!!! ")
  
# dict.get() method will look for a given key in a dictionary. If the key exists, it will return the corresponding value. Otherwise it returns None. If we want a value for a key that may or may not exist in a dictionary, we ust get() method. 

product = input("What product are you going to purchase today? ")
price = prices.get(product)
if price:
  print(f"{product} is ${price}")
else:
  print("This product is not available!!! ")
