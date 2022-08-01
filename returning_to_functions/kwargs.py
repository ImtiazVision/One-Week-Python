# **kwargs: We can use the '**' notation to write functions that accept any number of keyword arguments. This '**kwargs' are applicable to dictionaries. 

def print_ages(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} is {value} years old")
    
print_ages(John=21, Kim=41, Sam=29)

