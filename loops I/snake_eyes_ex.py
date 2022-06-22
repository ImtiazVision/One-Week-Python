from random import randint
roll_1 = randint(1,6)
roll_2 = randint(1,6) 
roll_count = 1

while roll_1 != 1 or roll_2 != 1:
  print(roll_1, roll_2)
  roll_1 = randint(1,6)
  roll_2 = randint(1,6)
  roll_count += 1
  
print(roll_1, roll_2)
print("Yay, that was a snake eyes !!!")
print(f"It took {roll_count} rolls to get the snake eyes!")