# Default parameters are used to offer a default value for a parameter if no argument is provided. Using this method, we can easily add the default: parameter=value

def sound_level(level=4):
  return("Buzz "* level)

extreme = sound_level(10)
default = sound_level()

print(extreme)
print(default)
  
#******************************************

def slugify(phrase, separated_by="-"):
  return phrase.lower().strip().replace(" ", separated_by) 

result_with_default_argument = slugify("Hi there welcome to python study")
print(result_with_default_argument)
result_with_provided_argument = slugify("Hi there welcome to python study", "_") # or we can provide our own argument "_" underscore
print(result_with_provided_argument)