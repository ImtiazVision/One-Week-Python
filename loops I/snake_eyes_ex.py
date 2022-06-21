from random import randint
roll_1 = randint(1,6)
roll_2 = randint(1,6) 

while roll_1 != 1 or roll_2 != 1:
  print(roll_1, roll_2)
  roll_1 = randint(1,6)
  roll_2 = randint(1,6)
print(roll_1, roll_2)
print("Yay, that was a snake eyes !!!")