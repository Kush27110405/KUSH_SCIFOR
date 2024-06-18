"""
Question:-
Filter Odd Numbers:
Write a lambda function to filter out all the odd numbers from a given list. 
Use the filter() function along with your lambda function to achieve this.
"""

l = []
n = int(input("Enter the no. of integers in your list:"))
for i in range(0, n):
    l.append(int(input("Enter integer:")))

even = filter(lambda x: x % 2 == 0, l)
print("Filtered list:", list(even))

"""
Output:-

Enter the no. of integers in your list:3
Enter integer:-34
Enter integer:-57
Enter integer:25
Filtered list: [-34]

"""
