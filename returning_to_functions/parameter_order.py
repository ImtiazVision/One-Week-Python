# When defining functions, the order of parameters matters! The default argument has to come second after positional arguments/parameters.

# this is the order which parameter follows
# (parameters, *args, default parameters, **kwargs)

# here default parameter is: status='married'
def display_info(person, *args, status="married", **kwargs):
  print(f"person is: {person}")
  print(f"status is: {status}")
  print(f"args are : {args}")
  print(f"kwargs are : {kwargs}")

display_info('Jon', True, False, 2,8,10, age=20, mood="happy")