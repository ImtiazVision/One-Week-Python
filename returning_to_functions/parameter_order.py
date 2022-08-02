# When defining functions, the order of parameters matters! The default argument has to come second after positional arguments/parameters.

# this is the order which parameter follows
# (parameters, *args, default parameters, **kwargs)

def display_info(person, status="married"):
  print(f"person is: {person}")
  print(f"status is: {status}")

display_info('Jon')