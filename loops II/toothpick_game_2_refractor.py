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
  num_of_toothpick_remaining -= player_input
# check to see if they win, whoever takes the last toothpick will win!
  if num_of_toothpick_remaining <= 0:
    print(f'{player_1_name} wins the game!')
    break


print("GAME OVER!")