# Without Recursion

def factorial_Fun(n):
    """
    factorial without recursion
    """
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

n = int(input())
fact = factorial_Fun(n)
print(fact)

# Using Recursion

def fact(n):
    """
    factorial with recursion
    """
    if n < 0:
        return None
    if n < 2:
        return 1
    return n*(fact(n-1))
    
print(fact(5))