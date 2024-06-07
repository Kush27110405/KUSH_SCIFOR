"""
Q9:- code for functions
"""

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


num_terms = int(input("Enter the number of terms: "))
print(f"First {num_terms} terms of the Fibonacci sequence: {fibonacci(num_terms)}")
