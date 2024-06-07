"""
Polymorphism Practice Q1 - creating a class "Shape" to calculate the area of different shapes.
"""

import math

class Shape:
  def area(self):
    raise NotImplementedError("Subclasses should implement this method")

class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return math.pi * self.radius ** 2

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width

def calculate_area(l):
  if not isinstance(l,list):
    raise ValueError("l must be a list")
  elif not all(isinstance(i,Circle) or isinstance(i,Rectangle) for i in l):
    raise ValueError("l must contain only Circle or Rectangle objects")
  else:
    for i in l:
      if isinstance(i,Circle):
        print(f"Circle area with radius {i.radius}: {i.area()}")
      else:
        print(f"Rectangle area with length {i.length} and width {i.width}: {i.area()}")

l = [Circle(5),Rectangle(4,5)]
calculate_area(l)
