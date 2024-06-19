"""
Question:-
Given two sets of integers, set1 and set2, 
write a function union_and_intersection(set1, set2) that returns a tuple containing the union and intersection of these sets.
"""

def union_and_intersection(set1, set2):
  union = set1 | set2
  intersection = set1 & set2
  return tuple((union, intersection))

set1 = set()
set2 = set()

m = int(input("Enter the number of integers in first set: "))
for i in range(m):
    x = int(input("Enter integer no." + str(i + 1) + " of first set: "))
    set1.add(x)

n = int(input("Enter the number of integers in second set: "))
for i in range(n):
    y = int(input("Enter integer no." + str(i + 1) + " of second set: "))
    set2.add(y)

print(union_and_intersection(set1, set2))

"""
Output:-

Enter the number of integers in first set: 3
Enter integer no.1 of first set: 1
Enter integer no.2 of first set: 2
Enter integer no.3 of first set: 3
Enter the number of integers in second set: 4
Enter integer no.1 of second set: 2
Enter integer no.2 of second set: 3
Enter integer no.3 of second set: 4
Enter integer no.4 of second set: 5
({1, 2, 3, 4, 5}, {2, 3})
"""
