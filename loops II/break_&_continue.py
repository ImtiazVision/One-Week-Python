# we can use the 'break' keyword to prematurely exit a loop. Usually this is done inside of a conditional. 

for char in 'cricketmatch':
  if char == 'm':
    break
  print(char)
print("End of loop")


# The 'continue' keyword end the current iteration of the loop, but does not break out of the loop.