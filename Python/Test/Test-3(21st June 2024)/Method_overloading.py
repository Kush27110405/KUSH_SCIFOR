"""
Question 3:- Python Program demonstrating method overloading
"""

"""
Method overloading :-  Phenomena where two or more methods 
have the same name but different number and/or type of parameters.
These methods are called overloaded methods.
"""
from multipledispatch import dispatch

"""
Implementation using multiple dispatch decorator:-

A decorator is a tool which is used to wrap a function, for the purpose of extending the behaviour of the wrapped function,
without permanently modifying it.

In backend, the Dispatcher creates an object for each different type of implementation of the overloaded method,
and on runtime, selects the appropriate method with the correct type and no. of arguments passed.
"""

@dispatch(int, int)
def add(a, b):
  return a + b

@dispatch(int, int, int)
def add(a, b, c):
  return a + b + c

@dispatch(float, float, float)
def add(a, b, c):
  return a + b + c

print(add(1, 2))
print(add(1, 2, 3))
print(add(1.1, 2.2, 3.3))

"""
Output:-

3
6
6.6
"""
