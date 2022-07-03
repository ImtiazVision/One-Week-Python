def get_total(price, quantity=1, tax=0.02, discount=0):
  subtotal = price * quantity * (1-discount)
  print(subtotal * (1 + tax))
  
get_total(8.90, 5, 0.0875, 0.15)
# Writing out the name of the parameter and its corresponding value is known as keyword argument when we call the function. It is similar to default parameter except that default parameter is defined at the beginning of the function while keyword arguments are invoked during the function call at the end of the function. 