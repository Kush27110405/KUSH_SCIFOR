class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.department = department

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}, Course: {self.course}")

class Intern(Employee, Student):
    def __init__(self, name, age, employee_id, department, student_id, course):
        super().__init__(name, age, employee_id, department)
        self.student_id = student_id
        self.course = course

    def display(self):
        super().display()
        #print(f"Student ID: {self.student_id}, Course: {self.course}")


# Creating objects and displaying their information
person = Person("Alice", 30)
employee = Employee("Bob", 40, "E123", "Engineering")
student = Student("Charlie", 20, "S456", "Computer Science")
intern = Intern("Daisy", 22, "E789", "Marketing", "S789", "Business")

print("Person Info:")
person.display()
print("\nEmployee Info:")
employee.display()
print("\nStudent Info:")
student.display()
print("\nIntern Info:")
intern.display()

"""
Output:- 

Person Info:
Name: Alice, Age: 30

Employee Info:
Name: Bob, Age: 40
Employee ID: E123, Department: Engineering

Student Info:
Name: Charlie, Age: 20
Student ID: S456, Course: Computer Science

Intern Info:
Name: Daisy, Age: 22
Student ID: S789, Course: Business
Employee ID: E789, Department: Marketing
"""
