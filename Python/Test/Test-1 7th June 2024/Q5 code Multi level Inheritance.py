"""
Q5:- code for multi level inheritance
"""
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    return "Animal Sound"

class Mammal(Animal):
  def speak(self):
    return "Mammal Sound"

class Dog(Mammal):
  def speak(self):
    return "Woof!"
    
class Cat(Mammal):
  def speak(self):
    return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
