# Scope/boundary means where can we reference a given variable 
# 4 types of scoping
# Lexical, Enclosing, Global, Built-in (LEGB)
# Global Scope: Variables declared outside of functions are in the global scope. All functions have access to them.

movie = 'Titanic'
def review():
  print(movie)
  def inner():
    print(movie)
    
  inner()
review()
