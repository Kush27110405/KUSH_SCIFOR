# Question 1:- calculating the area of a rectangle using function :

def area(length,breadth):
  if length <=0 or breadth <= 0:
    return "Invalid Dimensions"

  return length * breadth

length = float(input("Enter the length of the rectangle :"))
breadth = float(input("Enter the breadth of the rectangle : "))

result = area(length,breadth)
print(result)
