class Dog:
  def __init__(self, name, breed, location):
    self.name = name
    self.breed = breed
    self.location = location
    self.tricks = []
    
german = Dog('Elmo','German Shepard', 10001)
print(german.name)
print(german.breed)
print(german.location)