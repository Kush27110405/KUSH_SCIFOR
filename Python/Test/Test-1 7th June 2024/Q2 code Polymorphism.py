"""
Q2 - code for polymorphism
"""
class Vehicle:
  def drive(self):
    return "Vehicle is driving"

class Car(Vehicle):
  def drive(self):
    return "Car is driving"

class Bike(Vehicle):
  def drive(self):
    return "Bike is driving"

def driving(vehicle):
  return vehicle.drive()

car = Car()
bike = Bike()

print(driving(car))
print(driving(bike))
