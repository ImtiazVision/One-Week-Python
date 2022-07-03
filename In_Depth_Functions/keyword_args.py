def get_total(price, quantity=1, tax=0.02, discount=0):
  subtotal = price * quantity * (1-discount)
  print(subtotal * (1 + tax))
  
get_total(8.90, 5, 0.0875, 0.15)
# When we call the function, we provide the keyword argument, which is the name of the parameter and its corresponding value. This syntax is similar to the default parameter syntax, except that the default parameter is defined at the beginning of the function where we can optionally put our own value later on, whereas keyword arguments are invoked during function execution by calling it at the end. For keyword arguments, position doesn't matter. 

get_total(price=9.89, discount=0.5, quantity=5, tax=0.05)
