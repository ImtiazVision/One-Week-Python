from audioop import mul


list1 = [2,3,4,5]
list2 = [1,3,5,7]

# addition = list1 + list2
# multiplication = list1 * 6
# in operator 

print(3 in list1) # True

ice_cream = ['birthday_cake', 'piece_of_cake', 'butter_pecan', 'strawberry_cheesecake']

user_choice = input("What kind of ice cream would you like?")

while user_choice.lower() not in ice_cream:
  user_choice = input("Please choose ice cream from the above menu list. What kind of ice cream would you like?")
print(f"OK, {user_choice} will be served momentarily...")
