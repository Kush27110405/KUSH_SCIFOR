class A:
  def show(self):
    print("Show Method in A")

  def extra(self):
    print("Extra Method in A")

class B(A):
  def show(self):
    print("Show Method in B")

  def extra(self):
    print("Extra Method in B")

class C(A):
  def show(self):
    print("Show Method in C")

  def extra(self):
    print("Extra Method in C")

class D(B, C):
  def show(self):
    print("Show Method in D")
    super().show()

  def extra(self):
    print("Extra Method in D")
    super().extra()

class E(D):
  def show(self):
    print("Show Method in E")
    super().show()

  def extra(self):
    print("Extra Method in E")
    super().extra()

e = E()
e.show()
e.extra()


print("MRO of class E:")
print(E.__mro__)

"""
Output:-

Show Method in E
Show Method in D
Show Method in B
Extra Method in E
Extra Method in D
Extra Method in B
MRO of class E:
(<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""
