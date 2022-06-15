# 'elif' is a short form for 'else if' in python. We can have as many 'elif' as we want but it has to be after an 'if' statement.

color = input('Please enter your favorite color: \n')

if color == 'black':
  print('Your favorite color is black')
elif color == 'orange':
  print('Your favorite color is orange')
elif color == 'blue':
  print('Your favorite color is blue')
else:
  print('The color is not black, orange or blue')