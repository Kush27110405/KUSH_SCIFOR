"""
Encapsulation:- It is one of the pillars of OOPS, which means that the attributes and methods are bundled together
into a single unit in a class.
This essentially means that the access to the attributes and methods are restricted(made private).
This is also known as data hiding.

To make the attributes private, we use double underscore before the name of the attribute(like self.__name)
To access the private attributes, we use getter and setter methods, like get_function_name() and set_function_name()
"""

"""
Real Life example:-
 In a company, there are various departments, such as sales, HR, finance, Operations, etc. 
 Now a person outside of the sales department cannot directly access the data of sale statistics. 
 He/she needs to ask the sales department to provide the data.
 Only the people in the sales department can access and modify the sales data.

Similarly, it is not possible to access the private attributes of a class directly from outside the class. 
We need to use getter and setter methods.
"""

#Implementation:-
class Employee:
    def __init__(self, name, employee_id, position, salary, performance_reviews):
      self.__name = name
      self.__employee_id = employee_id
      self.__position = position
      self.__salary = salary
      self.__performance_reviews = performance_reviews if isinstance(performance_reviews, list) and all((j >= 1 and j<=5) for j in performance_reviews) else []

    def get_name(self):
      return self.__name
    
    def get_employee_id(self):
      return self.__employee_id

    def get_position(self):
      return self.__position

    def get_salary(self):
      return self.__salary

    def set_name(self, name):
      self.__name = name

    def set_position(self, position):
      self.__position = position

    def raise_salary(self, percentage):
      self.__salary = self.__salary * (1 + percentage/100)

    def add_performance_review(self, review):
      if review >= 1 and review <= 5:
        self.__performance_reviews.append(review)
      else:
        print("Invalid performance review. Please enter a number between 1 and 5.")

    def avg_performance_review_score(self):
      if len(self.__performance_reviews) == 0:
        return 0
      return sum(self.__performance_reviews) / len(self.__performance_reviews)

    def eligible_for_bonus(self):
      if self.avg_performance_review_score() >= 4.5:
        return True
      return False

employee = Employee("Kush",1001,"Junior Data Scientist",50000,[4,4,5])
print(employee.get_name())
print(employee.get_employee_id())
print(employee.get_position())
print(employee.get_salary())

employee.set_name("Abhishek")
employee.set_position("Senior Data Scientist")
print(employee.get_name())
print(employee.get_position())

employee.raise_salary(10)
print(employee.get_salary())

employee.add_performance_review(4)
employee.add_performance_review(5)
print(employee.avg_performance_review_score())

print(employee.eligible_for_bonus())

"""
Sample Output:-

Kush
1001
Junior Data Scientist
50000
Abhishek
Senior Data Scientist
55000.00000000001
4.4
False

"""
