print('WELCOME TO OUR SHOPPING CART')
print('***************************')
item = input('What item are you purchasing?\n')
price = float(input(f'What is the price of {item}?\n'))
quantity = int(input(f'How many {item} are you purchasing?\n'))

print(f"You are purchasing {quantity} {item} at ${price} each with a total of ${quantity * price}")

