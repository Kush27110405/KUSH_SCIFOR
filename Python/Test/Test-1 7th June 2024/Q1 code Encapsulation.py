"""
Q1 - code for encapsulation
"""
class Student:
  def __init__(self, name, age, cgpa):
    self.__name = name
    self.__age = age
    self.__cgpa = cgpa

  def get_name(self):
    return self.__name

  def get_age(self):
    return self.__age

  def get_cgpa(self):
    return self.__cgpa

  def set_name(self, name):
    self.__name = name

  def set_age(self, age):
    self.__age = age

  def set_cgpa(self, cgpa):
    self.__cgpa = cgpa

student = Student("Ram",17,9.8)
print(student.get_name())
print(student.get_age())
print(student.get_cgpa())

student.set_name("Shyam")
student.set_age(18)
student.set_cgpa(9.9)

print(student.get_name())
print(student.get_age())
print(student.get_cgpa())
