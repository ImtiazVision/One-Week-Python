# unit = 'fahrenheit'
# unit = 'celsius'
# temp = int(input('Enter the temperature: '))

# if unit == 'fahrenheit':
#   if temp <= 32:
#     print('It is freezing outside.')
#   else:
#     print('It is not freezing outside.')
# else:
#   print('I am not too sure about celsius.')

fav_season = 'summer'
fav_food   = 'beef' 
fav_drink  = 'smoothie'

# following are nested conditional statements and in order for all of them to run, all must be true 
if fav_season == 'summer':
  print("It's a great summer!")
  if fav_food == 'beef':
    print("I love beef.")
    if fav_drink == 'smoothie':
      print("I love smoothie.")