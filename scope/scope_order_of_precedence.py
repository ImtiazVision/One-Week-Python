# LEGB 
# Local > Enclosing/nested inner > Global > Built-in

book = 'fiction'

def outer():
  book = 'non-fiction' # because book is re-defined in the function again and local scope take precedence over global scope, 'non-fiction' is printed on the console.
  
  def inner():
    print("From inner function :", book)
    print(str) # str is a built-in function and python will go through LEGB and find it as Built-in function and print it out on console
  inner()
    
  print("From outer function: ",book)
  
  
print("From outside of all function: ", book)

outer()