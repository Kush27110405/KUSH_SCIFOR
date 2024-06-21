"""
Question 2:- Python Program demonstrating method overriding
"""

class A:
  def show(self):
    return "In A"

class B(A):
  def show(self):
    return "In B"

class C(B):
  def show(self):
    return "In C"

a = A()
b = B()
c = C()

print(a.show())
print(b.show())
print(c.show())

"""
Output:-

In A
In B
In C
"""
