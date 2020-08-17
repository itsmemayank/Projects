#Using Without Recursion
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    print(elem1,elem2,sep="\n")
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
        print(elem2)
    return sum

a = fib(3)
print("Result :",a)

#Using With Recursion

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
    
print(fib(10))