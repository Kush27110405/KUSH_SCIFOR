"""
Q3:- code for single level inheritance
"""
class Animal:
  def eat(self):
    return "Eating"

class Dog(Animal):
  def bark(self):
    return "Barking"

dog = Dog()
print(dog.eat())
print(dog.bark())
