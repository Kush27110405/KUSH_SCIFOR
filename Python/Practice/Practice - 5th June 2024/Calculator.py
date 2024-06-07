def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def div(a,b):
  return a / b

def calculate(func,a,b):
  return func(a,b)

print(calculate(add,10,5))
print(calculate(sub,10,5))
print(calculate(mul,10,5))
print(calculate(div,10,5))
