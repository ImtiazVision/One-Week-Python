def get_total(price, quantity=1, tax=0.02, discount=0):
  subtotal = price * quantity * (1-discount)
  print(subtotal * (1 + tax))
  
get_total(8.90, 5, 0.0875, 0.15)