# prices = {
#   'mango': 2.99,
#   'strawberry': 4.99,
#   'peach': 2.44,
#   'watermelon': 3.11,
#   'coconut': 4.99,
#   'basil': 2.55
# }

# nested dictionary 
produce = {
  'mango': {
    'price': 2.99,
    'quantity': 44,
    'organic': True,
    'producer': 'Parley Farm '
  },
    'basil': {
    'price': 2.99,
    'quantity': 21,
    'organic': False,
    'producer': 'Mike Temper Farm'
  }
}

# print(produce['basil'])
# print(produce['basil']['quantity'])

# dictionary of lists are pretty common
test_scores = {
  "Amir": [89,99,80],
  "Sabin": [78, 89, 94]

}

# lists of dictionary are also pretty common 
waitlist = [
  {
    'email': 'john@email.com',
    'location': 'North America',
    'first_name': 'John',
    'last_name': 'Wolf'
  },
  {
      'email': 'Juan@email.com',
      'location': 'South America',
      'first_name': 'Juan',
      'last_name': 'Asker'
  }
]
