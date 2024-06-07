"""
MRO - Practice
"""

class A:
  def rk(self):
    print("In class A")

class B(A):
  def rk(self):
    print("In class B")

class C(A):
  def rk(self):
    print("In class C")

class D(B,C):
  pass
    

d = D()
d.rk()
