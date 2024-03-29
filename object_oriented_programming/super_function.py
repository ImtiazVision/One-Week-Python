# super() function is used to refer to the base or parent class. Sometimes, we need to access functionalities/methods from the parent/base class and super() does exactly that for us. 

class Cat:
  def __init__(self,name):
    self.name = name
  def meow(self):
    print(f"{self.name} meows")

# On line 13,  we use super() to access the __init__ method on from the base/parent Cat class.  
class Lion(Cat):
  
  def __init__(self, name, pride_name):
    super().__init__(name) # here we are accessing parent/base class's init 
    self.pride_name = pride_name
    
  def roar(self):
    print(f"{self.name} roars")