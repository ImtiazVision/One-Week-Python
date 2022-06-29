# ask for players name
print("Welcome To The Game!")
print("**********************")
num_of_toothpick_remaining = 13
player_1_name = input("Enter player 1's name: ")
player_2_name = input("Enter player 2's name: ")
current_player = player_1_name

# we are going to ask the user how many toothpicks they take while the left_number is > 0
# game loop, until someone wins: we 'break' out of the loop
while True:
  print('| ' * num_of_toothpick_remaining)
  print(f'There are {num_of_toothpick_remaining} toothpicks left.')
# ask player to enter number of toothpick s/he would take away and subsequently subtract that number from original toothpick number
  player_input = int(
      input(f"{current_player}, how many toothpicks do you take? "))
  while player_input != 1 and player_input != 2 and player_input != 3:
    player_input = int(input(f'You can only choose 1, 2, or 3: '))
  num_of_toothpick_remaining -= player_input
# check to see if they win, whoever takes the last toothpick will win!
  if num_of_toothpick_remaining <= 0:
    print(f'{current_player} wins the game!')
    break
  if current_player == player_1_name:
    current_player = player_2_name
  else:
    current_player = player_1_name


print("GAME OVER!!!")
