# unit = 'fahrenheit'
unit = 'celsius'
temp = int(input('Enter the temperature: '))

if unit == 'fahrenheit':
  if temp <= 32:
    print('It is freezing outside.')
  else:
    print('It is not freezing outside.')
else:
  print('I am not too sure about celsius.')