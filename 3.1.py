"""
3.1 Collatz

Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function 
returns the value 1. 
"""

def collatz(n):
    """
    Natural -> Natural
    Compute next element in collatz sequence
    """
    if n % 2 == 0:
        n = n // 2
        print(n)
        return n    
    else:
        n = (3 * n) + 1
        print(n)
        return n

print("Choose number: ")
n = 0
while n == 0:
    try:
        n = int(input())
    except ValueError:
        print("Please enter an integer")
        
while n != 1:
    n = collatz(n)


