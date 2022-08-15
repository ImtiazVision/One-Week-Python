# We can define methods that are available on the class directly. These class methods are not concerned with a specific instance of the class. 

class Puppy:
  species = 'canine'
  
  @classmethod
  def register_anon(cls):
    return cls('unknown')
  
  def __init__(self, name):
    self.name = name
    self.tricks = []