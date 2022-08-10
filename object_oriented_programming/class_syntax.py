# To define a class, first thing we need is the 'class' keyword and class name is Capitalized.

# __init__ is a special method that is automatically called whenever a new class i.e. Puppy is created(instantiated). 

# self: the 'self' keyword refers to the 'current' instance of the class i.e. Puppy. The 'self' must be the first parameter to '__init__'. 'self' keyword will hold the reference to the current Puppy instance. 
class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
#Instantiating: To create a Puppy instance, we call Puppy() and provide a name. 

mickey = Puppy('Mickey')
print(mickey.name)
print(mickey.tricks)