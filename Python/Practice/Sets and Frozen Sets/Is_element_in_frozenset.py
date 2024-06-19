"""
Question:-
Write a function is_element_in_frozenset(fset, element) that takes a frozen set fset and an integer element, 
and returns True if the element is in the frozen set, and False otherwise.
"""

def is_element_in_frozenset(frozenset, element):
    if element in frozenset:
        return True
    else:
        return False

n = int(input("Enter the number of integer elements in your frozen set: "))
l = []
for i in range(n):
    x = int(input("Enter integer element no. " + str(i + 1) + " : "))
    l.append(x)
s = frozenset(l)
element = int(input("Enter the element to be searched:"))
print(is_element_in_frozenset(s, element))

"""
Output:-

Enter the number of integer elements in your frozen set: 3
Enter integer element no. 1 : 234
Enter integer element no. 2 : 763
Enter integer element no. 3 : 1035
Enter the element to be searched:763
True
"""
