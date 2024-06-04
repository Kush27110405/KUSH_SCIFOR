"""
Encapsulation Q1 :- creating a class "Car" to encapsulate the "Brand" of a car. (discussed in class)
"""
class Car:
  def __init__(self,brand,model,year):
    self.__brand = brand  # private attribute - encapsulation
    self.model = model #public
    self.year = year #public

  def get_brand(self):#  Public method to access private attribute
    return self.__brand

  def accelerate(self):
    print(f"The {self.model} is accelerating!")

my_car = Car("Tesla","Model 5",2023)
print(my_car.model)

#print(my_car.__brand) --- wrong!

print(my_car.get_brand())
