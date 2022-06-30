# The "return" keyword outputs whatever value comes after the "return" keyword. It terminates the execution of a function. It means we can only get a single value from a function. We can have multiple 'return' statements, but only one of them will execute(the first one). 

def multiply(a,b):
  return a*b
# We can save the outcome of the function in a variable and then print it out.
result = multiply(8,8)
print(result)
