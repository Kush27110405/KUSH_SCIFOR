"""
Question:-
Given two sets of strings, setA and setB, write a function difference_and_symmetric_difference(setA, setB) 
that returns a dictionary with keys "difference" and "symmetric_difference" 
corresponding to the difference (setA - setB) and symmetric difference of the two sets.
"""

def difference_and_symmetric_difference(set1, set2):
    difference = set1 - set2
    symmetric_difference = set1 - set2 | set2 - set1
    dict = {
        'difference': difference,
        'symmetric_difference': symmetric_difference
    }
    return dict

set1 = set()
set2 = set()

m = int(input("Enter the number of elements in first set: "))
for i in range(m):
  x = input("Enter element no. " + str(i + 1) + " of first set: ")
  set1.add(x)

n = int(input("Enter the number of elements in second set: "))
for i in range(n):
  y = input("Enter element no. " + str(i + 1) + " of second set: ")
  set2.add(y)

print(difference_and_symmetric_difference(set1, set2))

"""
Output:-

Enter the number of elements in first set: 3
Enter element no. 1 of first set: apple
Enter element no. 2 of first set: banana
Enter element no. 3 of first set: cherry
Enter the number of elements in second set: 3
Enter element no. 1 of second set: banana
Enter element no. 2 of second set: cherry
Enter element no. 3 of second set: kiwi
{'difference': {'apple'}, 'symmetric_difference': {'apple', 'kiwi'}}
"""
