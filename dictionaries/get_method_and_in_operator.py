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

product = input("What product are you going to purchase today? ")
if product in prices:
  price = prices[product]
  print(f"{product} is ${price}")
