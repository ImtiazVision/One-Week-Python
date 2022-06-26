from random import randint

num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))
# 

while True:
  divider = "|"
  for die in range(num_dice):
    rand = randint(1, num_sides)
    divider += f'{rand}|'
  print(divider)
  reply = input("Roll again? ('q' to quit)")
  if reply == 'q':
    break

