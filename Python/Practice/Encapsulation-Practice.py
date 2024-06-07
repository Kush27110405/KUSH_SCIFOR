"""
Encapsulation Practice Q1 - creating a class "Student" to encapsulate the name and grades of the student
"""

class Student:
    def __init__(self, name, grades=None):
        self._name = name
        self._grades = grades if grades is not None else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value):
        if not isinstance(value, list) or not all(isinstance(grade, int) for grade in value):
            raise ValueError("Grades must be a list of integers.")
        self._grades = value

    def add_grade(self, grade):
        if not isinstance(grade, int):
            raise ValueError("Grade must be an integer.")
        self._grades.append(grade)

# Usage
student = Student("Alice")
print(student.name)  # Output: Alice

student.name = "Bob"
print(student.name)  # Output: Bob

student.grades = [90, 85, 92]
print(student.grades)  # Output: [90, 85, 92]

student.add_grade(88)
print(student.grades)  # Output: [90, 85, 92, 88]

# Trying to set invalid values
try:
    student.name = 12345
except ValueError as e:
    print(e)  # Output: Name must be a string.

try:
    student.grades = [90, "A", 85]
except ValueError as e:
    print(e)  # Output: Grades must be a list of integers.

try:
    student.add_grade("A")
except ValueError as e:
    print(e)  # Output: Grade must be an integer.
