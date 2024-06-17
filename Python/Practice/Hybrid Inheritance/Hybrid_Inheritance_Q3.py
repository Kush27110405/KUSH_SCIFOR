class A:
    def show(self):
        print("Method from class A")

    def extra(self):
        print("Extra method from class A")

class B(A):
    def show(self):
        print("Method from class B")
        super().show()  # Ensure calling A's show method

    def extra(self):
        print("Extra method from class B")
        super().extra()  # Ensure calling A's extra method

class C(A):
    def show(self):
        print("Method from class C")
        super().show()  # Ensure calling A's show method

    def extra(self):
        print("Extra method from class C")
        super().extra()  # Ensure calling A's extra method

class D(B, C):
    def show(self):
        print("Method from class D")
        super().show()  # Calls B's show method

    def extra(self):
        print("Extra method from class D")
        super().extra()  # Calls B's extra method

# Instantiate an object of class D
d_instance = D()

# Call the show method
print("Calling show method on D instance:")
d_instance.show()

# Call the extra method
print("\nCalling extra method on D instance:")
d_instance.extra()

# Print the Method Resolution Order (MRO)
print("\nMRO of class D:")
print(D.__mro__)

"""
Output:-

Calling show method on D instance:
Method from class D
Method from class B
Method from class C
Method from class A

Calling extra method on D instance:
Extra method from class D
Extra method from class B
Extra method from class C
Extra method from class A

MRO of class D:
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""
