"""
Question:-

Map Function with Lambda:
Write a lambda function that takes a list of integers and returns a list with each integer squared. 
Use the map() function along with your lambda function to achieve this.
"""

l = []
n = int(input("Enter the number of integers in your list:"))
for i in range(0, n):
    l.append(int(input("Enter integer:")))

result = map(lambda x: x ** 2, l)
print("Square of each element in the list:", list(result))


"""
Output:-

Enter the number of integers in your list:3
Enter integer:57
Enter integer:-89
Enter integer:22
Square of each element in the list: [3249, 7921, 484]
"""
