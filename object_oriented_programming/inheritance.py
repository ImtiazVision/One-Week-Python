# The main idea behind inheritance is that multiple class can share functionalities between them. 
class Cat:
  def __init__(self,name):
    self.name = name
    print('Inside Cat init')
  def meow(self):
    print(f"{self.name} meows")
    
# The following Lion class inherits from the base class Cat on line 9.

class Lion(Cat):
  def __init__(self, name, pride_name):
    print("Inside Lion init")
    # self.name = name 
    super().__init__(name) # here, we are accessing the parent class Cat's  init method. Output: 'Inside Cat init'
    self.pride_name = pride_name
  
  def roar(self):
    print(f"{self.name} roars")
# eli is a Lion, but it can meow even though meow() method is defined on Cat class, because Lion inherits functionalities from base class Cat. 

eli = Lion('Eli', 'bulbul')
eli.meow() # Eli meows

class Cougar(Cat):
  def purr(self):
    print(f"{self.name} purrs")
    
puma = Cougar('Puma')
puma.purr()
puma.meow()
    
