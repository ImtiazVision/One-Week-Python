# We can define methods that are available on the class directly. These class methods are not concerned with a specific instance of the class. Class method helps us create new instances within that class. 

class Puppy:
  species = 'canine'
  
  @classmethod    # this is a decorator 
  def register_anon(cls):
    return cls('unknown')
  
  def __init__(self, name):
    self.name = name
    self.tricks = []