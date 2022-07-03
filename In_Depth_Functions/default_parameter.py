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

slugify("Hi there welcome to python study")
slugify("Hi there welcome to python study", "_") # 