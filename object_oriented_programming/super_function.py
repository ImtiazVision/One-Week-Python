# super() function is used to refer to the base or parent class. 

class Cat:
  def __init__(self,name):
    self.name = name
  def meow(self):
    print(f"{self.name} meows")

# On line 13,  we use super() to access the __init__ method on from the base/parent Cat class.  
class Lion(Cat):
  
  def __init__(self, name, pride_name):
    super().__init__(name)
    self.pride_name = pride_name
  def roar(self):
    print(f"{self.name} roars")