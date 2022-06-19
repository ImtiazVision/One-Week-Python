#NOT
#AND
#OR
# NOT comes before AND and AND comes before OR

day = "Monday"
is_vet = False
age = 80

# Veterans get a 10% discount
# teenagers get a 20% discount

# if age <= 20 or is_vet and day == "Monday":
    # print("You get in for free today!!!")

# if not (age <= 20 or is_vet and day == "Monday"):
#         print("You have to buy a ticket!")
        
gets_in_for_free = age <= 20 or is_vet and day == "Monday"

if not gets_in_for_free:
    print("You have to buy a ticket!")