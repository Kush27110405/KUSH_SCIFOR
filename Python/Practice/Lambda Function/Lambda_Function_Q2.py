"""
Question:-

Sort a List of Tuples:
You have a list of tuples where each tuple contains two elements - a string and an integer.
Write a lambda function to sort this list based on the integer values in ascending order.
"""

l = []
n = int(input("Enter the no. of tuples in your list:"))
for i in range(0, n):
  s = input("Enter String for tuple no." + str(i + 1) + ": ")
  m = int(input("Enter integer for tuple no." + str(i + 1) + ": "))
  l.append(tuple((s, m)))

sorted_list = sorted(l, key=lambda x: x[1])
print("Sorted list:", sorted_list)

"""
Output:-

Enter the no. of tuples in your list:3
Enter String for tuple no.1: apple
Enter integer for tuple no.1: -34
Enter String for tuple no.2: banana
Enter integer for tuple no.2: 2
Enter String for tuple no.3: cherry
Enter integer for tuple no.3: -23
Sorted list: [('apple', -34), ('cherry', -23), ('banana', 2)]
"""
