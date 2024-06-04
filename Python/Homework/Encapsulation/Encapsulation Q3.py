"""
Encapsulation Q3 - creating a class "Employee" to encapsulate the employee id and salary
"""

class Employee:
  def __init__(self,employee_id,salary):
    self.__employee_id = employee_id if isinstance(employee_id,int) else None
    self.__salary = salary if isinstance(salary,float) else None

  @property
  def employee_id(self):
    return self.__employee_id

  @property
  def salary(self):
    return self.__salary

  def raise_salary(self,percentage):
    self.__salary += (self.__salary * percentage/100)

  @employee_id.setter
  def employee_id(self,employee_id):
    if not isinstance(employee_id,int):
      print("Employee_id must be an integer")
    else:
      self.__employee_id = employee_id

  @salary.setter
  def salary(self,salary):
    if not isinstance(salary,float):
      print("Salary must be a decimal value.")
    else:
      self.__salary = salary

emp = Employee("A","B")
print(emp.employee_id)
print(emp.salary)

emp.employee_id = 101
print(emp.employee_id)

emp.salary = 10000.0
print(emp.salary)

emp.raise_salary(10)
print(emp.salary)
