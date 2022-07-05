# Enclosing scope: Nested 'inner' functions have access to variables declared in outer parent functions.

def outside():
  a = 10
  def inside():
    print('a is: ', a) # nested function inside() has access to the variable declared in the parent function 'a'
  inside() # executing the function
  def third():
    print("Third inner function and variable 'a' is still available", a)
  third() # calling/executing function
outside()