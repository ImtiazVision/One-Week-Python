# Scopes in loops and conditionals are considered as global scope as codes are accessible outside the loop

for element in 'abcdef':
  color = 'blue'
  print(element)
  
if True:
  animal = 'Tiger'
print(f'After conditional: {animal}')
print(f'After loop: {color}')