# LEGB 
# Local > Enclosing/nested inner > Global > Built-in

book = 'fiction'
def outer():
  book = 'non-fiction' # because book is re-defined in the function again and local scope take precedence over global scope, 'non-fiction' is printed on the console.
  print(book)
outer()