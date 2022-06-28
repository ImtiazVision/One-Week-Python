# ask for players name
print("Welcome To The Game!")
print("**********************")
num_of_toothpick_remaining = 13
player_1_name = input("Enter player 1's name: ")
player_2_name = input("Enter player 2's name: ")

# we are going to ask the user how many toothpicks they take while the left_number is > 0
# game loop, until someone wins: we 'break' out of the loop
while True:
  print('| ' * num_of_toothpick_remaining)
  print(f'There are {num_of_toothpick_remaining} toothpicks left.')
# ask player 1 to enter number of toothpick s/he would take away and subsequently subtract that number from original toothpick number
  player_1_input = int(input(f"{player_1_name}, how many toothpicks do you take? "))
  num_of_toothpick_remaining -= player_1_input
# check to see if they win, whoever takes the last toothpick will win!
  if num_of_toothpick_remaining <=0:
    print(f'{player_1_name} wins the game!')
    break

  print('| ' * num_of_toothpick_remaining)
  print(f'There are {num_of_toothpick_remaining} toothpicks left.')
# ask player 2 to enter number of toothpick s/he would take away and subsequently subtract that number from original toothpick number 
  player_2_input = int(
      input(f"{player_2_name}, how many toothpicks do you take? "))
  num_of_toothpick_remaining -= player_2_input
# check to see if they win, whoever takes the last toothpick will win!
  if num_of_toothpick_remaining <=0:
    print(f'{player_2_name} wins the game!')
    break
print("GAME OVER!")






