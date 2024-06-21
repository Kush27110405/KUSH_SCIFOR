"""
Question 1:- Python program demonstrating all types of inheritance
"""
class A:             # Base class 1
  def show(self):
    print("In A")

#Hierarchical Inheritance :- creating two subclasses B and C w.r.t parent class A

class B(A):
  def show(self):
    print("In B")
    super().show()

class C(A):
  def show(self):
    print("In C")
    super().show()

#Multi level Inheritance :- creating a child class D of parent class B, which is child of A

class D(B):
  def show(self):
    print("In D")
    super().show()

# Base class 2:-

class X:
  def show(self):
    print("In X")

# Single level inheritance:- creating one child class Y of parent class X

class Y(X):
  def show(self):
    print("In Y")
    super().show()

# demonstrating both multiple inheritance and hybrid inheritance:- 

class E(D, Y):    # Hybrid inheritance(also includes multiple inheritance)
  def show(self):
    print("In E")
    super().show()

e = E()
y = Y()
e.show()
print("\n")
y.show()
print("\n")
c = C()
c.show()
print("\n")
d = D()
d.show()
print("\n")
b = B()
b.show()
print("\n")
x = X()
x.show()
print("\n")
a = A()
a.show()

"""
Output:-

In E
In D
In B
In A


In Y
In X


In C
In A


In D
In B
In A


In B
In A


In X


In A
"""
